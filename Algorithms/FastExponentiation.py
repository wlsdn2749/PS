def get_fast_exponentiation(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        exponent >>= 1
        base = (base * base) % mod
        
    return result     


print(get_fast_exponentiation(2, 10, 17))
    
            