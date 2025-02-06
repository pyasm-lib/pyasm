"""
pyasm.data
----------
This module contains functions to manage data like bytes, words, doubles
or longs.
"""

def define_byte(value, program) -> None:
    """
    This function defines a byte.

    Parameters:
    value: the value of the byte
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"db {value}")

def define_word(value, program) -> None:
    """
    This function defines a word.

    Parameters:
    value: the value of the word
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"dw {value}")

def define_double(value, program) -> None:
    """
    This function defines a double.

    Parameters:
    value: the value of the double
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"dd {value}")

def define_long(value, program) -> None:
    """
    This function defines a long.

    Parameters:
    value: the value of the long
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"dl {value}")

def define_quadword(value, program) -> None:
    """
    This function defines a quadword.

    Parameters:
    value: the value of the quadword
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"dq {value}")