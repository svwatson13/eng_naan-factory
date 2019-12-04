from naan_factory_functions import *
# Tests go here for separation of concerns

print("testing make_dough with 'water' and 'flour'. Expected --> 'dough'")
# print statements used for boolean test (True/False)
print(make_dough('water', 'flour') == 'dough')
print('when testing make_dough we got:', make_dough('water', 'flour'))

print("testing bake_dough with 'dough'. Expected --> 'naan'")
print(bake_dough('dough') == 'naan')
print('when testing bake_dough we got:', bake_dough('dough'))

print(make_dough('water', 'flour') == 'dough')
print(make_dough('water', 'water') == 'dough')
print(make_dough('flour', 'flour') == 'dough')
print(make_dough('water', 'cement') == 'not dough')
print(bake_dough('chicken') == 'not naan')
print(bake_dough('DOUGH') == 'not naan')

print(run_factory('flour', 'water'))