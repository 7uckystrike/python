import random

print ('가위바위보 게임을 시작합니다!')

game = ['가위', '바위', '보']

computer = random.choice(game)
answer = input('무엇을 낼까?')


print ('컴퓨터:' + computer)
print ('나:' + answer)

if computer == '가위' :
  if answer == '가위' :
    print('비겼다!')
  elif answer == '보' :
    print('졌당!!')
  elif answer == '주먹' :
    print('이겼당!!!!')
elif computer == '보' :
  if answer == '보' :
    print('비겼습니다요..')
  elif answer == '가위' :
    print('졌습니다..')
  elif answer == '주먹' :
    print('이겼다요!!!!')
elif computer == '주먹' :
  if answer == '보' :
    print('졌습니다.....') 
  elif answer == '주먹' :
    print('비겼습니다다아아아!!!')
  elif answer == '가위' :
    print ('이겼습니다아아!!')
