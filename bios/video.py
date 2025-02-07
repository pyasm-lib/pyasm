"""
pyasm.bios.video
----------------
This module provides functions to use BIOS interrupts related to video.
"""

def set_video_mode(program) -> None:
    """
    This function enables the video mode.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                "mov al, 0x03",
                                "int 0x10"])

def define_cursor(program) -> None:
    """
    This function defines the cursor in video mode.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x01",
                                "mov ch, 0x06",
                                "mov cl, 0x07",
                                "int 0x10"])

def set_cursor_position(row, column, program, page=0x00) -> None:
    """
    This function sets the cursor at a certain position.

    Parameters:
    row: the row number
    column: the column number
    page: the page number (default=0x00)
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x02",
                                f"mov bh, {page}",
                                f"mov dh, {row}",
                                f"mov dl, {column}",
                                "int 0x10"])

def get_cursor_position(page, program) -> None:
    """
    This function gets the cursor position. The column is stored in DL
    and the row is in DH.

    Parameters:
    page: page number (default=0x00)
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x03",
                                f"mov bh, {page}",
                                "int 0x10"])

def scrollup(lines, blank_lines_attr, top_row, left_col, bottom_row, right_col, program) -> None:
    """
    This function scrolls the active page up.

    Parameters:
    lines: number of line to scroll
    blank_lines_attr: attribute of blank lines
    top_row: the top row
    left_col: the left column
    bottom_row: the bottom row
    right_col: the right column
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x06",
                                f"mov al, {lines}",
                                f"mov bh, {blank_lines_attr}",
                                f"mov ch, {top_row}",
                                f"mov cl, {left_col}",
                                f"mov dh, {bottom_row}",
                                f"mov dl, {right_col}",
                                "int 0x10"])

def scrolldown(lines, blank_lines_attr, top_row, left_col, bottom_row, right_col, program) -> None:
    """
    This function scrolls the active page down.

    Parameters:
    lines: number of line to scroll
    blank_lines_attr: attribute of blank lines
    top_row: the top row
    left_col: the left column
    bottom_row: the bottom row
    right_col: the right column
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x07",
                                f"mov al, {lines}",
                                f"mov bh, {blank_lines_attr}",
                                f"mov ch, {top_row}",
                                f"mov cl, {left_col}",
                                f"mov dh, {bottom_row}",
                                f"mov dl, {right_col}",
                                "int 0x10"])

def read_cursor(program, page=0x00) -> None:
    """
    This function reads the character at the current cursor position.
    The character is stored in AL, and his attribute in AH.

    Parameters:
    page: the number of the page
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x08",
                                f"mov bh, {page}",
                                "int 0x10"])

def write_cursor(char, attribute, times, program, page=0x00) -> None:
    """
    This function writes a character with given attributes at the current
    cursor position.

    Parameters:
    char: the character to write
    attribute: the attribute of the character to write
    times: the number of times the character will be written
    page: the page number
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("mov ah, 0x09")
    if char is not None: program.asm_codegen.append(f"mov al, {char}")
    program.asm_codegen.extend([f"mov bh, {page}",
                                f"mov bl, {attribute}",
                                f"mov cx, {times}",
                                "int 0x10"])

def teletype_write_cursor(char, attribute, program, page=0x00) -> None:
    """
    This function writes a character with given attributes in TeleType
    mode.

    Parameters:
    char: the character to write
    attribute: the attribute of the character to write (not on every
    BIOSs)
    page: the page number
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("mov ah, 0x0e")
    if char is not None: program.asm_codegen.append(f"mov al, {char}")
    program.asm_codegen.extend([f"mov bh, {page}",
                                f"mov bl, {attribute}",
                                "int 0x10"])

def get_video_mode(program) -> None:
    """
    This function reads the current video mode. The video mode is in AL,
    the page number is in BH and the number of columns is in DL.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x0f",
                                "int 0x10"])