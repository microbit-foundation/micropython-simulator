# tests for bool objects

# basic logic
print(not False)
print(not True)
print(False and True)
print(False or True)

# unary operators
print(+True)
print(-True)

# unsupported unary op
try:
    len(False)
    print('FAIL')
except TypeError:
    print("PASS")
