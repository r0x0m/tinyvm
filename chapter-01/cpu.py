# Smallest valid version of a CPU emulator
def main():

    memory = [0] * 256  # 256 words of memory

    registers = [0, 0, 0, 0]  # R0, R1, R2, R3
    pc = 0  # program counter

    # fmt: off
    program = [
        1, 0, 7,    # LOAD R0, 7
        1, 1, 5,    # LOAD R1, 5
        2, 2, 0, 1, # ADD R2, R0, R1
        3, 2,       # PRINT R2
        1, 0, 10,   # LOAD R0, 10
        1, 1, 3,    # LOAD R1, 3
        4, 2, 0, 1, # SUB R2, R0, R1
        5, 3, 2,    # MOV R2, R3
        3, 2,       # PRINT R2
        3, 3,       # PRINT R3
        0           # HALT
    ]
    # fmt: on
    for i, word in enumerate(program):
        memory[i] = word

        # Execution loop: fetch-decode-execute cycle
    running = True

    while running:
        # FETCH: read the instruction at the pc
        opcode = memory[pc]

        # DECODE + EXECUTE
        if opcode == 0:  # HALT
            print("[CPU] HALT - execution stopped.")
            running = False

        elif opcode == 1:  # LOAD_IMM reg, value
            reg = memory[pc + 1]
            val = memory[pc + 2]
            registers[reg] = val
            pc += 3  # advance past opcode + reg + value

        elif opcode == 2:  # ADD, dst, src1, src2
            dst = memory[pc + 1]
            src1 = memory[pc + 2]
            src2 = memory[pc + 3]
            registers[dst] = registers[src1] + registers[src2]
            pc += 4

        elif opcode == 3:  # PRINT_REG reg
            reg = memory[pc + 1]
            print(f"[CPU] R{reg} = {registers[reg]}")
            pc += 2

        elif opcode == 4:
            dst = memory[pc + 1]
            src1 = memory[pc + 2]
            src2 = memory[pc + 3]
            registers[dst] = registers[src1] - registers[src2]
            pc += 4

        elif opcode == 5:
            dst = memory[pc + 1]
            src = memory[pc + 2]
            registers[dst] = registers[src]
            pc += 3

        else:
            print(f"[CPU] ERROR - UNKNOWN opcode {opcode} at PC={pc}")
            running = False

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
