import math

# Manually implemented sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Test values
values = [-5, -2, 0, 2, 5]

for value in values:
    print(f"sigmoid({value}) = {sigmoid(value):.4f}")
