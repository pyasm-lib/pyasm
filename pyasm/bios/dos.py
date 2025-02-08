"""
pyasm.bios.dos
--------------
This module provides functions to use DOS interrupts related to various DOS operations.
"""

def write_string(string: str, program) -> None:
    """
    This function writes a string to the standard output.

    Parameters:
    string (str): The string to write. The string must be terminated with a '$' character.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x09",
                                f"mov dx, {string}",
                                "int 0x21"])

def set_interrupt_vector(interrupt_number: int, vector_address: int, program) -> None:
    """
    This function sets the interrupt vector.

    Parameters:
    interrupt_number (int): The interrupt number.
    vector_address (int): The address of the interrupt vector.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x25",
                                f"mov al, {interrupt_number}",
                                f"mov dx, {vector_address}",
                                "int 0x21"])

def get_interrupt_vector(interrupt_number: int, program) -> None:
    """
    This function gets the address of the interrupt vector.

    Parameters:
    interrupt_number (int): The interrupt number.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x35",
                                f"mov al, {interrupt_number}",
                                "int 0x21"])

def terminate_with_retcode(return_code: int, program) -> None:
    """
    This function terminates the program with a return code.

    Parameters:
    return_code (int): The return code.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x4C",
                                f"mov al, {return_code}",
                                "int 0x21"])