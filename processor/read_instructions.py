from memory.program_memory import *


class MemoryOperand:
    def __init__(self, address):
        self.address = address


class InstructionParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.instruction_classes = {
            'mov': Mov,
            'add': Add, 'sub': Sub, 'mul': Mul, 'div': Div,
            'not': NOT, 'and': AND, 'or': OR, 'xor': XOR,
            'shl': SHL, 'shr': SHR,
            'cmp': Cmp,
            'jmp': Jmp, 'je': JE, 'jne': JNE, 'jz': JZ, 'jg': JG, 'jl': JL, 'jge': JGE, 'jle': JLE,
            'push': Push, 'pop': Pop
        }

    @staticmethod
    def parse_operand(operand_str):
        if operand_str.startswith("[") and operand_str.endswith("]"):
            value = operand_str[1:-1]
            if value.isdigit():
                return MemoryOperand(int(value))
                pass
        elif operand_str.isdigit():
            return Int16(int(operand_str))
        else:
            return operand_str

    def parse_instruction(self, instruction_str):
        parts = instruction_str.split()
        if len(parts) >= 2:
            mnemonic = parts[0].lower()
            if mnemonic in self.instruction_classes:
                instruction_class = self.instruction_classes[mnemonic]
                operands = [self.parse_operand(op) for op in parts[1:]]
                return instruction_class(*operands)
        raise ValueError("Invalid instruction format")

    def read_instructions_from_file(self):
        instructions = []
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    instructions.append(self.parse_instruction(line))
        return instructions


if __name__ == "__main__":
    instruction_parser = InstructionParser("/Users/cosminpasat/Desktop/MAN1/QA/Software-Quality-Project/resources/instructions.txt")
    instructions = instruction_parser.read_instructions_from_file()
    print("asd")


