"""__init__.py module for the Print AaC Definitions plugin."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from os.path import join, dirname
from aac.execute.aac_execution_result import (
    ExecutionResult,
    ExecutionStatus,
)
from aac.execute import hookimpl
from aac.context.language_context import LanguageContext
from aac.execute.plugin_runner import PluginRunner
from aac.plugins.print_defs.print_aac_definitions_impl import plugin_name, print_defs

print_aac_definitions_aac_file_name = "print_aac_definitions.aac"


def run_print_defs(core_only) -> ExecutionResult:
    """Print YAML representation of AaC language definitions."""

    result = ExecutionResult(plugin_name, "print-defs", ExecutionStatus.SUCCESS, [])

    print_defs_result = print_defs(core_only)
    if not print_defs_result.is_success():
        return print_defs_result
    else:
        result.add_messages(print_defs_result.messages)

    return result


@hookimpl
def register_plugin() -> None:
    """
    Returns information about the plugin.

    Returns:
        A collection of information about the plugin and what it contributes.
    """

    active_context = LanguageContext()
    print_aac_definitions_aac_file = join(
        dirname(__file__), print_aac_definitions_aac_file_name
    )
    definitions = active_context.parse_and_load(print_aac_definitions_aac_file)

    print_aac_definitions_plugin_definition = [
        definition for definition in definitions if definition.name == plugin_name
    ][0]

    plugin_instance = print_aac_definitions_plugin_definition.instance
    for file_to_load in plugin_instance.definition_sources:
        active_context.parse_and_load(file_to_load)

    plugin_runner = PluginRunner(
        plugin_definition=print_aac_definitions_plugin_definition
    )
    plugin_runner.add_command_callback("print-defs", run_print_defs)

    active_context.register_plugin_runner(plugin_runner)