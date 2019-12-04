## Functions
def make_dough(ing1, ing2):
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

def run_factory(ing1, ing2):
    output1 = make_dough(ing1, ing2)
    final_output = bake_dough(output1)
    return final_output
