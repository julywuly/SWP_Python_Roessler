import matplotlib.pyplot as plt
import random

dictionary = {}
for i in range(1, 46):
    dictionary[i] = 0


def draw(li, how_many):
    drawn_numbers = []
    for j in range(how_many):
        num = random.randint(0, len(li) - 1)
        drawn_numbers.append(li[num])
        dictionary[li[num]] += 1
        li = li[:num] + li[num + 1:]
    return drawn_numbers


for i in range(1000):
    numbers = list(range(1, 46))
    result = draw(numbers, 6)
    print(f" {i + 1}: {sorted(result)}")

print(dictionary)

plt.bar(dictionary.keys(), dictionary.values())
plt.show()
