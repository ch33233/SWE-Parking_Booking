class Display:  # Display class 생성

    def __init__(self, page): # Display할 page 생성

        self.dataList = ''
        self.page = page


    def getRequest(self, req): # req로 page세팅

        self.page = req

        print("set page based on req")

        return self.page


    def setDataList(self): # DB에서 요청된 data가져와 저장
        
        dataList = ''
        print("Search data matching the request in DB")

        self.dataList = dataList

        return self.dataList


    def render(self): # page display

        print(self.page + self.dataList) # dataList가 있는 page를 출력


t = Display("testPage") #display할 testPage 생성

t.getRequest("url")  # page 세팅

print(t)

t.setDataList("input dataList1") # dataList 입력

t.render() # 입력된 page와 dataList로 display

print(t)