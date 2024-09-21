# all_mem = []
# n = 5
# for i in range(n):
#     all_mem.append([int(x) for x in input(f"input score member {i+1} :").split()])
# result = []
# for i in all_mem:
#     x = sum(i)
#     result.append(x)
# result.sort()
# n = 0
# for i in all_mem:
#     n += 1
#     if result[-1] == sum(i):
#         print(f"member {n} hightest score is {sum(i)}")

all_mem = []
result = []
for i in range(5):
    all_mem.append([int(x) for x in input(f"input score member {i+1} :").split()])
for i in all_mem:
    x = sum(i)
    result.append(x)
n = 0
for i in all_mem:
    n += 1
    if max(result) == sum(i):
        print(f"member {n} hightest score is {sum(i)}")
