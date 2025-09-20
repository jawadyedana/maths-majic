import itertools

def calculate_Q(A, B, C):
    and_AB = A and B
    xor_AC = A ^ C  # XOR operation
    Q = and_AB or xor_AC
    return Q

# Generate all possible combinations of A, B, C
for A, B, C in itertools.product([0, 1], repeat=3):
    Q = calculate_Q(A, B, C)
    print(f"A={A}, B={B}, C={C} => Q={Q}")
