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
                          'depth'  : node['depth'] + 1 
                        }
            node['childs'].append(new_child)
            directory[child] = new_child
            fill_node(new_child) # wheew, the recurive part

# construct root node and add it to the directory
tree = {
         'label'  : 'COM', 
         'childs' : [], 
         'depth'  : 0,     
       }
directory = {'COM' : tree}

# fill the rest of the tree
fill_node(tree)


cum_depth = 0
for label, node in directory.items():
    #print(label, node['depth'])
    cum_depth += node['depth']

print('\n\n  answer : ', cum_depth)








    

