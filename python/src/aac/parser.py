"""Parse Architecture-as-Code YAML files.

The AaC parser reads a YAML file, performs validation (if not suppressed) and provides
the caller with a dictionary of the content keyed by the named type.  This allows you
to find a certain type in a model by just looking for that key.
"""

import os

import yaml
from attr import Factory, attrib, attrs, validators
from yaml.parser import ParserError as YAMLParserError


def parse_file(arch_file: str) -> dict[str, dict]:
    """Parse an Architecture-as-Code YAML file.

    Arguments:
        arch_file (str): The Architecture-as-Code YAML file to be parsed.

    Returns:
        The parse method returns a dict of each root type defined in the Arch-as-Code spec. If
        validation of the provided YAML file fails, an error message is displayed and None is
        returned.
    """
    parsed_models: dict[str, dict] = {}

    files = _get_files_to_process(arch_file)
    for file in files:
        contents = _read_file_content(file)
        parsed_models = parsed_models | parse_str(arch_file, contents)
    return parsed_models


def parse_str(source: str, model_content: str) -> dict[str, dict]:
    """Parse a string containing one or more YAML model definitions.

    Arguments:
        source:  The file the content came from (to help with better logging)
        model_content:  The YAML to parse

    Returns:
        A dictionary of the parsed model(s). The key is the type name from the model and the
        value is the parsed model root.
    """
    parsed_models = {}

    roots = _load_yaml(source, model_content)
    for root in roots:
        if "import" in root:
            del root["import"]

        if not isinstance(root, dict):
            raise ParserError(source, ["provided content was not YAML", model_content])

        root_name, *_ = root.keys()
        root_item = root.get(root_name)

        if not root_item:
            raise ParserError(source, ["incomplete model:", model_content, ""])

        parsed_models = parsed_models | {root_item.get("name"): root}
    return parsed_models


def _load_yaml(source: str, content: str) -> dict:
    """Parse content as a YAML string and return the resulting structure.

    Arguments:
        source (str): The source of the YAML content. Used to provide better error messages.
        content (str): The YAML content to be parsed.

    Returns:
        The parsed YAML content.

    Raises:
        If the YAML is invalid, a ParserError is raised.
    """
    try:
        return list(yaml.load_all(content, Loader=yaml.SafeLoader))
    except YAMLParserError as error:
        raise ParserError(source, [f"invalid YAML {error.context}", error.problem, content])


def _read_file_content(arch_file: str) -> str:
    """
    Read file content method extracts text content from the specified file.

    Arguments:
        arch_file: The file to read.

    Returns:
        The contents of the file as a string.
    """
    arch_file_path = arch_file
    content = ""
    with open(arch_file_path, "r") as file:
        content = file.read()
    return content


def _get_files_to_process(arch_file_path: str) -> list[str]:
    """Return a list of all files referenced in the model.

    Traverse the import path starting from the specified Arch-as-Code file and returns a list of
    all files referenced by the model.
    """
    ret_val = [arch_file_path]
    content = _read_file_content(arch_file_path)
    roots = _load_yaml(arch_file_path, content)
    for root in roots:
        if root and isinstance(root, dict) and "import" in root.keys():
            for imp in root["import"]:
                # parse the imported files
                parse_path = ""
                if imp.startswith("."):
                    # handle relative path
                    arch_file_dir = os.path.dirname(os.path.realpath(arch_file_path))
                    parse_path = os.path.join(arch_file_dir, imp)
                else:
                    parse_path = imp
                for append_me in _get_files_to_process(parse_path):
                    ret_val.append(append_me)

    return ret_val


@attrs
class ParserError(Exception):
    """An error that represents a file that could not be parsed."""

    source: str = attrib(validator=validators.instance_of(str))
    errors: list[str] = attrib(default=Factory(list), validator=validators.instance_of(list))
