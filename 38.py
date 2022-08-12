#매개변수 지정하여 호출하는 방법
def add(a,b):
    return a+b

result = add(b=3, a=7)
print(result)

#여러개의 입력값을 받는 함수를 만드는 방법
def add_many(*args):
    result = 0
    for i in args:
        result = result + i #*args에 입력받은 모든 값을 더한다.
    return result 

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
