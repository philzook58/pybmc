from dataclasses import dataclass
from enum import Enum


class RoundingMode(Enum):
    TO_NEAREST = 0
    DOWNWARD = 1
    UPWARD = 2
    TOWARDS_ZERO = 3


@dataclass
class MachineModel:
    alignment: int
    architecture: str
    bool_width: int
    char_is_unsigned: bool
    char_width: int
    double_width: int
    float_width: int
    int_width: int
    is_big_endian: bool
    long_double_width: int
    long_int_width: int
    long_long_int_width: int
    memory_operand_size: int
    null_is_zero: bool
    pointer_width: int
    rounding_mode: RoundingMode
    short_int_width: int
    single_width: int
    wchar_t_is_unsigned: bool
    wchar_t_width: int
    word_size: int

    def pointer_width_in_bytes(self) -> int:
        return self.pointer_width // 8
