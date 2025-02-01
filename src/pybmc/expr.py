# https://github.com/model-checking/kani/blob/main/cprover_bindings/src/goto_program/expr.rs
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Union
from .typ import Type
from .location import Location
from .machine_model import MachineModel
# Assuming `InternedString` is just a string alias
InternedString = str


class BinaryOperator(Enum):
    """Represents binary operators in CBMC."""

    AND = "And"
    ASHR = "Ashr"
    BITAND = "Bitand"
    BITOR = "Bitor"
    BITNAND = "Bitnand"
    BITXOR = "Bitxor"
    DIV = "Div"
    EQUAL = "Equal"
    GE = "Ge"
    GT = "Gt"
    IEEE_FLOAT_EQUAL = "IeeeFloatEqual"
    IEEE_FLOAT_NOTEQUAL = "IeeeFloatNotequal"
    IMPLIES = "Implies"
    LE = "Le"
    LSHR = "Lshr"
    LT = "Lt"
    MINUS = "Minus"
    MOD = "Mod"
    MULT = "Mult"
    NOTEQUAL = "Notequal"
    OR = "Or"
    OVERFLOW_MINUS = "OverflowMinus"
    OVERFLOW_MULT = "OverflowMult"
    OVERFLOW_PLUS = "OverflowPlus"
    OVERFLOW_RESULT_MINUS = "OverflowResultMinus"
    OVERFLOW_RESULT_MULT = "OverflowResultMult"
    OVERFLOW_RESULT_PLUS = "OverflowResultPlus"
    PLUS = "Plus"
    ROK = "ROk"
    ROL = "Rol"
    ROR = "Ror"
    SHL = "Shl"
    VECTOR_EQUAL = "VectorEqual"
    VECTOR_NOTEQUAL = "VectorNotequal"
    VECTOR_GE = "VectorGe"
    VECTOR_GT = "VectorGt"
    VECTOR_LE = "VectorLe"
    VECTOR_LT = "VectorLt"
    XOR = "Xor"

    def to_irep_id(self) -> str:
        """Converts the operator to its corresponding irep ID."""
        return self.value


class SelfOperator(Enum):
    """Represents unary operators with side effects."""

    POSTDECREMENT = "Postdecrement"
    POSTINCREMENT = "Postincrement"
    PREDECREMENT = "Predecrement"
    PREINCREMENT = "Preincrement"

    def to_irep_id(self) -> str:
        """Converts the operator to its corresponding irep ID."""
        return self.value


class UnaryOperator(Enum):
    """Represents unary operators."""

    BITNOT = "Bitnot"
    BIT_REVERSE = "BitReverse"
    BSWAP = "Bswap"
    IS_DYNAMIC_OBJECT = "IsDynamicObject"
    IS_FINITE = "IsFinite"
    NOT = "Not"
    OBJECT_SIZE = "ObjectSize"
    POINTER_OBJECT = "PointerObject"
    POINTER_OFFSET = "PointerOffset"
    POPCOUNT = "Popcount"
    COUNT_TRAILING_ZEROS = "CountTrailingZeros"
    COUNT_LEADING_ZEROS = "CountLeadingZeros"
    UNARY_MINUS = "UnaryMinus"

    def to_irep_id(self) -> str:
        """Converts the operator to its corresponding irep ID."""
        return self.value


@dataclass
class Expr:
    """Represents an expression in CBMC."""

    value: "ExprValue"
    typ: Type
    location: Optional[Location] = None
    size_of_annotation: Optional[Type] = None


@dataclass
class ArithmeticOverflowResult:
    """The return type for `__CPROVER_overflow_op` operations."""

    result: Expr  # The computed result if no overflow occurred
    overflowed: Expr  # Boolean flag indicating whether overflow occurred


# Constants for struct field names
ARITH_OVERFLOW_RESULT_FIELD = "result"
ARITH_OVERFLOW_OVERFLOWED_FIELD = "overflowed"


def arithmetic_overflow_result_type(operand_type: Type) -> Type:
    """Creates a struct type representing an arithmetic overflow result."""
    name = f"overflow_result_{operand_type.kind}"
    return Type(kind=name)  # Simplified, assumes Type can represent a struct


@dataclass
class AddressOf:
    e: Expr


@dataclass
class Array:
    elems: List[Expr]


@dataclass
class ArrayOf:
    elem: Expr


@dataclass
class Assign:
    left: Expr
    right: Expr


@dataclass
class BinOp:
    op: BinaryOperator
    lhs: Expr
    rhs: Expr


@dataclass
class BoolConstant:
    c: bool


@dataclass
class ByteExtract:
    e: Expr
    offset: int


@dataclass
class Dereference:
    e: Expr


@dataclass
class DoubleConstant:
    value: float


@dataclass
class FloatConstant:
    value: float


@dataclass
class FunctionCall:
    function: Expr
    arguments: List[Expr]


@dataclass
class IfThenElse:
    c: Expr
    t: Expr
    e: Expr


@dataclass
class Index:
    array: Expr
    index: Expr


@dataclass
class Member:
    lhs: Expr
    field: InternedString


@dataclass
class PointerConstant:
    value: int


@dataclass
class ReadOk:
    ptr: Expr
    size: Expr


@dataclass
class UnOp:
    op: UnaryOperator
    e: Expr


@dataclass
class Vector:
    elems: List[Expr]


ExprValue = Union[
    AddressOf,
    Array,
    ArrayOf,
    Assign,
    BinOp,
    BoolConstant,
    ByteExtract,
    Dereference,
    DoubleConstant,
    FloatConstant,
    FunctionCall,
    IfThenElse,
    Index,
    Member,
    PointerConstant,
    ReadOk,
    UnOp,
    Vector,
]


def to_irep(e : ExprValue, mm : MachineModel) -> Irep:
    match e:
        case AddressOf(e):
