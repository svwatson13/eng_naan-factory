# Basis of a test
# Usually be testing functions or methods, these need to be called or initialised
# Having controlled inputs for known outputs
    # and testing for these

# Make test for make_dough
## Our factory should take in flour and water to make dough
print(make_dough('water', 'flour') == 'dough')

# Make test for bake_dough
## Should be able to put dough in oven and get naan
print(bake_dough('dough') == 'naan')