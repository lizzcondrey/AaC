# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

import unittest
from copy import deepcopy
from aac.lang.requirementspecification import RequirementSpecification


class RequirementSpecificationTestHelper:
    @staticmethod
    def generate_data() -> dict:
        return {
            "name": "test",
            "description": "test",
            "sections": ["test"],
            "parent_specs": ["test"],
            "child_specs": ["test"],
            "requirements": ["test"],
        }

    @staticmethod
    def generate_data_required_only() -> dict:
        return {
            "name": "test",
        }


class TestRequirementSpecification(unittest.TestCase):
    def test_requirementspecification_from_dict_all_fields(self):
        requirementspecification_dict = (
            RequirementSpecificationTestHelper.generate_data()
        )
        instance = RequirementSpecification.from_dict(
            deepcopy(requirementspecification_dict)
        )
        self.assertEqual(instance.name, requirementspecification_dict["name"])
        self.assertEqual(
            instance.description, requirementspecification_dict["description"]
        )
        self.assertEqual(instance.sections, requirementspecification_dict["sections"])
        self.assertEqual(
            instance.parent_specs, requirementspecification_dict["parent_specs"]
        )
        self.assertEqual(
            instance.child_specs, requirementspecification_dict["child_specs"]
        )
        self.assertEqual(
            instance.requirements, requirementspecification_dict["requirements"]
        )

        requirementspecification_dict = (
            RequirementSpecificationTestHelper.generate_data_required_only()
        )
        instance = RequirementSpecification.from_dict(
            deepcopy(requirementspecification_dict)
        )
        self.assertEqual(instance.name, requirementspecification_dict["name"])


if __name__ == "__main__":
    unittest.main()
