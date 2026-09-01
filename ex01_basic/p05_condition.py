from tkinter import simpledialog

score = simpledialog.askinteger(title="Score", prompt="Score: ")
result = ''
if score >= 90:
    result = 'A'
elif score >= 80:
    result = 'B'
elif score >= 70:
    result = 'C'
elif score >= 60:
    result = 'D'
else:
    result = 'F'

def subGrade(score):
    if score == 100:
        return '+'
    elif score < 100 and score >= 60:
        if (score % 10 >= 7):
            return '+'
        elif (score % 10 >= 4):
            return '0'
        else:
            return '-'
    else:
        return ''

print(f"Your Grade is {result}{subGrade(score)}")

a = 1
if a in (1,2,3):
    print("Yes")
else:
    print("No")

print(f"{" 파이썬에는 switch case문이 없다 ":=^30}")
def switch_case(key):
  zipcode = {'연산동': "00000", "진구": "00001"}.get(key, '알수없는 번호')
  print("우편번호:{} / 동: {}".format(zipcode, key))
switch_case('연산동')

# 대신에 match case문이 있다. Python 3.10+
for i in range(1, 11):
  match (i%2):
    case 0:
      print(f'{i} is even.')
    case 1:
      print(f'{i} is odd.')

# 복수 조건 가능:  match (i%2,i%3,i%5) case (1,0,_):
for i in range(1, 11):
  match (i%2,i%3,i%5):
    case (0,0,0):
      print(f'{i} 3, 5의 배수이면서 짝수임.')
    case (1,0,_): #'_'표시는 어떤 값이든 상관 없다.
      print(f'{i} 3의 배수이면서 홀수임.')
    case (0,_,_):
      print(f'{i} 짝수임')
    case (_,_,0):
      print(f'{i} 5의 배수임')
    case (_,0,_):
      print(f'{i} 3의 배수임')
    case _:
      print(f'{i} ')
