import numpy as np

with open('input.txt') as f:
    blob = f.read()[:-1]

wire_1, wire_2 = blob.split('\n')

def points_from_wire(wire):
    current_pos = np.asarray([0,0])
    directions = { 'U' : np.asarray([ 0, 1]) , 
                   'D' : np.asarray([ 0,-1]) ,
                   'L' : np.asarray([-1, 0]) ,
                   'R' : np.asarray([ 1, 0]) ,  }
    pnts = set()
    for section in wire.split(','):
        direction = section[0]
        number = int(section[1:])
        for _ in range(number):
            current_pos += directions[direction]
            pnts.add(tuple(current_pos))
    return pnts
    
pnts_1 = points_from_wire(wire_1)
pnts_2 = points_from_wire(wire_2)

cross_pnts = pnts_1.intersection(pnts_2)
manhantan_dist = [abs(x) + abs(y) for x,y in cross_pnts]

print('\n\n answer : ', min(manhantan_dist))
 
