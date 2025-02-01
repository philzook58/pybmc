# https://github.com/model-checking/kani/blob/main/cprover_bindings/src/goto_program/symbol.rs
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from .typ import Type
from .location import Location
from .expr import Expr

# InternedString is assumed to be just a string alias.
InternedString = str


@dataclass
class Parameter:
    """Represents the formal parameters of a function."""

    typ: "Type"
    identifier: Optional[InternedString] = None
    base_name: Optional[InternedString] = None


@dataclass
class Lambda:
    """Represents an anonymous function object for function contracts."""

    arguments: List[Parameter]
    body: Expr

    @classmethod
    def as_contract_for(
        cls, fn_ty: "Type", return_var_name: Optional[InternedString], body: Expr
    ) -> "Lambda":
        if fn_ty.kind != Type.Kind.CODE:
            raise ValueError(
                f"Contract lambdas can only be generated for `Code` types, received {fn_ty.kind}"
            )

        parameters = [
            Parameter(typ=fn_ty.return_type, identifier=None, base_name=return_var_name)
        ] + fn_ty.parameters

        return cls(arguments=parameters, body=body)


@dataclass
class FunctionContract:
    """Represents a CBMC function contract."""

    assigns: List[Lambda]

    @classmethod
    def new(cls, assigns: List[Lambda]) -> "FunctionContract":
        return cls(assigns=assigns)


class SymbolModes(Enum):
    """Modes supported by CBMC."""

    C = "C"
    RUST = "Rust"


class SymbolValues(Enum):
    """Possible values for a Symbol."""

    EXPR = "Expr"
    STMT = "Stmt"
    NONE = "None"


@dataclass
class Symbol:
    """Represents a symbol in CBMC."""

    name: str
    location: Location
    type: Type
    value: SymbolValues
    contract: Optional[FunctionContract] = None

    baseName: Optional[InternedString] = None
    prettyName: Optional[InternedString] = None
    prettyType: Optional[str] = None
    prettyValue: Optional[str] = None
    module: Optional[InternedString] = None
    mode: SymbolModes = SymbolModes.C

    isExported: bool = False
    isInput: bool = False
    isMacro: bool = False
    isOutput: bool = False
    isProperty: bool = False
    isStateVar: bool = False
    isType: bool = False
    isAuxiliary: bool = False
    isExtern: bool = False
    isFileLocal: bool = False
    isLvalue: bool = False
    isParameter: bool = False
    isStaticLifetime: bool = False
    isThreadLocal: bool = False
    isVolatile: bool = False
    isWeak: bool = False
    isStaticConst: bool = False
