from collections import deque

with open('input.txt') as f:
    blob = f.read()[:-1]

memory = [int(i_str) for i_str in blob.split(',')]

# Although i don't like to write classes in Python, day 7 part 2 forces
# me to do, just to keep things managable... :-( 

# Our Intcode computer must now suspend operations waiting for results
# of other Intcode computers, lets bite the bullet and make it a class

class IntCodeComputer:

    # constants
    FINISHED          = 100_001  # some random, but recognizable numbers 
    HALTED_FOR_INPUT  = 100_002
    HALTED_FOR_OUTPUT = 100_003

    def __init__(self, mem, computer_number):
        self._mem = mem
        self._number = computer_number
        self._pc = 0
        self._halted_for_input = False
        self._inp = None
        self._halted_for_output = False
        self._outp = None
        
    def _get_parameter(self, mem, addr, mode):
        return mem[addr] if mode == 1 else mem[mem[addr]]

    def continue_with_input(self, inp):
        self._inp = inp
        print(f'IntCode number {self._number} continued with input {inp} [{self._pc}]')
        return self.run_program()

    def continue_from_output(self):
        print(f'IntCode number {self._number} continued from output [{self._pc}]')
        return self.run_program()

    def get_output(self):
        return self._outp

    def run_program(self):
        while(True):
        
            command = ('00000' + str(self._mem[self._pc]))[-5:] # command_str
            opcode = int(command[3:])
            p_1_mode = int(command[2])  # 1 immediate-, 0 position-mode
            p_2_mode = int(command[1])
            
            # too shorten the code set some variables required by various
            # opcodes (note: this is a classical speed vs size issue)
            if opcode in (1,2,5,6,7,8):
                # these opcode's need two parameters
                par_1 = self._get_parameter(self._mem, self._pc+1, p_1_mode)
                par_2 = self._get_parameter(self._mem, self._pc+2, p_2_mode)
            if opcode in (1,2,7,8):
                # these opcode's need the third parameter as an address
                addr_3 = self._mem[self._pc+3]

            # handle the opcode
            if opcode == 1: 
                # add
                self._mem[addr_3] = par_1 + par_2
                self._pc += 4

            elif opcode == 2:
                # multiply
                self._mem[addr_3] = par_1 * par_2
                self._pc += 4

            elif opcode == 3:
                # input
                if self._halted_for_input:
                    self._halted_for_input = False
                    self._mem[self._mem[self._pc+1]] = self._inp
                    self._pc += 2
                else:
                    self._halted_for_input = True
                    print(f'IntCode number {self._number} halted for input')
                    return(self.HALTED_FOR_INPUT)

            elif opcode == 4:
                # output
                if self._halted_for_output:
                    self._halted_for_output = False
                    self._pc += 2
                else:
                    self._halted_for_output = True
                    out = self._get_parameter(self._mem, self._pc+1, p_1_mode) 
                    self._outp = out
                    print(f'IntCode number {self._number} halted for output of {out}')
                    return(self.HALTED_FOR_OUTPUT)

            elif opcode == 5:
                # jump if true
                self._pc = par_2 if par_1 != 0 else self._pc+3

            elif opcode == 6:
                # jump if false
                self._pc = par_2 if par_1 == 0 else self._pc+3

            elif opcode == 7:
                # less than
                self._mem[addr_3] = int(par_1 < par_2)
                pc += 4

            elif opcode == 8:
                # equals
                self._mem[addr_3] = int(par_1 == par_2)
                self._pc += 4

            elif opcode == 99:
                return(self.FINISHED)

            else:
                raise ValueError('Oops, should not happen')


# oke, made a class for the IntCodeComputer, let try it...

max_thrust = 0
max_phase = None
from itertools import permutations
for phase in permutations([5,6,7,8,9]):

    print(phase)
    # create our amplifiers computers
    IntCodes = []
    for i in range(5):
        IntCodes.append(IntCodeComputer(memory.copy(), i))    
    
    print('start computers and input the first input: phase')
    for i in range(5):
        if IntCodes[i].run_program() == IntCodeComputer.HALTED_FOR_INPUT:
             # cool, this is what we expect, input phase
             IntCodes[i].continue_with_input(phase[i])
        else:
            raise ValueError('Oops, expected input request for phase')
    

    print('continue computers and input the second input: thrust')
    thrust = 0
    while True:
        # even stom, op goed vertrouwen, dat het programma doet wat ie moet
        for i in range(5):
            result = IntCodes[i].continue_with_input(thrust)
            thrust = IntCodes[i].get_output()
            result = IntCodes[i].continue_from_output()
            
        if result == IntCodeComputer.FINISHED: # is het result van de 5e
            print('FINISHED')
            break

    print('\n\n result for :', phase, thrust)
    if thrust > max_thrust:
        max_thrust = thrust
        max_phase = phase

print('\n\n  answer', max_phase, max_thrust)

