"""Python module for the RequirementAttribute class."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from dataclasses import dataclass
import attr
from typing import Optional
from attr import attrib, validators


@dataclass(frozen=True)
class RequirementAttribute:
    """
    User definable attributes that can be associataed with a requirement. A common example may be explanation or interpretation to provice additional context to help reduce ambiguity.

    name: str - The name of the attribute.
    value: str - The value of the attribute.
    """

    name: str = attrib(init=attr.ib(), validator=validators.instance_of(str))
    value: str = attrib(init=attr.ib(), validator=validators.instance_of(str))

    @classmethod
    def from_dict(cls, data):
        args = {}

        return cls(**args, **data)
