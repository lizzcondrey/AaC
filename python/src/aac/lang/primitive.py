"""Python module for the Primitive class."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from dataclasses import dataclass
import attr
from typing import Optional
from attr import attrib, validators
from aac.lang.aactype import AacType


@dataclass(frozen=True)
class Primitive(AacType):
    """
    A definition that represents a primitive value for use in the model.

    python_type: Optional[str] - The type value to represend this primitive with while generating python code.
    """

    python_type: Optional[str] = attrib(
        init=attr.ib(), validator=validators.optional(validators.instance_of(str))
    )

    @classmethod
    def from_dict(cls, data):
        python_type = data.pop("python_type", None)

        return cls(python_type=python_type, **data)
