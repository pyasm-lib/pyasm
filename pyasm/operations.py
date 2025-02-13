"""
pyasm.instructions
------------------
This module contains functions which allows the programer to make operations
on the registers.
"""

import re

def add(register1: str, register2: str, program) -> None:
    """
    This function adds the value of :param register2: to the value of
    :param register1:.

    Parameters:
    register1 (str): the register which contains the value to change
    register2 (str): the register which contains the value to add
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"add {register1}, {register2}")

def sub(register1: str, register2: str, program) -> None:
    """
    This function substracts the value of :param register2: to the value of
    :param register1:.

    Parameters:
    register1 (str): the register which contains the value to change
    register2 (str): the register which contains the value to substract
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"sub {register1}, {register2}")

def mul(register1: str, register2: str, program) -> None:
    """
    This function multiplies the value of :param register1: by the value of
    :param register2:.

    Parameters:
    register1 (str): the register which contains the value to multiply
    register2 (str): the register which contains the multiplier value
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"mul {register1}, {register2}")

def div(register1: str, register2: str, program) -> None:
    """
    This function divides the value of :param register1: by the value of
    :param register2:.

    Parameters:
    register1 (str): the register which contains the value to divide
    register2 (str): the register which contains the divider value
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"div {register1}, {register2}")

def move(register1: str, register2: str, program) -> None:
    """
    This function moves the value of :param register2: into :param register1:.

    Parameters:
    register1 (str): the destination
    register2 (str): the source
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"mov {register1}, {register2}")

def shift_left(register1: str, register2: str, program) -> None:
    """
    This functions shifts the value of :param register1: of :param register2: bits
    on the left.
    
    Example with :param register2: = 1
    10110101 -> 01101011

    Parameters:
    register1 (str): the register which will be shifted
    register2 (str): the number of bits to shift
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"shl {register1}, {register2}")

def shift_right(register1: str, register2: str, program) -> None:
    """
    This functions shifts the value of :param register1: of :param register2: bits
    on the right.
    
    Example with :param register2: = 1
    10110101 -> 11011010

    Parameters:
    register1 (str): the register which will be shifted
    register2 (str): the number of bits to shift
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"shr {register1}, {register2}")

def push(register: str, program) -> None:
    """
    This function pushes a register on the top of the stack.

    Parameters:
    register (str): the register to push
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"push {register}")

def pop(register: str, program) -> None:
    """
    This function removes the register on the top of the stack.

    Parameters:
    register (str): the register to pop
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"pop {register}")

def push_all(program) -> None:
    """
    This function pushes all the registers on the top of the stack.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("pusha")

def pop_all(program) -> None:
    """
    This function removes all the registers from the top of the stack.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append("popa")

def bool_and(register1: str, register2: str, program) -> None:
    """
    AND TABLE:
    1 - 1 -> 1
    1 - 0 -> 0
    0 - 0 -> 0

    Parameters:
    register1 (str): the register which contains the first value
    register2 (str): the register which contains the second value
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"and {register1}, {register2}")

def bool_or(register1: str, register2: str, program) -> None:
    """
    OR TABLE:
    1 - 1 -> 1
    1 - 0 -> 1
    0 - 0 -> 0

    Parameters:
    register1 (str): the register which contains the first value
    register2 (str): the register which contains the second value
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"or {register1}, {register2}")

def bool_xor(register1: str, register2: str, program) -> None:
    """
    XOR TABLE:
    1 - 1 -> 0
    1 - 0 -> 1
    0 - 0 -> 0

    Parameters:
    register1 (str): the register which contains the first value
    register2 (str): the register which contains the second value
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"xor {register1}, {register2}")

def bool_not(register: str, program) -> None:
    """
    NOT TABLE:
    1 -> 0
    0 -> 1

    Parameters:
    register (str): the register which contains the bit to invert
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"not {register}")