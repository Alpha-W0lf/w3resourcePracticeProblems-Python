# Write a program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input('Please enter an integer: '))
n_str = str(n)
nn = int(n_str+n_str)
nnn = int(n_str+n_str+n_str)
print(n), print(nn), print(nnn)
print(n + nn + nnn)