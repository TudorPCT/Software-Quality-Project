# Software-Quality-Project

## Goal

Develop a simulator of a computing system.

## Phase 1 - application development

Specifications

The main components of the system are:

- the processor
- the memory
- the peripheral devices

### Processor specifications

- The processor has 8 data registers, each of them 16-bit wide, and a set of conditional flags (see below). It also possible to define special-purpose registers (e.g., stack pointer or program counter).
- The processor's instructions perform the following operations:
  - assignment
  - addition, subtraction, multiplication, division
  - Boole operations: NOT, AND, OR, XOR, shift
  - comparison: sets the internals flags depending on the relation betwen the two operands (==, !=, <, >, <=, >=)
  - jumps: unconditional, conditional (based on the flags set by previous comparison)
  - push/pop (using part of the system memory as a stack)
  - function call/return (also using the stack)
- For each unary operation, the operand also stores the result (where needed).
- Each binary operation is implemented by an instruction with 2 operands, and the first operand is also the destination where the result is stored.
- The operands (always 16-bit wide) may be:
  - data registers
  - memory locations
  - constant values
-The instructions executed by the processor are read from a text file, where they are written in an assembly-like language.

### Memory specifications

- There are two separate memory spaces for the instruction codes and for the program data, respectively.
- The sizes of the two memory components are set up through the program's configuration file and must comply with the following restrictions:
  - each size must be a multiple of 1 KB ( = 1024 bytes)
  - each size may not exceed 65536 ( = 216) bytes
- Whenever an instruction uses a memory location as an operand, the address is specified either by a constant value or by a data register.
- Because all operands are 16-bit wide, any read/write operation to the data memory is accessing two consecutive addresses at once.
- For the instruction memory, each instruction is considered to occupy 1 byte. The address of each instruction is equal to the line number in the input text file.

### Peripheral devices specifications

- There are two peripheral devices: the keyboard and the screen.
- The keyboard is simulated by a FIFO buffer, which can be read by the processor.
- The screen is simulated by a video memory, which can be written by the processor. The screen is a text display, of rectangular shape.
- The peripheral devices are accessible through a graphical interface, which allows the user to input data to the keyboard buffer and see the screen.
- Both devices are mapped into the data memory:
  - The keyboard buffer is allocated a single address, which is repeatedly read by the processor in order to get the characters input by the user.
  - The screen is allocated a range of consecutive addresses, equal in size to the number of characters of the screen. Each byte in that range corresponds to a character on the   screen, starting with the upper-left corner and moving right, then down. Any write to a location in the video memory will have immediate effect on the corresponding character on the screen.
  - The addresses allocated to the devices in the data memory are set up through the program's configuration file.
- Unlike the memory cells, the peripheral devices are accessed on 8 bits:
  - Whenever a byte is read from the address associated with the keyboard buffer, only the lower byte of the destination operand is overwritten.
  - Also, when video memory is accessed, only the lower byte of the source operand is written to the destination address.
  
### General requirements

- The implementation must not make use of library functions, i.e., the code must be written by the programmers. There is one exception from this rule: the implementation of the graphical interface, where the use of libraries is allowed.
- Permanent communication with the beneficiary is necessary, so feel free to ask any questions you may have about the requirements. Programs that do not do what they are supposed to, due to misunderstanding the requirements, will be penalized.
- Any programming language may be used, provided there are unit testing and mocking tools for it, as well as assertions (which must be language-specific, apart from unit testing assertions); all these will be necessary during the subsequent phases.
- It is recommended to design a program structure as simple as possible, without including any additional features than the ones mentioned above. The goal is to create a working version of the program, not necessarily fully stable or error-free, on which testing techniques will subsequently be applied.
- Throughout the project phases it is also necessary to sketch the documentation, which will be written and delivered in the final phase.


### Deadlines

- Set up the teams (3-4 persons): April 22
- Finalize program development: May 13

## Phase 2 - unit testing

### Specifications

- Use of unit testing tools to test the code developed during phase 1.
- Reminder: unit testing is about discovering if the module being tested can handle incorrect input data (provided by other modules or by application I/O). Error fixing is NOT required.
- Testing must provide code coverage as complete as possible. For indications regarding the conditions to be tested, read the courses.
- Each module must be tested independently. For simulating the interactions with other modules, where necessary, mocking will be used.

### Deadline

Finalize the unit testing code: May 20
