"""
pyasm.builtin.stdio
--------------------
This module provides several functions related to Inputs/Outputs.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# --------------------------------------------------------------------------- #
import utils, labels, bios.video, data, stream, operations
import bios.keyboard

def def_print(program) -> None:
    """
    This function defines the BUILTIN_STDIO_print subroutine.
    Don't forget to use call_print() when you want to use it.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    labels.new_label("BUILTIN_STDIO_print", program)
    labels.new_label(".BUILTIN_STDIO_print_begin", program)
    data.load_byte(program)
    stream.jump_if("al", 0, "=", ".BUILTIN_STDIO_print_done", program)
    bios.video.teletype_write_cursor(None, 0x07, program)
    labels.goto_label(".BUILTIN_STDIO_print_begin", program)
    labels.new_label(".BUILTIN_STDIO_print_done", program)
    labels.subroutine_return(program)

def def_input(program) -> None:
    """
    This function defines the BUILTIN_STDIO_input subroutine.
    Don't forget to use call_input() when you want to use it.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    labels.new_label("BUILTIN_STDIO_input", program)
    operations.push("ax", program)
    operations.push("di", program)
    labels.new_label(".BUILTIN_STDIO_input_begin", program)
    bios.keyboard.read_key(program)
    stream.jump_if("al", 0x0d, "=", ".BUILTIN_STDIO_input_newline", program)
    stream.jump_if("al", 0x08, "=", ".BUILTIN_STDIO_input_backspace", program)
    data.store_byte(program)
    bios.video.teletype_write_cursor(None, 0x07, program)
    labels.goto_label(".BUILTIN_STDIO_input_begin", program)
    labels.new_label(".BUILTIN_STDIO_input_backspace", program)
    stream.jump_if("di", 0, "=", ".BUILTIN_STDIO_input_begin", program)
    operations.sub("di", 1, program)
    bios.video.teletype_write_cursor(0x08, 0x07, program)
    bios.video.teletype_write_cursor("' '", 0x07, program)
    bios.video.teletype_write_cursor(0x08, 0x07, program)
    labels.goto_label(".BUILTIN_STDIO_input_begin", program)
    labels.new_label(".BUILTIN_STDIO_input_newline", program)
    bios.video.teletype_write_cursor(0x0a, 0x07, program)
    bios.video.teletype_write_cursor(0x0d, 0x07, program)
    operations.move("al", 0, program)
    data.store_byte(program)
    operations.pop("di", program)
    operations.pop("ax", program)
    labels.subroutine_return(program)

def call_print(message: str, program) -> None:
    """
    This function calls the BUILTIN_STDIO_print function, after moving
    the message in SI. Note that the message must be terminated by a
    null-character (0).

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    operations.move("si", f"{message}", program)
    labels.call("BUILTIN_STDIO_print", program)

def call_input(buffer, program) -> None:
    """
    This function calls the BUILTIN_STDIO_input function, after moving
    the input buffer in DI.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    operations.move("di", f"{buffer}", program)
    labels.call("BUILTIN_STDIO_input", program)