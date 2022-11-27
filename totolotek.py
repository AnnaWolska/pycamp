import random
print("hellothere")

my_numbers = [13,17,7,33,5,10]
print(my_numbers)

iter_num = 1
f_r =range(1,50)
first=[]
for n in f_r:
    first.append(n)
print(first)

first_draw = []
while iter_num < 7:
    first_draw.append(first[0])
    random.shuffle(first)
    iter_num += 1

print(first_draw)