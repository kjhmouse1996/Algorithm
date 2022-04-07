#ards = []
#cards = list()

#mulcam = {'name':'멀캠','age':5,'address':'역삼'}

#mulcam_infos = ['멀캠',5,'역삼','선릉멀캠',3,'선릉']

#mulcam_infos = [
#    {'name':'멀캠','age':5,'address':'역삼'},
#    {'name':'선릉멀캠','age':3,'address':'선릉'}
#]

#mulcam_cards1 = [8,3,2,8,1,8]
#mulcam_cards12 = [5,6,4,2,9,1]

#all_player_cards = [[8,3,2,8,1,8],[5,6,4,2,9,1]]

#for i in range(11):
#    print(i)

#cards = [8,3,2,8,1,8]
#1번 
#for card in cards:
#    print(card) 

#houses = [0,0,0,0,0,0,0,0,0,0]
#ready = True
#num_cal = 0

#for house in houses:
#    if house ==1:
#        print('작업 하면 안돼요')
#        break
#else: #break가 한번도 안걸렸을 때 출력해줌
#    print('작업을 시작해도됩니다')
#print(num_cal)

#nums = [1,5,77,26,33,2,6,16,55]

#max_num = max(nums)
#print(max_num)
#max_num=-1 # 나올 수 없는 작은 숫자를 기준을 잡음
#for num in nums:
#    if max_num < num:
#        max_num = num

# 받아줄 수 있는 틀을 만듦
#odd_nums = []
# nums = [2,5,77,26,33,2,6,16,55]
#for num in nums:
#    if num % 2 ==1:
#        odd_nums.append(num)
#print(odd_nums)

# min_num = nums[0]
# for num in range(1,len(nums)):
#    if min_num > nums[num]:
#        min_num = nums[num]
# print(min_num)

## Baby-Gin 게임
#cards = [8,3,2,8,1,8]
#cards_count = [0,0,0,0,0,0,0,0,0,0,0] #바를 정자를 그릴 틀

#for num in cards:
#    cards_count[num] +=1
#print(cards_count)

#for cnt in cards_count:
#    if cnt >= 3:
#        print('triplet을 찾았습니다')

#run여부
# cards = [4, 8, 7, 3, 1, 5, 5, 6]
# cards_count = [0]*10
# is_run=False
# for num in cards:
#    cards_count[num] +=1
# for count in range(len(cards)-2):
#     if cards_count[count] >=1 and cards_count[count+1]>=1 and cards_count[count+2] >=1:
#         is_run = True
# print(is_run)

# cards = [4, 8, 1, 3, 1, 6, 6, 6]
# cards_count = [0]*10
# is_run=False 

# for num in cards: 
#    cards_count[num] += 1
# for j in range(len(cards_count)-2):
# 		if 0 not in cards_count[j:j+3]: #3개를 가져왔을 때 그 중 0이 없을 경우
# 			is_run = True
# print(is_run)

#string
# my_name = 'alex'

# for i in my_name:
#     print(i)

# customer_id = 'alex@hphk.kr'
# # splitted_list = customer_id.split('@')
# # print(splitted_list[0])

# real_id = ''
# for letter in customer_id:
#     if letter != '@':
#         real_id += letter
#     elif letter == '@':
#         break
# print(real_id)


# 회문 reverse해도 똑같은 경우
# word = input()
# reverse_word = word[::-1]
# print(word, reverse_word)
# reverse_word = ''
# for num in range(len(word)-1,-1,-1):
#     print(num)
# for idx in word[::-1]:
#     reverse_word += idx
# if word == reverse_word:
#     print(1)
# else:
#     print(0)