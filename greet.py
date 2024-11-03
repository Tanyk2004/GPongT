def greet(a, b, c):
    print("Hello, greet1!", a, b, c)

def greet_1(a, b, c):
    print("Hello, gree_1!", a, b, c)

def greet_2(a, b, c):
    print("Hello, gree_2!", a, b, c)

functions = [greet, greet_1, greet_2]
for function  in functions:
    function(1, 2, 3)