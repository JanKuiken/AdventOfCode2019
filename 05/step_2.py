with open('input.txt') as f:
    blob = f.read()[:-1]

memory = [int(i_str) for i_str in blob.split(',')]

def get_input():
    # part 1:
    # "provide it 1, the ID for the ship's air conditioner unit."
    # part 2:
    # "provide it 5, the ID for the ship's thermal radiator controller"
    return 5

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
        
        # too shorten the code set some variables required by various
        # opcodes (note: this is a classical speed vs size issue)
        if opcode in (1,2,5,6,7,8):
            # these opcode's need two parameters
            par_1 = get_parameter(mem, pc+1, p_1_mode)
            par_2 = get_parameter(mem, pc+2, p_2_mode)
        if opcode in (1,2,7,8):
            # these opcode's need the third parameter as an address
            addr_3 = mem[pc+3]

        # handle the opcode
        if opcode == 1: 
            # add
            mem[addr_3] = par_1 + par_2
            pc += 4

        elif opcode == 2:
            # multiply
            mem[addr_3] = par_1 * par_2
            pc += 4

        elif opcode == 3:
            # input
            inp = get_input()
            mem[mem[pc+1]] = inp
            pc += 2

        elif opcode == 4:
            # output
            out = get_parameter(mem, pc+1, p_1_mode) 
            set_output(out)
            pc += 2

        elif opcode == 5:
            # jump if true
            pc = par_2 if par_1 != 0 else pc+3

        elif opcode == 6:
            # jump if false
            pc = par_2 if par_1 == 0 else pc+3

        elif opcode == 7:
            # less than
            mem[addr_3] = int(par_1 < par_2)
            pc += 4

        elif opcode == 8:
            # equals
            mem[addr_3] = int(par_1 == par_2)
            pc += 4

        elif opcode == 99:
            return(mem[0])

        else:
            raise ValueError('Oops, should not happen')

# oke, run the program
run_program(memory)

