"""
pyasm.bios.memory
-----------------
This module provides functions to use BIOS interrupts related to vectors.
"""

def set_disk_vector(vector_address: int, program) -> None:
    """
    This function sets the Disk interrupt vector.

    Parameters:
    vector_address (int): The address of the interrupt vector.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                f"mov dx, {vector_address}",
                                "int 0x1E"])

def set_timer_vector(vector_address: int, program) -> None:
    """
    This function sets the Timer interrupt vector.

    Parameters:
    vector_address (int): The address of the interrupt vector.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                f"mov dx, {vector_address}",
                                "int 0x1C"])

def set_break_vector(vector_address: int, program) -> None:
    """
    This function sets the Break interrupt vector.

    Parameters:
    vector_address (int): The address of the interrupt vector.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                f"mov dx, {vector_address}",
                                "int 0x1B"])

"""
pyasm.bios.floppy
-----------------
This module provides functions to use BIOS interrupts related to the Floppy Disk vector.
"""

def set_floppy_vector(vector_address: int, program) -> None:
    """
    This function sets the Floppy Disk interrupt vector.

    Parameters:
    vector_address (int): The address of the interrupt vector.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                f"mov dx, {vector_address}",
                                "int 0x1F"])