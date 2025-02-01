from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Union

# InternedString is not defined in the provided Rust code, so assuming it's just a string alias
InternedString = str


class CIntType(Enum):
    BOOL = "Bool"
    CHAR = "Char"
    INT = "Int"
    LONG_INT = "LongInt"
    SIZE_T = "SizeT"
    SSIZE_T = "SSizeT"


@dataclass
class DatatypeComponent:
    """Represents a field or padding in a struct/union."""

    name: InternedString
    typ: Optional["Type"] = None  # Only for fields
    bits: Optional[int] = None  # Only for padding


@dataclass
class Parameter:
    """Represents the formal parameters of a function."""

    typ: "Type"
    identifier: Optional[InternedString] = None
    base_name: Optional[InternedString] = None


@dataclass
class Type:
    """Represents different types used in a goto-program."""

    class Kind(Enum):
        ARRAY = "Array"
        BOOL = "Bool"
        CBITFIELD = "CBitField"
        CINTEGER = "CInteger"
        CODE = "Code"
        CONSTRUCTOR = "Constructor"
        DOUBLE = "Double"
        EMPTY = "Empty"
        FLEXIBLE_ARRAY = "FlexibleArray"
        FLOAT = "Float"
        FLOAT16 = "Float16"
        FLOAT128 = "Float128"
        INCOMPLETE_STRUCT = "IncompleteStruct"
        INCOMPLETE_UNION = "IncompleteUnion"
        INTEGER = "Integer"
        INFINITE_ARRAY = "InfiniteArray"
        POINTER = "Pointer"
        SIGNEDBV = "Signedbv"
        STRUCT = "Struct"
        STRUCT_TAG = "StructTag"
        TYPEDEF = "TypeDef"
        UNION = "Union"
        UNION_TAG = "UnionTag"
        UNSIGNEDBV = "Unsignedbv"
        VARIADIC_CODE = "VariadicCode"
        VECTOR = "Vector"

    kind: Kind
    typ: Optional["Type"] = None  # Used for wrapped types like arrays, pointers
    size: Optional[int] = None  # Used for arrays, vectors
    width: Optional[int] = None  # Used for bitfields, signedbv, unsignedbv
    c_int_type: Optional[CIntType] = None  # Used for CInteger
    parameters: Optional[List[Parameter]] = None  # Used for Code
    return_type: Optional["Type"] = None  # Used for Code
    tag: Optional[InternedString] = None  # Used for structs/unions
    components: Optional[List[DatatypeComponent]] = None  # Used for Struct/Union


# Example usage:
example_type = Type(kind=Type.Kind.ARRAY, typ=Type(kind=Type.Kind.BOOL), size=3)

print(example_type)
