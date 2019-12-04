from naan_factory_functions import *
# Here we run the factory (functions)
# We call the function

print('Welcome to the naan factory')
produce1 = input('What is the first produce?')
produce2 = input('What is the second produce?')

output1 = make_dough1(produce1, produce2)
final_output = bake_dough(output1)

print('Well done! You made some:', final_output)
