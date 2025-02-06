"""
pyasm.stream
------------
This module provides functions you can use to control the execution stream
of the program.
"""

def hang(program) -> None:
    """
    This function jumps continuously at the same memory address to stop
    the program.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("jmp $")