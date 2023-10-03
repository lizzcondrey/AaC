"""Python module for the ProjectDependency class."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from dataclasses import dataclass
import attr
from typing import Optional
from attr import attrib, validators


@dataclass(frozen=True)
class ProjectDependency:
    """
    A pypi project dependency.

    name: str - The name of the pypi project to import.
    version: str - The version nof the pypi project to import.
    """

    name: str = attrib(init=attr.ib(), validator=validators.instance_of(str))
    version: str = attrib(init=attr.ib(), validator=validators.instance_of(str))

    @classmethod
    def from_dict(cls, data):
        args = {}

        return cls(**args, **data)
