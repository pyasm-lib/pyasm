"""
pyasm.bios.terminate
--------------------
This module provides functions to use BIOS interrupts related to program
termination.
"""

def terminate_program(program) -> None:
    """
    This function terminates the program.

    Parameters:
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                "int 0x20"])

def quit_program(program) -> None:
    """
    This function quits the program.

    Parameters:
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                "int 0x27"])