"""
pyasm.bios.system
-----------------
This module provides functions to use BIOS interrupts related to system time and date operations.
"""

def read_clock_counter(program) -> None:
    """
    This function reads the clock counter.

    Parameters:
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x00",
                                "int 0x1A"])

def set_clock_counter(counter_high: int, counter_low: int, program) -> None:
    """
    This function sets the clock counter.

    Parameters:
    counter_high (int): The high word of the counter.
    counter_low (int): The low word of the counter.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x01",
                                f"mov cx, {counter_high}",
                                f"mov dx, {counter_low}",
                                "int 0x1A"])

def read_system_time(program) -> None:
    """
    This function reads the system time.

    Parameters:
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x02",
                                "int 0x1A"])

def set_system_time(hour: int, minute: int, second: int, daylight: int, program) -> None:
    """
    This function sets the system time.

    Parameters:
    hour (int): The hour (24-hour format).
    minute (int): The minute.
    second (int): The second.
    daylight (int): Daylight savings flag.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x03",
                                f"mov ch, {hour}",
                                f"mov cl, {minute}",
                                f"mov dh, {second}",
                                f"mov dl, {daylight}",
                                "int 0x1A"])

def read_system_date(program) -> None:
    """
    This function reads the system date.

    Parameters:
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x04",
                                "int 0x1A"])

def set_system_date(century: int, year: int, month: int, day: int, program) -> None:
    """
    This function sets the system date.

    Parameters:
    century (int): The century.
    year (int): The year.
    month (int): The month.
    day (int): The day.
    program: this is the Assembly program where the Assembly code will be generated.
             (Must be an instance of pyasm.program.Program).

    Return:
    None
    """
    program.asm_codegen.extend(["mov ah, 0x05",
                                f"mov ch, {century}",
                                f"mov cl, {year}",
                                f"mov dh, {month}",
                                f"mov dl, {day}",
                                "int 0x1A"])