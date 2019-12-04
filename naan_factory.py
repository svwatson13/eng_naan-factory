# Basis of a test
# Usually be testing functions or methods, these need to be called or initialised
# Having controlled inputs for known outputs
    # and testing for these

# Make test for make_dough
def make_dough(ing1, ing2):
    pass
## Our factory should take in flour and water to make dough
print("testing make_dough with 'water' and 'flour'. Expected --> 'dough'")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))
# Make test for bake_dough
def bake_dough(in1):
    pass
## Should be able to put dough in oven and get naan
print("testing bake_dough with 'dough'. Expected --> 'naan'")
print(bake_dough('dough') == 'naan')
print('got:', bake_dough('dough'))