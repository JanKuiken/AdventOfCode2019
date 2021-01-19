with open('input.txt') as f:
    blob = f.read()[:-1]

memory = [int(i_str) for i_str in blob.split(',')]

def get_input():
    # "provide it 1, the ID for the ship's air conditioner unit."
    return 1  

def set_output(val):
    print(' output : ', val)

def get_parameter(mem, addr, mode):
    return mem[addr] if mode == 1 else mem[mem[addr]]

def run_program(mem):
    pc = 0
    while(True):
    
        command = ('00000' + str(mem[pc]))[-5:] # command_str
        opcode = int(command[3:])
        p_1_mode = int(command[2])  # 1 immediate-, 0 position-mode
        p_2_mode = int(command[1])
        p_3_mode = int(command[0])

        if opcode == 1: 
            # add
            par_1 = get_parameter(mem, pc+1, p_1_mode)
            par_2 = get_parameter(mem, pc+2, p_2_mode)
            mem[mem[pc+3]] = par_1 + par_2
            pc += 4

        elif opcode == 2:
            # multiply
            par_1 = get_parameter(mem, pc+1, p_1_mode)
            par_2 = get_parameter(mem, pc+2, p_2_mode)
            mem[mem[pc+3]] = par_1 * par_2
            pc += 4

        elif opcode == 3:
            # input
            inp = get_input()
            mem[mem[pc+1]] = inp
            pc += 2

        elif opcode == 4:
            # output
            out = mem[pc+1] if p_1_mode == 1 else mem[mem[pc+1]] 
            set_output(out)
            pc += 2

        elif opcode == 99:
            return(mem[0])

        else:
            raise ValueError('Oops, should not happen')

# oke, run the program
run_program(memory)




