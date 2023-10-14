"""The AaC Exclusive fields plugin implementation module."""
# NOTE: It is safe to edit this file.
# This file is only initially generated by aac gen-plugin, and it won't be overwritten if the file already exists.

# There may be some unused imports depending on the definition of the plugin...but that's ok
from aac.execute.aac_execution_result import (
    ExecutionResult,
    ExecutionStatus,
    ExecutionMessage,
)
from aac.lang.schema import Schema
from aac.lang.plugininputvalue import PluginInputValue
from aac.context.language_context import LanguageContext
from aac.context.definition import Definition
from aac.io.files.aac_file import AaCFile
from aac.context.source_location import SourceLocation
from typing import Any


plugin_name = "Exclusive fields"


def mutually_exclusive_fields(
    instance: Any, definition: Definition, defining_schema: Schema, fields: list[str]
) -> ExecutionResult:
    """Business logic for the Mutually exclusive fields constraint."""

    num_present = 0
    for field in fields:
        instance_fields = vars(instance)
        if field in instance_fields:
            field_value = getattr(instance, field)
            if field_value is None:  # handle primitives and schema defined types
                continue
            elif isinstance(field_value, list) and len(field_value) == 0:  # handle lists
                continue
            elif isinstance(field_value, dict) and len(field_value) == 0:  # this is for the any type
                continue
            else:
                num_present += 1  # we found a real instance, so count it


    if num_present == 0:
        error_msg = ExecutionMessage(
            f"None of the following fields were present: {fields}",
            definition.source,
            None,
        )
        return ExecutionResult(plugin_name, "Mutually exclusive fields", ExecutionStatus.GENERAL_FAILURE, [error_msg])

    if num_present > 1:
        error_msg = ExecutionMessage(
            f"More than one of the following fields were present: {fields}",
            definition.source,
            None,
        )
        return ExecutionResult(plugin_name, "Mutually exclusive fields", ExecutionStatus.GENERAL_FAILURE, [error_msg])
            

    return ExecutionResult(plugin_name, "Mutually exclusive fields", ExecutionStatus.SUCCESS, [])
