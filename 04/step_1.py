pw_min = 357253
pw_max = 892942

valid_pws = []

for pw in range(pw_min, pw_max+1):
    d = [int(c) for c in str(pw)]  # d is a int list of the digits
    # check never decrease condition
    if d[1]<d[0] or d[2]<d[1] or d[3]<d[2] or d[4]<d[3] or d[5]<d[4]:
        continue  
    # check two adjecient condition
    if d[1]==d[0] or d[2]==d[1] or d[3]==d[2] or d[4]==d[3] or d[5]==d[4]:
        valid_pws.append(d)  

print('\n\n answer part 1 : ', len(valid_pws))

# part 2
from collections import Counter

valid_pws_2 = []

# uit voorgaande moeten we een setje van twee vinden
# (uit stijgings conditie weten we dat x???xx niet kan voorkomen
for d in valid_pws:
    c = Counter(d)
    if 2 in c.values():
        valid_pws_2.append(d)

print('\n\n answer part 2 : ', len(valid_pws_2))

