import random

l = sorted(random.sample(range(-1000, 1001), 1000))
max = l[-1]
for max2 in list(reversed(l))[1:]:
    if max2 != max:
        break
print(max, max2)



# def two_biggest_digits(l):
#     max = l[-1]
#     for max2 in list(reversed(l))[1:]:
#         if max2 != max:
#             break
#     print(max, max2)
#
#
# l = sorted(random.sample(range(-1000, 1001), 1000))
# print(two_biggest_digits(l))

