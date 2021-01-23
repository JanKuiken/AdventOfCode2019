from collections import deque

with open('input.txt') as f:
    blob = f.read()[:-1]

memory = [int(i_str) for i_str in blob.split(',')]

# we're gonna use some ugly global variables for the get_input 
# and set_output functions of the Intcode computer (from day 5)
input_value = deque([])
def get_input():
    global input_value
    val = input_value.popleft()
    print(' input  : ', val)
    return val

output_value = 0
def set_output(val):
    global output_value
    print(' output : ', val)
    output_value = val

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


# example program 1:
memory_ex1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
phase = [4,3,2,1,0]
output_value = 0
input_value = deque([])

for i in range(5):   # the five amplifiers
    print('run program for amp no', i)
                                     # set up input values    
    input_value.append(phase[i])     # phase for amp number i
    input_value.append(output_value) # output from previous amp
    run_program(memory_ex1.copy())
print('\n\n result example 1:', output_value)
print('\n\n')

# example program 2:
memory_ex2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
              101,5,23,23,1,24,23,23,4,23,99,0,0]
phase = [0,1,2,3,4]
output_value = 0
input_value = deque([])

for i in range(5):   # the five amplifiers
    print('run program for amp no', i)
                                     # set up input values    
    input_value.append(phase[i])     # phase for amp number i
    input_value.append(output_value) # output from previous amp
    run_program(memory_ex2.copy())
print('\n\n result example 2:', output_value)
print('\n\n')

# oke, those two examples produced the correct answer, lets try the real stuff
max_thrust = 0
max_phase = None
from itertools import permutations
for phase in permutations([0,1,2,3,4]):
    output_value = 0
    input_value = deque([])

    for i in range(5):   # the five amplifiers
        print('run program for amp no', i)
                                         # set up input values    
        input_value.append(phase[i])     # phase for amp number i
        input_value.append(output_value) # output from previous amp
        run_program(memory.copy())
    print('\n\n result for :', phase, output_value)
    print('\n\n')
    if output_value > max_thrust:
        max_thrust = output_value
        max_phase = phase

print('\n\n  answer', max_phase, max_thrust)

