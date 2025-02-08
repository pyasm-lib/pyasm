"""
pyasm.preprocessor
------------------
This module provides several functions which are used to setup and verify
things before the code generation.
"""

from contextlib import contextmanager
import os

def define(name: str, value, program) -> None:
    """
    This function defines a constant.

    Parameters:
    name (str): the constant name. You cannot redefine a constant, so
    check if you defined a constant with the same name before.
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if name in program.constants:
        raise NameError(f"Cannot redefine '{name}' constant")
    programs.constants[name] = value

@contextmanager
def ifdef(name: str, program) -> bool:
    """
    This function checks if a constant is defined.

    Parameters:
    name (str): the constant name
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    bool:
    - True if the constant is defined
    - False if the constant is not defined
    """
    if name in program.constants:
        return True
    return False

@contextmanager
def ifndef(name: str, program) -> bool:
    """
    This function checks if a constant is not defined.

    Parameters:
    name (str): the constant name
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    bool:
    - True if the constant is not defined
    - False if the constant is defined
    """
    if name not in program.constants:
        return True
    return False

def undef(name: str, program) -> None:
    """
    This function undefines a constant.

    Parameters:
    name (str): the constant name. You cannot undefine a constant which
    was not defined before.
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if name not in program.constants:
        raise NameError(f"Cannot undefine an undefined constant '{name}'")
    program.constants.pop(name)

def include(file: str, program) -> None:
    """
    This function includes an Assembly program. The code of the included
    file will be added to the main generated Assembly code.

    Parameters:
    file (str): the path of the Assembly file to include
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if os.path.exists(f"{file}"):
        with open(f"{file}", 'r') as included:
            asm_to_add = included.read()
            if asm_to_add is not None:
                for line in asm_to_add:
                    if line is not None:
                        program.asm_codegen.append(f"{line}")
    elif os.path.isidr(f"{file}"):
        raise IsADirectoryError(f"Cannot include '{file}'because it is a directory")
    else:
        raise FileNotFoundError(f"'{file}' not found")