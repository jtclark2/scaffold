def add(x, y):
    return x + y


result = add(1, 2)

# removing formatted strings to remain consistent with tutorial
# They don't work in python <3.6, and azure was still on python3.5 when tutorial was made  
# not sure why we don't just upgrade python environment instead? Maybe we will shortly.
# print(f"This is the sum: {1}, {1}, {result}")
print("This is the sum: %d, %d, %d" % (1, 1, result))
