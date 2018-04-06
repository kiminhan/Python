# for문의 기본구조
# for 변수 in 자료형
# 여러개의 element를 가져오기위해 사용한다.
# 리스트, 튜플, 문자열 가능

# my_list = "Hello"
#
# for x in my_list:
#     print(x,end='') # end는 x 이후에 \n의 역할을 없애준다.
#     print('!')

# for i in range(2,10):
#     for j in range(1,10): # 이중for문 이해 : 이중 for문은 i에 하나가 들어오고 j에 모든게 수행한 후에 다시 i로 돌아간다.
#         print(i*j, end=' ') # ex) i(1),j(1,10),i(2),j(1,10)
#     print('')

# print("[구구단 출력]")
# for i in range(2,10):
#     print('-',i,'단')
#     for j in range(1,10):
#         print(i,'*',j,'=',i*j)
#     print('')

# a = [70,60,55,75,95,90,80,80,85,100]
# total = 0
# for number in a:
#     total += number
# average = total/len(a)
# print(average)
