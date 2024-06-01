import numpy as np
import matplotlib.pyplot as plt
import random
import time

# prob.1 - Arithmetic Operations
print("\nprob.1 - Arithmetic Operations")
x = 10
y = 4.12

Addition = x+y
Subtraction = x-y
Multiplication = x*y
Division = x/y
Exponentiation = np.exp(x)

print(f'Addition={Addition:.2f}, Subtraction={Subtraction}, Multiplication={Multiplication}, Division={Division:.2f}, Exponentiation={Exponentiation:.2f}')


# prob.2 - Conditionals
print("\nprob.2 - Conditionals")
age = int(input("Please enter your age:\t"))
if age < 18:
    print("you're a Minor")
elif 18 <= age <= 65:
    print("you're an Adult")
elif 65 < age:
    print("you're a Senior")
else:
    print("invalid input")


# prob.3 - Loops
print("\nprob.3 - Loops")
n = 12
fib = [0, 1]
for i in range(n-2):
    new = fib[-1] + fib[-2]
    fib.append(new)
print(fib)


# prob.4 - Functions
print("\nprob.4 - Functions")

def prob4(n, d, word):
    for i in range(n):
        if i != n-1:
            end = ' - '
        else:
            end = "\n"
        print(word, end=end, flush=True)
        time.sleep(d)

prob4(5, 1, "Test")


# prob.5 - Visualization
print("\nprob.5 - Visualization")
x = np.linspace(0, 10, 1000)
noise_1 = []
noise_2 = []
for i in range(1000):
    noise_1.append(random.uniform(0, 0.05))
    noise_2.append(random.uniform(0, 0.2))

noise_1 = np.array(noise_1)
noise_2 = np.array(noise_2)

wave_1 = np.sin(x) + noise_1
wave_2 = 2*np.sin(1.5*x) + noise_2

plt.figure(1, (12, 5))
plt.plot(x, wave_1, label=r"$y_1 = \mathrm{sin}(t)$")
plt.plot(x, wave_2, label=r"$y_2 = 2\times\mathrm{sin}(1.5t)$")
plt.title("Two Different Sinusoidal Waves Subject to Noise")
plt.xlabel("time (s)")
plt.ylabel("magnitude")
plt.xlim([0, 10])
plt.legend()
plt.grid()
plt.show()
