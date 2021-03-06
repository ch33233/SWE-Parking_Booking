# Android Parking Booking System.지도에서_주차장 찾기  
### REQ - User Story	
TEAM: 9 in SWE, CAUCSE 2021. Mapping part 

|identifier|User Story|Size|   
|----|----------------|----|  
|REQ-1|사용자로서 자신의 위치에서 주차장으로 가는 길을 확인한다.|5|  
|REQ-2|사용자로서 주차장의 위치를 누르면 주차장의 간략한 정보와 예약하기 버튼이 표시한다.|2|  
|REQ-3|사용자로서 로그인되어있으면 로그아웃, 로그아웃 되어있으면 로그인을 할 수 있다.|2|  
|REQ-4|사용자로서 로그인 버튼을 누르면 계정과 비밀번호를 입력하는 페이지로 이동한다.|2|  
|REQ-5|사용자로서 나의 개인정보 결제 정보, 이름, 전화번호, 차 번호가 표시되는 개인정보 페이지로 이동한다.|1|  
|REQ-6|사용자로서 피드백 버튼을 누르면 제목과 내용을 적을 수 있는 별도의 페이지로 이동한다.|1|  
|REQ-7|사용자로서 피드백 페이지에서 보내기 버튼을 누르면 피드백이 보내지면서 지도 페이지로 돌아온다.|1|  
|REQ-8|관리자로서 관리자는 관리자용 계정을 통해 로그인을하면 관리 페이지로 넘어간다.|2|  
|REQ-9|관리자로서 관리 페이지에서 피드벡 확인을 누르면 피드벡 제목이 표시된 페이지로 넘어간다.|2|  
|REQ-10|관리자로서 관리 페이지에서 영업 스케줄 버튼을 누르면 달력이 있는 페이지로 넘어가고 달력에서 비운영 날짜와 시간을 선택할 수 있다.|3|  
|REQ-11|사용자로서 로그인 화면에서 회원가입 버튼을 누르면 개인 정보로 회원가입을 할 수 있는 페이지로 넘어간다.|2|    
  
  
* * * 
### User Case  

|UserCase|UserCaseName|Description|   
|--------|------------|-----------|  
|UC-1|주차장이 표시된 지도|주차장 위치를 지도에 표시해준다|  
|UC-2|로그인 버튼|ID 와 PW 를 입력하는 페이지로 이동시켜준다|  
|UC-3|개인정보 확인 버튼|개인 정보를 확인할 수 있는 페이지로 이동시켜준다|   
|UC-4|피드백 버튼|피드백을 보낼 수 있는 페이지로 이동시켜준다|  
|UC-5|관리 버튼 |관리자로만 접근할 수 있으며 관리 페이지로 이동시켜준다|  
|UC-6|로그아웃 버튼|현재 접속 중인 계정에서 로그아웃 할 수 있다|  
|UC-7|영업 스케줄 선택|영업을 하지 않을 날을 달력 형식의 UI에서 선택할 수 있다|  
|UC-8|피드백 확인 버튼|User들이 제출한 피드벡을 확인할 수 있는 페이지로 이동한다| 
|UC-9|회원가입 버튼|개인정보로 회원가입을 할 수 있는 페이지로 이동한다|  

  
  * * * 
### Use Case Diagram

![UseCase](https://user-images.githubusercontent.com/49308460/114367015-fadbe400-9bb6-11eb-9ed3-87747ede0550.png)


* * * 
### Traceabitility matrix between User Case And Requirement  
  
|REQ|PW|UC1|UC2|UC3|UC4|UC5|UC6|UC7|UC8|UC9|    
|---|--|---|---|---|---|---|---|---|---|---|      
|REQ - 1|5|O|---|---|---|---|---|---|---|---|      
|REQ - 2|2|O|---|---|---|---|---|---|---|---|      
|REQ - 3|2|---|O|---|---|---|O|---|---|---|      
|REQ - 4|2|---|O|---|---|---|---|---|---|---|      
|REQ - 5|1|---|---|O|---|---|---|---|---|---|      
|REQ - 6|1|---|---|---|O|---|---|---|---|---|      
|REQ - 7|1|---|---|---|O|---|---|---|---|---|      
|REQ - 8|2|---|---|---|---|O|---|---|---|---|      
|REQ - 9|2|---|---|---|---|O|---|---|O|---|      
|REQ - 10|3|---|---|---|---|O|---|O|---|---|  
|REQ - 11|2|---|---|---|---|---|---|---|---|O|      

|Max PW|5|2|1|1|3|2|3|2|2|      
|------|---|---|---|---|---|---|---|---|---|      
|Total PW|7|4|1|2|7|2|3|2|2|        
  
  
* * * 

### Domain Model about Use Cases  

#### Use case 1

![UC1](./Image/UC1.png)  

#### Use case 2

![UC2](./Image/UC2.png)  

#### Use case 3

![UC3](./Image/UC3.png)  

#### Use case 4

![UC4](./Image/UC4.png)  

#### Use case 5  

![UC5](./Image/UC5.png)  

#### Use case 6  

![UC6](./Image/UC6.png)  

#### Use case 7  

![UC7](./Image/UC7.png)  

##### Use case 8  

![UC8](./Image/UC8.png)  
#### Use case 9

![UC9](./Image/UC9.png)  

* * * 

### User Interface Example  

### Before LogIn  

![BeforeLogIn](./Image/BeforeLogIn.png)
* * * 

### After LogIn (User)

![AfterLogInUser](./Image/AfterLogInUser.png)
* * * 

### After LogIn (관리자)

![AfterLogIn](./Image/AfterLogIn.png)
* * * 

### LogIn Page  

![LogInPage](./Image/LogInPage.png)
* * * 
   
