"""
pyasm.stream
------------
This module provides functions you can use to control the execution stream
of the program.
"""

def hang(program) -> None:
    """
    This function jumps continuously at the same memory address to stop
    the program.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("jmp $")

def jump_if(register1: str, register2: str, operator: str, label: str, program) -> None:
    """
    This function jumps to a label if a certain condition is true. This
    condition is verified by the :param operator: operator.

    Parameters:
    register1: the first register
    register2: the second register
    operator: the comparison operator (=, !=, <, >, <=, >=, -<, ->, -<=,
    ->=, c, !c)
    label: the name of the label which will be created if the condition is
    true
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if operator == "=":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"je {label}"])
    elif operator == "!=":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"jne {label}"])
    elif operator == "<":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"jl {label}"])
    elif operator == ">":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"jg {label}"])
    elif operator == "<=":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"jle {label}"])
    elif operator == ">=":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"jge {label}"])
    elif operator == "-<":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"jb {label}"])
    elif operator == "->":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"ja {label}"])
    elif operator == "-<=":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"jbe {label}"])
    elif operator == "->=":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"jae {label}"])
    elif operator == "c":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"jc {label}"])
    elif operator == "!c":
        program.asm_codegen.extend([f"cmp {register1}, {register2}",
                                    f"jnc {label}"])
    else:
        raise ValueError(f"Invalid operator '{operator}'")

def halt(program) -> None:
    """
    This functions stops the CPU.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("hlt")