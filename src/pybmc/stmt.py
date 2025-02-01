# https://github.com/model-checking/kani/blob/main/cprover_bindings/src/goto_program/location.rs
from dataclasses import dataclass
from typing import List, Optional
from .expr import Expr
from .location import Location

# Assuming `InternedString` is just a string alias
InternedString = str


@dataclass
class Stmt:
    """Base class for all statements."""

    # location: Optional[Location] = None


@dataclass
class Assign(Stmt):
    """`lhs = rhs;`"""

    lhs: Expr
    rhs: Expr


@dataclass
class Assert(Stmt):
    """`assert(cond)`"""

    cond: Expr
    property_class: InternedString
    msg: InternedString


@dataclass
class Assume(Stmt):
    """`__CPROVER_assume(cond);`"""

    cond: Expr


@dataclass
class AtomicBlock(Stmt):
    """`{ ATOMIC_BEGIN stmt1; stmt2; ... ATOMIC_END }`"""

    stmts: List[Stmt]


@dataclass
class Block(Stmt):
    """`{ stmt1; stmt2; ... }`"""

    stmts: List[Stmt]


@dataclass
class Break(Stmt):
    """`break;`"""

    pass


@dataclass
class Continue(Stmt):
    """`continue;`"""

    pass


@dataclass
class Dead(Stmt):
    """End-of-life of a local variable"""

    expr: Expr


@dataclass
class Decl(Stmt):
    """`lhs.typ lhs = value;` or `lhs.typ lhs;`"""

    lhs: Expr  # SymbolExpr
    value: Optional[Expr] = None


@dataclass
class Deinit(Stmt):
    """Marks the target place as uninitialized."""

    expr: Expr


@dataclass
class ExpressionStmt(Stmt):
    """`e;`"""

    expr: Expr


@dataclass
class ForLoop(Stmt):
    """`for (init; cond; update) { body }`"""

    init: Stmt
    cond: Expr
    update: Stmt
    body: Stmt


@dataclass
class FunctionCall(Stmt):
    """`lhs = function(arguments);` or `function(arguments);`"""

    lhs: Optional[Expr]
    function: Expr
    arguments: List[Expr]


@dataclass
class Goto(Stmt):
    """`goto dest;`"""

    dest: InternedString
    loop_invariants: Optional[Expr] = None


@dataclass
class IfThenElse(Stmt):
    """`if (i) { t } else { e }`"""

    cond: Expr
    then_branch: Stmt
    else_branch: Optional[Stmt] = None


@dataclass
class Label(Stmt):
    """`label: body;`"""

    label: InternedString
    body: Stmt


@dataclass
class Return(Stmt):
    """`return e;` or `return;`"""

    expr: Optional[Expr] = None


@dataclass
class Skip(Stmt):
    """`;`"""

    pass


@dataclass
class SwitchCase:
    """Represents a case in a switch statement."""

    case: Expr
    body: Stmt


@dataclass
class Switch(Stmt):
    """`switch (control) { case1; case2; ... }`"""

    control: Expr
    cases: List[SwitchCase]
    default: Optional[Stmt] = None


@dataclass
class WhileLoop(Stmt):
    """`while (cond) { body }`"""

    cond: Expr
    body: Stmt
