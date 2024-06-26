import os
from src.memory.instructions.basic_instructions import *
from src.memory.instructions.jump_instructions import *
from src.memory.instructions.stack_instructions import *


class InstructionParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.instruction_classes = {
            'mov': Mov,
            'add': Add, 'sub': Sub, 'mul': Mul, 'div': Div,
            'not': NOT, 'and': AND, 'or': OR, 'xor': XOR,
            'shl': SHL, 'shr': SHR,
            'cmp': Cmp,
            'jmp': Jmp, 'jeq': JEQ, 'jneq': JNEQ, 'jgt': JGT, 'jlt': JLT, 'jgteq': JGTEQ, 'jlteq': JLTEQ,
            'jz': JZ, 'jnz': JNZ,
            'push': Push, 'pop': Pop,
            'ret': Ret,
            'call': Call
        }
        self.jumps = {'jmp', 'jeq', 'jneq', 'jgt', 'jlt', 'jgteq', 'jlteq', 'jz', 'jnz', 'call'}
        self.no_arg_instructions = {'ret'}

    @staticmethod
    def parse_operand(operand_str):
        if operand_str.endswith(","):
            operand_str = operand_str[:-1]

        if operand_str.startswith("[") and operand_str.endswith("]"):
            value = operand_str[1:-1]
            if value.isdigit():
                return Operand(MemoryLocation(Int16(int(value))))

            return Operand(MemoryLocation(Register[value]))

        elif operand_str.isdigit():
            return Operand(Int16(int(operand_str)))
        else:
            return Operand(Register[operand_str])

    def parse_instruction(self, instruction_str, labels):
        parts = instruction_str.split()
        if len(parts) >= 2:
            mnemonic = parts[0].lower()
            if mnemonic in self.instruction_classes:
                instruction_class = self.instruction_classes[mnemonic]
                if mnemonic in self.jumps:
                    operands = [Operand(Int16(labels[parts[1]]))]
                else:
                    operands = [self.parse_operand(op) for op in parts[1:]]
                return instruction_class(*operands)

        elif len(parts) == 1 and parts[0].lower() in self.no_arg_instructions:
            return self.instruction_classes[parts[0].lower()]()

        raise ValueError("Invalid instruction format")

    def read_instructions_from_file(self):
        instructions = []
        labels = {}
        line_index = 0

        assert os.path.isfile(self.file_path)

        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.endswith(":"):
                    labels[line[:-1]] = line_index
                elif line:
                    line_index += 1
                    assert line_index >= 0

            file.seek(0)
            for line in file:
                line = line.strip()
                if line:
                    if line.endswith(":"):
                        continue
                    instructions.append(self.parse_instruction(line, labels))
                    assert len(instructions) <= line_index

        assert len(instructions) == line_index
        return instructions
