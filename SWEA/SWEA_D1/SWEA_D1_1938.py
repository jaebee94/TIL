num = list(map(int, input().split()))
if num[0] > num[1]:
    num_large = num[0]
    num_small = num[1]
else:
    num_large = num[1]
    num_small = num[0]

print(num_large + num_small)
print(num_large - num_small)
print(num_large * num_small)
print(num_large // num_small)