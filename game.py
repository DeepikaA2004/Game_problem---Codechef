def maximum_special_attacks(X, Y):
    max_attacks = Y // X
    return max_attacks

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read X and Y for each test case
    X, Y = map(int, input().split())
    
    # Calculate the maximum number of special attacks
    result = maximum_special_attacks(X, Y)
    
    # Print the result
    print(result)
