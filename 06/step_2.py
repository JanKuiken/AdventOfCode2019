with open('input.txt') as f:
    blob = f.read()[:-1]

lines = blob.split('\n')

parent_n_childs = [line.split(')') for line in lines]

# first analysis
print(len(parent_n_childs))
# result 1036, conclusion: 'no worries' 

# some further analysis...
parents = set()
childs = set()
for p_n_c in parent_n_childs:
    parents.add(p_n_c[0])
    childs.add(p_n_c[1])
end_childs = childs.difference(parents)
print(len(parents), len(childs), len(end_childs))
# result 949 1036 88, conclusion: 'no worries'
# btw.: 949 + 88 = 1037, verschil met 1036 moet 'COM' zijn, parent but no child

# nu even verzinnen hoe we dat handig in standaard python data containers 
# (dicts, lists, etc) kunnen stoppen...
#
#  ok, we gaan voor een dict (node) met:
#
#  key    | value
#  -------+---------------------
#  label  | label (string)
#  childs | list of child nodes
#  depth  | depth (int) 

def fill_node(node):
    for parent_n_child in parent_n_childs:
        parent, child = parent_n_child
        if parent == node['label']:
            new_child = {
                          'label'  : child, 
                          'childs' : [], 
                          'depth'  : node['depth'] + 1,
                          'parent' : node['label'],
                        }
            node['childs'].append(new_child)
            directory[child] = new_child
            fill_node(new_child) # wheew, the recurive part

# construct root node and add it to the directory
tree = {
         'label'  : 'COM', 
         'childs' : [], 
         'depth'  : 0,
         'parent' : None,
       }
directory = {'COM' : tree}

# fill the rest of the tree
fill_node(tree)


cum_depth = 0
for label, node in directory.items():
    #print(label, node['depth'])
    cum_depth += node['depth']

print('\n\n  answer : ', cum_depth)

print('\n  part two, from YOU to SAN')

# ok, niet vreselijk ingewikkeld, we moeten onze node uitbreiden met
# een parent, zodat we 'naar boven' kunnen navigeren...

def route_to_root(label):
    route = []
    node = directory[label]
    route.append(node['label'])
    if node['parent']:
        route += route_to_root(node['parent'])
    return route

route_YOU = route_to_root('YOU')
route_SAN = route_to_root('SAN')
 
print()
print(route_YOU)
print()
print(route_SAN)

# cool, pretty deep, maar nu even uitzoeken waar de wegen samenkomen...
# gemeenschappelijke orbits weggooien en dan weer even puzzelen over begin 
# en eind punten.

common = len(set(route_YOU).intersection(set(route_SAN)))
route_YOU = route_YOU[:-(common-1)]
route_SAN = route_SAN[:-(common-1)]
print()
print(route_YOU)
print()
print(route_SAN)

# cool, nu even de aanwijzingen goed lezen, het gaat over het aantal
# 'orbit' stappen, YOU zit in orbit 9Z5, gemeenschappelijke orbit is JZW,
# dat is lengte van route_YOU minus 2, evenzo voor de orbit van SAN

print('\n\n  answer : ', len(route_YOU) + len(route_SAN) - 4)



