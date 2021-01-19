with open('input.txt') as f:
    blob = f.read()[:-1]

memory = [int(i_str) for i_str in blob.split(',')]

def run(mem):
    pc = 0
    while(True):
        if mem[pc] == 1:
            mem[mem[pc+3]] = mem[mem[pc+1]] + mem[mem[pc+2]]
            pc += 4
        elif mem[pc] == 2:
            mem[mem[pc+3]] = mem[mem[pc+1]] * mem[mem[pc+2]]
            pc += 4
        elif mem[pc] == 99:
            return(mem[0])
        else:
            raise ValueError('Oops, should not happen')

required_output = 19690720

for noun in range(100):
    for verb in range(100):
        m = memory.copy()
        m[1] = noun
        m[2] = verb
        if run(m) == required_output:
            print('\n\n  answer : ', 100 * noun + verb)

