from random import randint


passed = True

for x in range(1000):
    rand_1 = randint(-100,100)
    rand_2 = randint(-100,100)
    rand_3 = randint(-100,100)
    if rand_1 > rand_2:
        if rand_2 > rand_3:
            largest = rand_1
            smallest = rand_3
        elif rand_1 > rand_3:
            largest = rand_1
            smallest = rand_2
        else:
            largest = rand_3
            smallest = rand_2
    else:
        if rand_1 > rand_3:
            largest = rand_2
            smallest = rand_3
        elif rand_2 > rand_3:
            largest = rand_2
            smallest = rand_1
        else:
            largest = rand_3
            smallest = rand_1
    if largest != max(rand_1, rand_2, rand_3) or \
       smallest != min(rand_1, rand_2, rand_3):
        passed = False
        break

print(passed)

abs(sum(rand_1, rand_2, rand_3))
