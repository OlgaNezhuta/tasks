import random

in_list = random.sample(range(-1000, 1001), 1000)
print(in_list)

result = 0
for i in in_list:
   result = result + i


print(result)

average = float(result / len(in_list))
print(average)


delta = average * 20 / 100
print(delta)


out_list = [x for x in in_list if x >= (average - delta) and x <= (average + delta)]

print(out_list)

