# cards = [1,3,22,5]
# count_dict = dict()

# for num in cards:
#     if not count_dict.get(num):#값이 없다 none으로 나올 경우 
#         count_dict[num] = 1 #1을 넣어줌
#     else: #있을 경우
#         count_dict[num] += 1 #1을 더해줌
# print(count_dict)

# from collections import defaultdict
# cards = [1,3,22,5]

# count_dict = defaultdict(int)

# for num in cards:
#     count_dict[num] += 1
# print(count_dict)

# T = int(input()) # 처음에 몇개의 시퀀스를 넣을건지 개수를 적어주고 그다음에 시퀀스를 하나씩 입력

# for tc in range(1,T+1):
#     nums = list(map(int, input().split()))

#     count_dict = dict()

#     for num in nums:
#         if not count_dict.get(num):
#             count_dict[num] = 1
#         else:
#             count_dict[num] += 1
#     answer = 0

#     for key, val in count_dict.items():
#         if count_dict[key] == 1:
#             answer = key
#             break
#     print('#{} {}'.format(tc,answer))

# first = input()
# second = first.split()
# third = map(int, second)
# fourth = list(third)
# print('처음: ', first)
# print('두번째: ', second)
# print('세번째: ', third)
# print('네번째: ', fourth)

## https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do min max 문제
# T = int(input())

# for tc in range(1, T+1): #range(1,)1로 받는 이유
#     N = int(input())
#     nums = list(map(int, input().split()))
#     answer = max(nums)-min(nums)

#     print('#{} {}'.format(tc,answer))

## https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do 구간합
T = int(input())

for tc in range(1,T+1):
    N,M = map(int, input().split())
    nums = list(map(int, input().split()))
    sum_num = []
    for i in range(len(nums)-(M-1)):
        for ind in range(1,M):
            nums[i] += nums[i+ind]
        sum_num.append(nums[i])
        answer = max(sum_num)-min(sum_num)

    print(f'#{tc}, {answer}')