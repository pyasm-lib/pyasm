"""
pyasm.utils
-----------
This module provides some utils to better manage the generated Assembly code.
"""

def fill_file(times: int, value: (int, str), program) -> None:
    """
    This function fills the binary file created by the assembler.

    Parameters:
    times (int): times to write in the file to fill it
    value (int, str): value to write in the file
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"times {times} - ($ - $$) db {value}")

def inline_asm(code: str, program) -> None:
    """
    This function allows the programer to use inline Assembly code.

    Parameters:
    code: the Assembly code
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.append(f"{code}")