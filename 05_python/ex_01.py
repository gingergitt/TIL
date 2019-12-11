import random
numbers = random.sample(range(1,46),6) #1부터 45사이의 숫자를 랜덤으로 6개 가져온다.
numbers2 = random.randrange(46)  #1부터 46사이의 숫자를 랜덤으로 하나 가져온다.
print(numbers)
print(numbers2)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list 값 섞기 (tuple, dict 에서는 불가능)
random.shuffle(num_list)
print(num_list)  # [2, 8, 9, 7, 10, 6, 4, 1, 3, 5]