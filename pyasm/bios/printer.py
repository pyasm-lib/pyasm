"""
pyasm.bios.printer
------------------
This module provides functions to use BIOS interrupts related to the printer.
"""

def init_printer(program, printer=0x00) -> None:
    """
    This function initializes the printer.

    Parameters:
    printer: printer number (default=0x00 (LPT1))
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                f"mov dx, {printer}",
                                "int 0x17"])

def send_char(char: str, program, printer=0x00) -> None:
    """
    This function sends a character to the printer and store the printer
    status in AH.

    Parameters:
    char (str): the character to send
    printer: printer number (default=0x00 (LPT1))
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x01",
                                f"mov al, '{char}'",
                                f"mov dx, {printer}",
                                "int 0x17"])

def get_printer_status(program, printer=0x00) -> None:
    """
    This function gets the printer status and store it in AH.

    Parameters:
    printer: printer number (default=0x00 (LPT1))
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x02",
                                f"mov dx, {printer}",
                                "int 0x17"])