# Precedence of Operators
a = 10
b = 5
c = 2

result = a + b * c
print(result)

result = (a + b) * c
print(result)

result = a + b / c
print(result)

result = (a + b) / c
print(result)

result = a * b + c
print(result)

result = a * (b + c)
print(result)