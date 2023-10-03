# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

import unittest
from copy import deepcopy
from aac.lang.plugincommandreference import PluginCommandReference


class PluginCommandReferenceTestHelper:
    @staticmethod
    def generate_data() -> dict:
        return {
            "plugin": "test",
            "command": "test",
        }

    @staticmethod
    def generate_data_required_only() -> dict:
        return {
            "plugin": "test",
            "command": "test",
        }


class TestPluginCommandReference(unittest.TestCase):
    def test_plugincommandreference_from_dict_all_fields(self):
        plugincommandreference_dict = PluginCommandReferenceTestHelper.generate_data()
        instance = PluginCommandReference.from_dict(
            deepcopy(plugincommandreference_dict)
        )
        self.assertEqual(instance.plugin, plugincommandreference_dict["plugin"])
        self.assertEqual(instance.command, plugincommandreference_dict["command"])

        plugincommandreference_dict = (
            PluginCommandReferenceTestHelper.generate_data_required_only()
        )
        instance = PluginCommandReference.from_dict(
            deepcopy(plugincommandreference_dict)
        )
        self.assertEqual(instance.plugin, plugincommandreference_dict["plugin"])
        self.assertEqual(instance.command, plugincommandreference_dict["command"])


if __name__ == "__main__":
    unittest.main()
