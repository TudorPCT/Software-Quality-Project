from memory.program_memory import *
from processor.processor import Register, MemoryLocation, Operand
from memory.instructions.basic_intructions import *
from memory.instructions.jump_instructions import *
from memory.instructions.stack_instructions import *


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
            'push': Push, 'pop': Pop
        }
        self.jumps = {'jmp', 'jeq', 'jneq', 'jgt', 'jlt', 'jgteq', 'jlteq'}

    @staticmethod
    def parse_operand(operand_str):
        if operand_str.endswith(","):
            operand_str = operand_str[:-1]

        if operand_str.startswith("[") and operand_str.endswith("]"):
            value = operand_str[1:-1]
            if value.isdigit():
                return Operand(MemoryLocation(Int16(int(value))))

            return Operand(MemoryLocation(Register[operand_str]))

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
        raise ValueError("Invalid instruction format")

    def read_instructions_from_file(self):
        instructions = []
        labels = {}
        line_index = 0
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.endswith(":"):
                    labels[line[:-1]] = line_index
                elif line:
                    line_index += 1

            file.seek(0)
            for line in file:
                line = line.strip()
                if line:
                    if line.endswith(":"):
                        continue
                    instructions.append(self.parse_instruction(line, labels))

        return instructions
