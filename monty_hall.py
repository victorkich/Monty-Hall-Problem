import numpy as np
from tqdm import tqdm

LOOP_SIZE = 10000000
SEED = [0, 1, 0]


def monty_hall(typed):
    doors = SEED
    np.random.shuffle(doors)
    opted_3 = np.random.randint(0, 3)

    if not typed:
        result = doors[opted_3]
        return result
    else:
        for i in range(3):
            if i != opted_3 and not doors[i]:
                excluded_3 = i
                for j in range(3):
                    if j != excluded_3 and j != opted_3:
                        result = doors[j]
                        return result


sum_0 = 0.
sum_1 = 0.
for _ in tqdm(range(LOOP_SIZE)):
    sum_0 += monty_hall(typed=0)
    sum_1 += monty_hall(typed=1)

print('For those who stopped in the second round the percentage of hit was of: ', (sum_0/LOOP_SIZE)*100)
print('For those who changed sides in the second round the percentage of hit was of: ', (sum_1/LOOP_SIZE)*100)
