#This is a dice rolling simulator
import random
results = [0,0,0,0,0,0]

n = int(input("Enter the number of dice rolls to simulate: "))
for i in range(n):
    roll = random.randint(1,6)
    results[roll-1] += 1
print(results)