user_input = input("Enter a string: ")
n = int(input("Enter n: "))

alpha = "abcdefghijklmnopqrstuvwxyz"
rev = alpha[::-1]
dict1 = dict(zip(alpha, rev))

prefix = user_input[0:n-1]
suffix = user_input[n-1:]

mirror = ""
for i in range(len(suffix)):
    mirror = mirror + dict1[suffix[i]]

result = prefix + mirror

print("Result is " + result)
