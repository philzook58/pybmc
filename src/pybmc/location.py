# https://github.com/model-checking/kani/blob/main/cprover_bindings/src/goto_program/location.rs

from dataclasses import dataclass
from typing import List, Optional

# Assuming `InternedString` is just a string alias
InternedString = str


class Location:
    """Base class for all location types."""


@dataclass
class NoneLocation(Location):
    """Unknown source location."""

    pass


@dataclass
class BuiltinFunction(Location):
    """Code is in a builtin function."""

    function_name: InternedString
    line: Optional[int] = None


@dataclass
class Loc(Location):
    """Location in user code."""

    file: InternedString
    function: Optional[InternedString]
    start_line: int
    start_col: Optional[int]
    end_line: int
    end_col: Optional[int]
    pragmas: List[str] = None  # Static list of pragmas

    def __post_init__(self):
        if self.pragmas is None:
            self.pragmas = []


@dataclass
class Property(Location):
    """Location for Statements that use Property Class and Description (Assert, Assume, Cover)."""

    file: InternedString
    function: Optional[InternedString]
    line: int
    col: Optional[int]
    comment: InternedString
    property_class: InternedString
    pragmas: List[str] = None  # Static list of pragmas

    def __post_init__(self):
        if self.pragmas is None:
            self.pragmas = []


@dataclass
class PropertyUnknownLocation(Location):
    """Covers cases where Location Details are unknown or set as None but Property Class is needed."""

    comment: InternedString
    property_class: InternedString
