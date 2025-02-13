# PyASM
*An advanced and easy-to-use Python library used to generate functionnals Assembly programs from Python code.*

## What is PyASM?
PyASM is an advanced and easy-to-use Python library. It is designed to generate Assembly programs from Python code.
Well, not exactly.
The library contains a lot of functions which generates Assembly code when they are called. All the generated code
is written into a `.asm` file that you can run.

## Why should you use PyASM?
You want to make very low level programs but you don't want how to do? You want to say to your friends that you are
an Assembly professionnal by showing them the code generated by PyASM? You want to write an entire OS in Python?
This is possible with this library.
Anything other?

## How to use it?
Actually, there is no special install. You must download the source code (fortunately, if you are reading this
README, you probably found it).
Go in pyasm and then type:
```bash
pip install .
```

## A first project
Here is an example of a simple bootloader with PyASM.
```py
# Import necessary modules from PyASM
from pyasm.program import Program
import pyasm.data, pyasm.utils, pyasm.settings, pyasm.stream

# Create your program
bootloader = Program("bootloader.asm")

# Infinity loop
pyasm.stream.hang(bootloader)

pyasm.utils.fill_file(510, 0, bootloader)            # Fill the binary file with 0
pyasm.data.define_word(0xaa55, bootloader)           # Magic word

bootloader.generate()
bootloader.assemble("bin", "bootloader.bin")          # NASM required for this line
```

## Contributing
If you want to contribute, please read [the contribution guide](CONTRIBUTING.md) first.
