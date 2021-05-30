class Time:
    def __init__(self, date, hour, rentHour):
      self.date = date
      self.hour = hour
      self.rentHour = rentHour

class DatabaseConnection: # 가상의 business hour를 가져온다고 가정
    def __init__(self):
        self.openHour = 9.00
        self.closeHour = 23.00

class ShowDisplay:
    def __init__(self, time): # data type생성 자료형의 따라 갈림
        self.time = time

    def post(self, time):
        print("입력하신 시간은 유효한 값입니다.")

class CheckTime:
    def __init__(self, time, parkingSlot): # data 추가 자료형은 일단 int형 기준
        self.isValid(time, parkingSlot)

    def isValid(self, time, parkingSlot): # data 삭제
        start = float(time.hour)
        end = start + float(time.rentHour)
        if start < parkingSlot.openHour or end > parkingSlot.closeHour:
            return 0
        else:
            return 1
            



# ==== Make a virtual Database ====
parkingSlot = DatabaseConnection()
print(parkingSlot.openHour, parkingSlot.closeHour)


# ==== input time ====
date = input("Input date : ")
time = input("Input time : ")
hour = input("Input rent hour : ")

NewTime = Time(date, time, hour)

if(not CheckTime(NewTime, parkingSlot)):
    print("invalid time, please choose time again data.")
else:
    print("valid time, next step..")

