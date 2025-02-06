"""
pyasm.bios.other
----------------
This module provides functions to use BIOS interrupts related to various
things, like coprocessors or memory blocks.
"""

def detect_coprocessor(program) -> None:
    """
    This function checks if there is a coprocessor or not. If AH = 0x00,
    there is no coprocessor and if AH = 0xff, there is one.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x4f",
                                "int 0x15"])

def move_memory_block(source, destination, bytes_n: int, program) -> None:
    """
    This function moves bytes from a memory block to another.

    Parameters:
    source: the source block
    destination: the destination block
    bytes_n: the number of bytes to move
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x87",
                                f"mov ds, seg {source}",
                                f"mov si, {source}",
                                f"mov es, seg {destination}",
                                f"mov di, {destination}",
                                f"mov cx, {bytes_n}",
                                "int 0x15"])

def get_extmem_size(program) -> None:
    """
    This function stores the size of the extended memory in AX (in kilobytes).

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x88",
                                "int 0x15"])

def ext_malloc_on(block_size: int, program) -> None:
    """
    This function turns on extended memory allocation.

    Parameters:
    block_size: the size of the block in kilobytes
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Note:
    Base address of allocated block is in AX:BX.

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0xc0",
                                f"mov bx, {block_size}",
                                "int 0x15"])

def ext_malloc_off(base_segment, base_offset, program) -> None:
    """
    This function turns off extended memory allocation.

    Parameters:
    base_segment: the base segment
    base_offset: the base offset
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0xc1",
                                f"mov ax, [{base_segment}]",
                                f"mov bx, [{base_offset}]",
                                "int 0x15"])

def move_extmem_block(source, destination, bytes_n: int, blocks: int, program) -> None:
    """
    This function moves bytes of an extended memory block to another.

    Parameters:
    source: the source block
    destination: the destination block
    bytes_n: the number of bytes to move
    blocks: the number of blocks to move
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x87",
                                f"mov ds, seg {source}",
                                f"mov si, {source}",
                                f"mov es, seg {destination}",
                                f"mov di, {destination}",
                                f"mov cx, {blocks}",
                                f"mov bx, {bytes_n}"
                                "int 0x15"])