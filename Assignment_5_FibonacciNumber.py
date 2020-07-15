fibonacci = []
i = -2
fibo = 0
while fibo < 55:
  if i < 0:
    fibonacci.append(1)
    i += 1
  else:
    fibo = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(fibo)
    i += 1
print(fibonacci)