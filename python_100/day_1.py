# 求水仙花数
# 过整除和求模运算分别找出了一个三位数的个位、十位和百位，

for num in range(100,1000):
  low = num % 10
  mid = num // 10 % 10
  high = num // 100
  if num == low**3 + mid**3 + high**3:
    print(num)



# 实现正整数的反转

num = int(input("输入正整数"))
reversed_num = 0
while num!=0:
  reversed_num = reversed_num*10 + num%10
  num = num // 10
print(reversed_num)


# 百钱买百鸡

for x in range(0,20):
  for y in range(0,33):
    z = 100 - x -y
    if 5*x + 3*y + z/3 == 100:
      print("公鸡{}只，母鸡{}只，小鸡{}只".format(x,y,z))


def foo():
  a = 100
  def bar():
    nonlocal a # 使用nonlocal对嵌套域的变量值进行修改
    a = 200
  bar()
  print(a)
if __name__ == "__main__":
  foo()


import os
import time
content = '北京欢迎你为你开天辟地…………'
while True:
  # 清理屏幕上的输出
  os.system('cls')  # os.system('clear')
  print(content)
  # 休眠200毫秒
  time.sleep(0.2)
  content = content[1:] + content[0]