import random
print('這是一個猜數字的遊戲')
up = input('請輸入上限: ')
down = input('請輸入下限: ')
up = int(up)
down = int(down)
r = random.randint(down, up)
time = 0
while True:
	time = time + 1
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('恭喜你答對了')
		print('你一共猜了', time, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小') 
	print('你一共猜了', time, '次')