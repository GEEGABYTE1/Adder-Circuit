from nand import NAND_gate
from and_gate import AND_gate
from not_gate import NOT_gate
from or_gate import OR_gate
from xor_gate import XOR_gate

def sum_bits(a, b):
    if a == 1 and b == 1:
        return 0
    elif a == 0 and b == 0:
        return 0 
    else:
        return 1 


def half_adder(a, b):
    s = sum_bits(a, b)
    c = AND_gate(a, b)
    return (s, c)

def full_adder(a, b, c):
    partial_sum = half_adder(a, b)[0]
    new_s = half_adder(partial_sum, c)[0]

    b_c = half_adder(b, c)[0]
    new_c = new_s
    if a == b and b == c and a == c:
        pass 
    else:
        new_c = NOT_gate(new_s)
    print("s: {}, c:{}".format(new_s, new_c))

print(full_adder(1, 1, 1))

