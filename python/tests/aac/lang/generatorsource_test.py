# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

import unittest
from copy import deepcopy
from aac.lang.generatorsource import GeneratorSource
from aac.lang.generatortemplate import GeneratorTemplate
from generatortemplate_test import GeneratorTemplateTestHelper


class GeneratorSourceTestHelper:
    @staticmethod
    def generate_data() -> dict:
        return {
            "name": "test",
            "data_source": "test",
            "templates": [GeneratorTemplateTestHelper.generate_data()],
        }

    @staticmethod
    def generate_data_required_only() -> dict:
        return {
            "name": "test",
            "data_source": "test",
            "templates": [GeneratorTemplateTestHelper.generate_data_required_only()],
        }


class TestGeneratorSource(unittest.TestCase):
    def test_generatorsource_from_dict_all_fields(self):
        generatorsource_dict = GeneratorSourceTestHelper.generate_data()
        instance = GeneratorSource.from_dict(deepcopy(generatorsource_dict))
        self.assertEqual(instance.name, generatorsource_dict["name"])
        self.assertEqual(instance.data_source, generatorsource_dict["data_source"])
        self.assertIsNotNone(instance.templates)

        generatorsource_dict = GeneratorSourceTestHelper.generate_data_required_only()
        instance = GeneratorSource.from_dict(deepcopy(generatorsource_dict))
        self.assertEqual(instance.name, generatorsource_dict["name"])
        self.assertEqual(instance.data_source, generatorsource_dict["data_source"])
        self.assertIsNotNone(instance.templates)


if __name__ == "__main__":
    unittest.main()
