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
            print('finished')
            print('\n\n  answer : ', mem[0])
            break
        else:
            print('Oops, should not happen')
            break

# replace  to the "1202 program alarm"
memory[1] = 12
memory[2] = 2

run(memory)

