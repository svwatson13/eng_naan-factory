## Basis of a test
## Usually be testing functions or methods, these need to be called or initialised
## Having controlled inputs for known outputs
    # and testing for these

## Make test for make_dough
# def make_dough(ing1, ing2):
#     return 'dough'
## Our factory should take in flour and water to make dough
# print("testing make_dough with 'water' and 'flour'. Expected --> 'dough'")
## print statements used for boolean test (True/False)
# print(make_dough('water', 'flour') == 'dough')
# print('when testing make_dough we got:', make_dough('water', 'flour'))

## When I pass in cement and water, or anything else into make_dough... shouldn't get dough

## Make test for bake_dough
# def bake_dough(ing1):
# #     return 'naan'
## Should be able to put dough in oven and get naan
# print("testing bake_dough with 'dough'. Expected --> 'naan'")
# print(bake_dough('dough') == 'naan')
# print('when testing bake_dough we got:', bake_dough('dough'))

## When I pass in something other than dough into bake_dough... shouldn't get naan

## My method
def make_dough(ing1, ing2):
    if ing1 or ing2 == 'water':
        if ing1 == ing2:
            return 'not dough'
        if ing1 or ing2 != 'flour':
            return 'not dough'
        else:
            return 'dough'
    else:
        return 'not dough'

## Filipe's method
def make_dough1(ing1, ing2):
    if 'water' != ing1 and 'water' != ing2:
        return 'not dough'
    if 'flour' != ing1 and 'flour' != ing2:
        return 'not dough'
    elif 'flour' in [ing1, ing2] and 'water' in [ing1, ing2]:
        return 'dough'


def bake_dough(ing1):
    if ing1.lower() == 'dough':
        return 'naan'
    else:
        return 'not naan'


print(make_dough1('water', 'flour') == 'dough')
print(make_dough('water', 'water') == 'dough')
print(make_dough('flour', 'flour') == 'dough')
print(make_dough1('water', 'cement') == 'not dough')
print(bake_dough('chicken') == 'not naan')
print(bake_dough('DOUGH') == 'not naan')