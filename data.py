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

def load_byte(program) -> None:
    """
    This function loads a byte.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("lodsb")

def load_word(program) -> None:
    """
    This function loads a word.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("lodsw")

def load_double(program) -> None:
    """
    This function loads a double.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("lodsd")

def load_quadword(program) -> None:
    """
    This function loads a quadword.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("lodsq")

def store_byte(program) -> None:
    """
    This function stores a byte.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("stosb")

def store_word(program) -> None:
    """
    This function stores a word.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("stosw")

def store_double(program) -> None:
    """
    This function stores a double.

    Parameters:
    value: the value of the double
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("stosd")

def store_qaudword(program) -> None:
    """
    This function stores a quadword.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("stosq")