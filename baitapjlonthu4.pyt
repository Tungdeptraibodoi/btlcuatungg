import random
secret = random.randint(10, 20)
print('chọn 1 số bất kì từ 10 đến 20')
print('bạn chỉ có thể đoán 5 lần')

for guessesTaken in range(1, 5):
  print('hãy nhập vào 1 số mà bạn nghĩ là đúng')
  guess = int(input())
  if guess < secret:
    print('nhỏ hơn số chính xác')
  elif guess > secret:
    print('lớn hơn số chính xác')
  else:
    break

if guess == secret:
  print('làm tốt lắm')
else:
  print('con số đúng là' + secret)