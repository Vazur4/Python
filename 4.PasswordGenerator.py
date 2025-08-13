import random
abecedario = [chr(i) for i in range(97, 123)]+ [chr(i)for i in range(65,91)] 
ascii_characters = [chr(i) for i in range(33,46)]


print("How many letter would you like in your password?")
leng = int(input())
print("How many symbols would you like?")
symbols = int(input())
print("How many numbers would you like?")
number = int(input())
pas = []
for i in range(leng):
    pas.append(random.choice(abecedario))

for i in range(symbols):
    pas.append(random.choice(ascii_characters))

for i in range(number):
    pas.append(str(random.randrange(0,11)))

random.shuffle(pas)
pasw = ""
for i in pas: pasw+= i
print(pasw)
