class Identify:  # identify class 사용자 기준 class 생성

    def __init__(self, name): # data type생성 자료형의 따라 갈림

        self.data = 0
        self.name = name
        print("A Data of",name, "has been called.")

    def addData(self, amount): # data 추가 자료형은 일단 int형 기준

        self.data += amount

        print("You have added", amount, "data.")

        return self.data


    def deleteData(self, amount): # data 삭제

        self.data -= amount

        print("You have deleted", amount, "data.")

        return self.data
    
    def __add__(self, other): #data 비교
        if self.name==other.name:
            print("data is added to {0} for {1}".format(self.data+other.data ,self.name) ,end='')
            return True # DB connect에서 data비교후 boolean 형태로 반환 
        else:
            print("The data is not matched.",end='')
            return False # DB connect에서 data비교후 boolean 형태로 반환

    def __str__(self): # data의 표시 외부에 나타낼 data를 직간접적으로 표현
        
        print("The data of {1} is {0}.".format(self.data,self.name) ,end='')
        return ""

a = Identify("Time") # time이라는 data의 생성

a.addData(30)  # data의 추가

print(a) 

a.addData(30) # 동일

print(a)

a.deleteData(50) # data의 제거

print(a)

b = Identify("money") # money라는 data의 추가

b.addData(2000)

infoisrevised=a+b

print(infoisrevised) # infoisrevise형태로 info control logger message creator로 전달
