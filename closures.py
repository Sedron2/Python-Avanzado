def make_multiplier(x):
    
    def multiplier(n):
        return x * n

    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))

# Los closures son en muuucha síntesis, son una forma de acceder a variables de otros scopes a través de una nested function