"""
pyasm.bios.mouse
---------------
This module provides functions to use BIOS interrupts related to mouse
operations.
"""

def detect_mouse(program) -> None:
    """
    This function detects the mouse.

    Parameters:
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                "int 0x33"])

def show_cursor(program) -> None:
    """
    This function displays the mouse cursor.

    Parameters:
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x01",
                                "int 0x33"])

def hide_cursor(program) -> None:
    """
    This function hides the mouse cursor.

    Parameters:
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x02",
                                "int 0x33"])

def get_cursor_position(program) -> None:
    """
    This function reads the cursor position.

    Parameters:
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x03",
                                "int 0x33"])

def set_cursor_position(x: int, y: int, program) -> None:
    """
    This function sets the cursor position.

    Parameters:
    x (int): The x-coordinate of the cursor position.
    y (int): The y-coordinate of the cursor position.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x04",
                                f"mov cx, {x}",
                                f"mov dx, {y}",
                                "int 0x33"])

def get_button_status(program) -> None:
    """
    This function reads the state of the mouse buttons.

    Parameters:
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x05",
                                "int 0x33"])

def set_cursor_shape(cursor_start: int, cursor_end: int, program) -> None:
    """
    This function sets the shape of the mouse cursor.

    Parameters:
    cursor_start (int): The start scan line of the cursor.
    cursor_end (int): The end scan line of the cursor.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x0A",
                                f"mov cx, {cursor_start}",
                                f"mov dx, {cursor_end}",
                                "int 0x33"])