with open('input.txt') as f:
    blob = f.read()[:-1]
mass = [int(i_str) for i_str in blob.split('\n')]

def fuel_required(m):
    fuel = (m//3)-2
    if fuel > 0:
        fuel += fuel_required(fuel)
    return max(0, fuel)

fuel = [fuel_required(m) for m in mass]

print('\n\n answer : ', sum(fuel))

