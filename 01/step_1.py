with open('input.txt') as f:
    blob = f.read()[:-1]

mass = [int(i_str) for i_str in blob.split('\n')]
fuel = [(m//3)-2 for m in mass]

print('\n\n answer : ', sum(fuel))

