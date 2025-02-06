"""
pyasm.program
-------------
This module provides a class named 'Program' to manage the generated
Assembly code.
"""

import os

class Program:
    """
    This class is used to manage the generation of the Assembly code.

    Parameters:
    program_name (str): the path of the Assembly file where the generated
    code will be written.
    """
    def __init__(self, program_name: str) -> None:
        self.asm_file_path = program_name
        self.asm_codegen = []
        self.registers = ["ah", "bh", "ch", "dh", "di", "si", "cs", "ds" "es",
        "fs", "gs", "ss", "bp", "sp", "ax", "bx", "cx", "dx", "al", "bl", "cl",
        "dl", 'eax', "ebx", "ecx", "edx", "esp", "ebp", "edi", "cr0", "cr2", "cr3",
        "cr4", "rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp", "r8", "r9",
        "r10", "r11", "r12", "r13", "r14", "r15"]
        self.labels = []

    def __repr__(self) -> str:
        return f"Program(asm_file_path={self.asm_file_path}, asm_codegen={self.asm_codegen}, bits={self.bits}, origin={self.origin})"

    def generate(self) -> None:
        """
        This function writes the generated Assembly code (which is contained
        by self.asm_codegen) into the file (the path is contained by self.
        asm_file_path).

        Return:
        None
        """
        with open(f"{self.asm_file_path}", 'w') as file:
            if self.asm_codegen is not None:
                for line in self.asm_codegen:
                    if line is not None:
                        file.write(f"{line}\n")

    def assemble(self, output_format: str, output_file: str):
        os.system(f"nasm -f {output_format} -o {output_file} {self.asm_file_path}")