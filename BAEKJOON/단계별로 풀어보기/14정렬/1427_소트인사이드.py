num_list = list(input())
num_sort = sorted(map(int, num_list), reverse=True)
print(''.join(map(str, num_sort)))