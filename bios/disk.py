"""
pyasm.bios.disk
---------------
This module provides functions to use BIOS interrupts related to disk.
"""

def reset_disk(program) -> None:
    """
    This function resets the disk.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                "int 0x13"])

def read_disk_status(program) -> None:
    """
    This function reads the disk status and store it in AH.

    Parameters:
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x01",
                                "int 0x13"])

def read_sectors(sectors: int, cylinder: int, sector: int, head: int, drive: int, buffer, program) -> None:
    """
    This function reads a given number of sectors.

    Parameters:
    sectors (int): the number of sectors to read
    cylinder (int): the number of the cylinder
    sector (int): the number of the sector (must be between 1 and 63)
    head (int): the number of the head
    drive (int): the number of the drive (0x80 for hard disk)
    buffer: buffer to store data
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if 1 <= sector <= 63:
        program.asm_codegen.extend(["mov ah, 0x02",
                                    f"mov al, {sectors}",
                                    f"mov ch, {cylinder}",
                                    f"mov cl, {sector}",
                                    f"mov dh, {head}",
                                    f"mov dl, {drive}",
                                    f"mov bx, {buffer}",
                                    "int 0x13"])
    else:
        raise ValueError("The sector number must be between 1 and 63")

def write_sectors(sectors: int, cylinder: int, sector: int, head: int, drive: int, buffer, program) -> None:
    """
    This function writes on a given number of sectors.

    Parameters:
    sectors (int): the number of sectors to write on
    cylinder (int): the number of the cylinder
    sector (int): the number of the sector (must be between 1 and 63)
    head (int): the number of the head
    drive (int): the number of the drive (0x80 for hard disk)
    buffer: buffer to store data
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    if 1 <= sector <= 63:
        program.asm_codegen.extend(["mov ah, 0x03",
                                    f"mov al, {sectors}",
                                    f"mov ch, {cylinder}",
                                    f"mov cl, {sector}",
                                    f"mov dh, {head}",
                                    f"mov dl, {drive}",
                                    f"mov bx, {buffer}",
                                    "int 0x13"])
    else:
        raise ValueError("The sector number must be between 1 and 63")

def read_drive_params(drive: int, program) -> None:
    """
    This function reads the drive parameters and store them in CX, DX and
    other registers.

    Parameters:
    drive (int): the number of the drive (0x80 for hard disk)
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x08",
                                f"mov dl, {drive}",
                                "int 0x13"])

def extended_disk_access(drive: int, program, signature: int=0xaa55) -> None:
    """
    This function checks for extended disk access support. If supported, CF
    will be clear.

    Parameters:
    drive (int): the number of the drive (0x80 for hard disk)
    signature (int): the signature (default=0xaa55)
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x41",
                                f"mov bx, {signature}",
                                f"mov dl, {drive}",
                                "int 0x13"])

def extended_read_sectors(drive: int, extended_read_packet, program) -> None:
    """
    This function reads extended sectors.

    Parameters:
    drive (int): the drive number (0x80 for hard disk)
    extended_read_packet: the packet
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x42",
                                f"mov dl, {drive}",
                                f"mov si, {extended_read_packet}",
                                "int 0x13"])

def extended_write_sectors(drive: int, extended_read_packet, program) -> None:
    """
    This function writes on extended sectors.

    Parameters:
    drive (int): the drive number (0x80 for hard disk)
    extended_write_packet: the packet
    program: this is the Assembly program where the Assembly code will be
    generated. (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x43",
                                f"mov dl, {drive}",
                                f"mov si, {extended_read_packet}",
                                "int 0x13"])