from myhdl import block, instances

@block
def top(dots = ...): #Def arg changed to avoid error
    dots
    instance_1 = module_1(dots)
    instance_2 = module_2(dots)
    dots
    instance_n = module_n(dots)
    dots
    return instances()