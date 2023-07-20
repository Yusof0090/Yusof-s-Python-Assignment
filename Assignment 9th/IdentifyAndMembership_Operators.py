# Identity and Membership Operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Identity Operator - 'is'
result = a is b
print(result)

result = a is c
print(result)

# Membership Operator - 'in'
result = 2 in a
print(result)

result = 4 in a
print(result)

result = 'hello' in 'hello world'
print(result)