def is_prime(num):
    criba = list(range(num+1))  # [0, 1, 2, 3, ..., num]
    
    # 0 y 1 no son primos
    criba[0] = 0
    criba[1] = 0
    
    for i in range(2, int(num**0.5) + 1):
        if criba[i] != 0:
            for j in range(i*2, num+1, i):
                criba[j] = 0
    
    if num in criba:
        return True
    else:
        return False

is_prime(29)
