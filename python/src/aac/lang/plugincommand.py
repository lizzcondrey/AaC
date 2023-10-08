"""Python module for the PluginCommand class."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from dataclasses import dataclass
import attr
from typing import Optional
from attr import attrib, validators
from aac.lang.plugincommandreference import PluginCommandReference
from aac.lang.plugincommandreference import PluginCommandReference
from aac.lang.plugininput import PluginInput


@dataclass(frozen=True)
class PluginCommand:
    """
    Autogenerated PluginCommand AaC schema

    name: str - The name of the command.  This will be used by the CLI to invke the command.
    help_text: Optional[str] - A description that will be displayed as help text when displaying command usage.
    run_before: list[PluginCommandReference]] - A listing of plugin commands to run before this command.
    run_after: list[PluginCommandReference]] - A listing of plugin commands to run before this command.
    input: list[PluginInput]] - The list of all the fields that are inputs to the component when the command is executed.
    """

    name: str = attrib(init=attr.ib(), validator=validators.instance_of(str))
    help_text: Optional[str] = attrib(
        init=attr.ib(), validator=validators.optional(validators.instance_of(str))
    )
    run_before: list[PluginCommandReference] = attrib(
        init=attr.ib(), validator=validators.instance_of(list[PluginCommandReference])
    )
    run_after: list[PluginCommandReference] = attrib(
        init=attr.ib(), validator=validators.instance_of(list[PluginCommandReference])
    )
    input: list[PluginInput] = attrib(
        init=attr.ib(), validator=validators.instance_of(list[PluginInput])
    )

    @classmethod
    def from_dict(cls, data):
        args = {}

        help_text = data.pop("help_text", None)
        args["help_text"] = help_text

        run_before_data = data.pop("run_before", [])
        run_before = [
            PluginCommandReference.from_dict(entry) for entry in run_before_data
        ]
        args["run_before"] = run_before

        run_after_data = data.pop("run_after", [])
        run_after = [
            PluginCommandReference.from_dict(entry) for entry in run_after_data
        ]
        args["run_after"] = run_after

        input_data = data.pop("input", [])
        input = [PluginInput.from_dict(entry) for entry in input_data]
        args["input"] = input

        return cls(**args, **data)
