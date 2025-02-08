"""
pyasm.bios.equipment
--------------------
This module provides functions to use BIOS interrupts related to equipment.
"""

def read_equipment_word(program) -> None:
    """
    This function reads the equipment word and store it in AX.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                "int 0x11"])