# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

import unittest
from copy import deepcopy
from aac.lang.plugincommand import PluginCommand
from aac.lang.plugincommandreference import PluginCommandReference
from aac.lang.plugincommandreference import PluginCommandReference
from aac.lang.plugininput import PluginInput
from plugincommandreference_test import PluginCommandReferenceTestHelper
from plugincommandreference_test import PluginCommandReferenceTestHelper
from plugininput_test import PluginInputTestHelper


class PluginCommandTestHelper:
    @staticmethod
    def generate_data() -> dict:
        return {
            "name": "test",
            "help_text": "test",
            "run_before": [PluginCommandReferenceTestHelper.generate_data()],
            "run_after": [PluginCommandReferenceTestHelper.generate_data()],
            "input": [PluginInputTestHelper.generate_data()],
        }

    @staticmethod
    def generate_data_required_only() -> dict:
        return {
            "name": "test",
            "input": [PluginInputTestHelper.generate_data_required_only()],
        }


class TestPluginCommand(unittest.TestCase):
    def test_plugincommand_from_dict_all_fields(self):
        plugincommand_dict = PluginCommandTestHelper.generate_data()
        instance = PluginCommand.from_dict(deepcopy(plugincommand_dict))
        self.assertEqual(instance.name, plugincommand_dict["name"])
        self.assertEqual(instance.help_text, plugincommand_dict["help_text"])
        self.assertIsNotNone(instance.run_before)
        self.assertIsNotNone(instance.run_after)
        self.assertIsNotNone(instance.input)

        plugincommand_dict = PluginCommandTestHelper.generate_data_required_only()
        instance = PluginCommand.from_dict(deepcopy(plugincommand_dict))
        self.assertEqual(instance.name, plugincommand_dict["name"])
        self.assertIsNotNone(instance.input)


if __name__ == "__main__":
    unittest.main()
