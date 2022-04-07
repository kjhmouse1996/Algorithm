# T = int(input())

# for tc in range(1,T+1):
#     N,M = map(int, input().split())
#     nums = list(map(int, input().split()))
#     sum_num = []
#     for i in range(len(nums)-(M-1)):
#         for ind in range(1,M):
#             nums[i] += nums[i+ind]
#         sum_num.append(nums[i])
#         answer = max(sum_num)-min(sum_num)

#     print(f'#{tc}, {answer}')

##Matrix
a = [[1, 8, 4], [7, 3, 9], [5, 2, 6]]

# trails = []

# for r in range(3):
#     for c in range(3):
#         trails.append(a[c][r])

# print(trails)
##전치
# a = 3
# b = 4
# a,b = b,a
# a = [[1, 8, 4], 
#      [7, 3, 9], 
#      [5, 2, 6]]
# for r in range(3):
#     for c in range(3):
#         if r >c:
#             a[r][c], a[c][r] = a[c][r],a[r][c] #파트너랑 위치 바꾸기

# matrix = [[0,0,0],[0,1,0],[0,0,0]]
# ready = False

# for r in range(3):
#     for c in range(3):
#         if matrix[r][c] == 1:
#             ready = True
#             break


## https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do 숫자카드
# T = int(input())

# for tc in range(1,T+1):
#     N = int(input()) #카드 수
#     cards = list(map(int, input().strip())) #카드 숫자
    
#     card_list = [0]*10
#     for num in cards:
#         card_list[num] += 1
    
#     max_n = 0
#     max_card = 0
#     for num_lst in card_list:
#         if max_n < num_lst:
#             max_n = num_lst
            
#     if max_n == 1:
#         max_card = max(cards)
#     elif max_n > 1:
#         for num_lst in range(len(card_list)):
#             if card_list[num_lst]==max_n:
#                 max_card = num_lst
    
#     print(f'#{tc}, {max_card} {max_n}')

# T = int(input())

# for tc in range(1,T+1):
#     part_num = list(map(int, input().split())) #참가자번호
#     part_dict = dict()
    
#     for num in part_num:
#         if not part_dict.get(num):
#             part_dict[num] = 1
#         else:
#             part_dict[num] += 1
    
#     radish = 0
#     for key, val in part_dict.items():
#         if part_dict[key] == 1:
#             radish = key
            
#     print(f'#{tc}, {radish}')




