# Smallest valid version of a CPU emulator
def main():

    memory = [0] * 256 # 256 words of memory

    registers = [0,0,0,0] # R0, R1, R2, R3
    pc = 0 # program counter

    program = [
        1, 0, 7,    # LOAD R0, 7
        1, 1, 5,    # LOAD R1, 5
        2, 2, 0, 1, # ADD R2, R0, R1
        3, 2,       # PRINT R2
        0           # HALT
    ]

    for i, word in enumerate(program):
        memory[i] = word

        # Execution loop: fetch-decode-execute cycle
        running = True

    while running:
        # FETCH: read the instruction at the pc
        opcode = memory[pc]

        # DECODE + EXECUTE
        if opcode == 0: # HALT
            print("[CPU] HALT - execution stopped.")
            running = False

        elif opcode == 1: # LOAD_IMM reg, value
            reg = memory[pc + 1]
            val = memory[pc + 2]
            registers[reg] = val
            pc += 3 # advance past opcode + reg + value

        elif opcode == 2: # ADD, dst, src1, src2
            dst = memory[pc + 1]
            src1 = memory[pc + 2]
            src2 = memory[pc + 3]
            registers[dst] = registers[src1] + registers[src2]
            pc += 4

        elif opcode == 3: # PRINT_REG reg
            reg = memory[pc + 1]
            print(f"[CPU] R{reg} = {registers[reg]}")
            pc += 2

        else:
            print(f"[CPU] ERROR - UNKNOWN opcode {opcode} at PC={pc}")
            running = False

    return 0


if __name__ == "__main__":
    raise SystemExit(main())




        
           
    