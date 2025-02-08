"""
pyasm.labels
----------
This module contains functions used to manage labels in the program.
"""

def new_label(name: str, program) -> None:
    """
    This function creates a new label with the name :param name:.

    Parameters:
    name (str): the name of the label ()
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if name in program.labels:
        raise NameError(f"Cannot redefine label '{name}'")
    program.labels.append(f"{name}")
    program.asm_codegen.append(f"{name}:")

def goto_label(label: str, program) -> None:
    """
    This function makes a short jump to a label.

    Parameters:
    label (str): the name of the label to go to
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if label not in program.labels:
        raise NameError(f"Jump to undefined label '{label}'")
    program.asm_codegen.append(f"jmp {label}")

def long_jump(segment: (int, str), offset: (int, str), program) -> None:
    """
    This function makes an absolute long jump to a label.

    Parameters:
    segment (int, str): the segment
    offset (int, str): the offset
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if isinstance(segment, str):
        if segment not in program.registers:
            raise NameError(f"Unknow segment '{segment}'")
    if isinstance(offset, str):
        if offset not in program.registers:
            raise NameError(f"Unknow register '{offset}'")

    converted_segment = str(segment)
    converted_offset = str(offset)

    program.asm_codegen.append(f"jmp dword {converted_segment}:{converted_offset}")

def subroutine_return(program) -> None:
    """
    This function returns from a subroutine.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("ret")

def interrupt_return(program) -> None:
    """
    This function returns from an interrupt.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("iret")

def call(label: str, program) -> None:
    """
    This function calls a given subroutine.

    Parameters:
    label (str): name of subroutine
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"call {label}")