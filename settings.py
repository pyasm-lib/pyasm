"""
pyasm.settings
--------------
This module contains several functions which are used to define parameters
for the compilation.
"""

def set_bits(bits: int, program) -> None:
    """
    This function is used to indicate to the assembler in which mode the
    program must be compiled.

    Parameters:
    bits (int): the three possible values are 16, 32 or 64. 16 = real mode
    (16 bits), 32 = protected mode (32 bits) and 64 = long mode (64 bits).
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if bits in [16, 32, 64]:
        converted_bits = str(bits)
        program.asm_codegen.append(f"[bits {converted_bits}]")
    else:
        raise ValueError(f"The three possible values are 16, 32 and 64")

def set_origin(origin: int, program) -> None:
    """
    This function is used to define the memory address where the program
    will be loaded.

    Parameters:
    origin (int): the memory address where the program will be loaded. This
    parameter must be a hexadecimal number.
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    converted_origin = str(hex(origin))
    if converted_origin.startswith("0x"):
        program.asm_codegen.append(f"[org {converted_origin}]")
    else:
        raise TypeError(f"The program origin must be a hexadecimal number, not '{converted_origin}'")

def change_mode(mode: str, program) -> None:
    """
    This function is used to setup the registers for switching modes.

    Parameters:
    mode (str): the new mode (real, protected, long)
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if mode == "real":
        program.asm_codegen.extend(["mov eax, cr0",
                                    "and eax, 0x7ffffffe",
                                    "mov cr0, eax"])
    elif mode == "protected":
        program.asm_codegen.extend(["mov eax, cr0",
                                    "or eax, 1",
                                    "mov cr0, eax"])
    elif mode == "long":
        program.asm_codegen.extend(["mov eax, cr4",
                                    "or eax, 0x20",
                                    "mov cr4, eax",
                                    "mov ecx, 0xC0000080",
                                    "rdmsr",
                                    "or eax, 0x100",
                                    "wrmsr",
                                    "mov eax, cr3",
                                    "mov cr3, eax",
                                    "mov eax, cr0",
                                    "or eax, 0x80000001",
                                    "mov cr0, eax"])
    else:
        raise ValueError(f"Cannot switch to '{mode}' mode. This mode does not exist.")