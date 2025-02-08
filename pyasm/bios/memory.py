"""
pyasm.bios.memory
-----------------
This module provides functions to use BIOS interrupts related to memory.
"""

def read_memory_size(program) -> None:
    """
    This function reads the size of the conventionnal memory in kilobytes
    and store it in AX.S

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("int 0x12")