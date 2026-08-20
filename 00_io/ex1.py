# 입출력

a = input()
print(a, end="")
print(type(a))
print(a,type(a),sep=",")

a = int(a)
print(a,type(a), sep=",")

a = int(input())
print(a, type(a))

b = float(input())
print(b,type(b))

# 정수 2개 출력
# 100
# 200
a = int(input())
b = int(input())
print(a,b)

a = input().split()
print(a, type(a))

# map
a,b,c = map(int,input().split())
print(a, b,c)

a = list(map(int,input().split()))
print(a,type(a))