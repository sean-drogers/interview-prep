def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        add = x+y
        x = y
        y = add

    

        
        
print(fibonacci(12))
print(fibonacci(7))
print(fibonacci(20))