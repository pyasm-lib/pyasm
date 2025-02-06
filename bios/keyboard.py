"""
pyasm.bios.keyboard
-------------------
This module provides functions to use BIOS interrupts related to keyboard.
"""

def read_key(program) -> None:
    """
    This function reads a key from the keyboard. The ASCII code is in AL,
    and the scan code is in AH.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                "int 0x16"])

def check_status(program) -> None:
    """
    This function checks the keyboard status. ZF set if no key is pressed,
    ZF clear if a key is pressed. If a key is pressed, the ASCII code is in
    AL and the scan code is in AH.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x01",
                                "int 0x16"])

def get_shift_status(program) -> None:
    """
    This function gets the shift status, which is in AL.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x02",
                                "int 0x16"])

def read_extended_key(program) -> None:
    """
    This function reads a key from the extended keyboard. The ASCII code is
    in AL, and the scan code is in AH.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x10",
                                "int 0x16"])

def check_extended_status(program) -> None:
    """
    This function checks the extended keyboard status. ZF set if no key is
    pressed, ZF clear if a key is pressed. If a key is pressed, the ASCII
    code is in AL and the scan code is in AH.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x11",
                                "int 0x16"])