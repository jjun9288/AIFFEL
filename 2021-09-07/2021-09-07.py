'''
Computational Thinking vs Algorithm
현실에서 컴퓨터로 해결하려는 문제는 비정형화된 문제가 대부분이다. 이 비정형화된 문제를
컴퓨터로 해결하는 과정, 즉 문제를 이해하고 분해, 패턴 인식, 추상화, 알고리즘 작성까지를
Computational thinking이라고 한다.
'''

'''
- / vs //
파이썬에서 int를 / 연산자로 계산하면
5/2 = 2.5       4/2 = 2.0 즉 float로 나온다.
5//2 = 4//2 = 2로 int로 나오지만, 5.5//2 = 2.0 즉 float로 연산을하면 int가 아닌 float가 나온다.
'''
'''
- int(3.3) = 3

- 몫과 나머지 함께 구하기 : divmod(5,2)   >>>(2,1)

- 부호 붙이기   
x=-10
+x   >>> -10
-x   >>> 10
'''

'''
- input 함수는 항상 문자열로 받는다. 그래서 예를 들어
a = input(); b = input()
print(a+b)
여기에서 10, 20을 각각 입력하면 1020을 출력한다.

한 번에 여러개을 받을 수도 있따.
a,b = input().split()로 한 후 10 20을 입력하면 a=10, b=20이 할당된다.
a,b = map(int, input().split(','))  이렇게 하면 a=10, b=20을 int로 할당받을 수 있다.
'''

'''
- Object 와 Instance 
비슷하지만, 공장에서 옷을 찍어낸다 했을 때, 공장을 class, 나온 옷들 중 예를 들어
빨간색, 파란색, 노란색 옷 이들을 통틀어 object, 파란색 옷 하나를 instance라고 보면 된다.
'''

# Question1
a, b = 3, 3
(a is b) == (a == b)    #true

# Question2
a, b = [1,2,3], [1,2,3]
a is b      #false

# 값 여러개 출력하기
print(1, 2, 3)             #1 2 3
print(1, 2, 3, sep = ',')   #1,2,3
print(1, 2, 3, sep = ', ')  #1, 2, 3
# print는 '/n'이 생략되어 있다. print(1, end='')로 입력하면 줄을 건너 뛰지 않는다!

year = 2000; month = 10; day = 27; hour = 11; min = 43; sec = 59
print(year, month, day, sep = '/', end = ' ')
print(hour, min, sec, sep = ':')
