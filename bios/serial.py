"""
pyasm.bios.serial
-----------------
This module provides functions to use BIOS interrupts related to sreial ports..
"""

def init_serial_port(program, bps: int=0x03, com: int=0x00) -> None:
    """
    This function initialize the serial port.

    Parameters:
    bps (int): (default=0x03 (9600 bps, 8-N-1))
    com (int): the COM number (default=0x00 (COM1))
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                f"mov al, {bps}",
                                f"mov dx, {com}",
                                "int 0x14"])

def send_char(char: str, program, com: int=0x00) -> None:
    """
    This function sends a character to a COM.

    Parameters:
    char (str): the character to send
    com (int): the COM number (default=0x00 (COM1))
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x01",
                                f"mov al, '{char}'",
                                f"mov dx, {com}",
                                "int 0x14"])

def receive_char(program, com: int=0x00) -> None:
    """
    This function receive a character from a COM.

    Parameters:
    com (int): the COM number (default=0x00 (COM1))
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x02",
                                f"mov dx, {com}",
                                "int 0x14"])

def get_serial_port_status(program, com: int=0x00) -> None:
    """
    This function gets the serial port status.

    Parameters:
    com (int): the COM number (default=0x00 (COM1))
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x03",
                                f"mov dx, {com}",
                                "int 0x14"])