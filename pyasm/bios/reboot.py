"""
pyasm.bios.reboot
-----------------
This module provides functions to use BIOS interrupts related to system
rebooting.
"""

def reboot(program) -> None:
    """
    This function reboots the system.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                "int 0x19"])