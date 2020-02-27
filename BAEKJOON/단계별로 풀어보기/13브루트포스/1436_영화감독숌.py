N = int(input())
number = 0
cnt = 0
while cnt != N:
    number += 1
    if '666' in str(number):
        cnt += 1
print(number)

# N = int(input())
# cnt = 1
# num_front = 0
# num_final = -1
# while cnt != N:
#     cnt += 1
#     num_front += 1
#     if (num_front % 10) == 5:
#         for _ in range(10**(num_front//10+1)):
#             cnt += 1
#             num_final += 1
#             if cnt == N:
#                 break
#         if cnt == N:
#             break
#         num_front += 1
#         num_final = -1
# if num_final == -1:
#     print(str(num_front) + '666')
# elif num_front // 10:
#     print(str(num_front//10) + '666' + str(num_final))
# else:
#     print('666' + str(num_final))