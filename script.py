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

s = sum_bits(a, b)

c = NOT_gate(s)

