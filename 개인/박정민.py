import pygame


# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [640, 480]   # size변수는 창의 크기를 리스트 형태로 저장한 것

# screen변수 저장 #그리기 단계에 screen변수에 그림 집어 넣을 예정
screen = pygame.display.set_mode(size)

title = "icreamgame"   # 제목 표시줄 설정
pygame.display.set_caption(title)   # 창의 크기와 제목 저장

# 3. 게임 내 필요한 설정 - 여러 변수들 지정
clock = pygame.time.Clock()  # 시계를 설정하여 나중에 FPS기능 이용

counter, text = 180, '180'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    #screen.size((40, 30))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)


class obj:
    def __init__(self):  # __init__은 클래스를 선언했을 때 실행되는 함수  #반드시 필요한 변수를 이 함수 안에 넣어줘야 함
        self.x = 0  # self에 들어가는 객체의 x, y 변수가 생김
        self.y = 0

    def put_img(self, address):  # 이미지 불러오는 기능 함수
        if address[-3] == "png":
            self.img = pygame.image.load(address).convert_alpha()  # 이미지 불러옴
        else:
            self.img = pygame.image.load(address)  # 이미지 불러옴
            # 확장자가 jpg면 pygame.image.load()에서 끝내지만 확장자가 png라면 .convert_alpha()를 덧붙여야 함

            # 이미지 크기 받아오기  # 두가지 값이 튜플형태로 나오기 때문에 결과값이 각각의 변수에 저장됨.
            self.sx, self.sy = self.img.get_size()

    def change_size(self, sx, sy):  # 이미지 사이즈 조절
        self.img = pygame.transform.scale(
            self.img, (sx, sy))   # 이미지변수설정 #이미지사이즈지정
        # pygame.transform.scale(이미지파일변수, (가로크기, 세로크기)) 함수를 이용해서 그림사이즈바꾸기
        # 화면에 표현하려면 그리기 단계에서 screen.blit(이미지파일변수, (0, 0)) 함수 이용해서 화면에 나타내기
        # 그런데 클래스니까 i1.show() 이렇게 하면 한번에 표시
        self_sx, self_sy = self.img.get_size()  # 크기 바뀐거 업데이트

    def show(self):
        screen.blit(self.img, (self.x, self.y))  # 화면에 나타내기


i1 = obj()
i1.put_img("C:\\gameproject\\first.png")
i1.change_size(110, 110)
i1.x = round(size[0]/2 - 270)   # size[0]=640  #중앙에 오고 싶으면 /2   # round는 반올림 함수
# size[1]=480    #조금 위로 올리려면 - 원하는 만큼의 숫자 -i1_sy(아이스크림의 가로길이만큼 빼주어 화면으로 올라오게 한다.)
i1.y = size[1] - 120
# 그리기 단계에서 screen.blit(이미지변수명, (변수명_x, 변수명_y)) 함수를 통해 화면에 나타내기
# 그런데 클래스니까 i1.show() 이렇게 하면 한번에 표시

i2 = obj()
i2.put_img("C:\\gameproject\\second.png")
i2.change_size(110, 110)
i2.x = round(size[0]/2 - 125)
i2.y = size[1] - 120

i3 = obj()
i3.put_img("C:\\gameproject\\thrid.png")
i3.change_size(110, 110)
i3.x = round(size[0]/2) + 13
i3.y = size[1] - 120

i4 = obj()
i4.put_img("C:\\gameproject\\forth.png")
i4.change_size(110, 110)
i4.x = round(size[0]/2) + 165
i4.y = size[1] - 120

i5 = obj()
i5.put_img("C:\\gameproject\\sixth.png")
i5.change_size(110, 110)
i5.x = round(size[0]/2 - 270)
i5.y = size[1] - 235

i6 = obj()
i6.put_img("C:\\gameproject\\seventh.png")
i6.change_size(110, 110)
i6.x = round(size[0]/2 - 125)
i6.y = size[1] - 235

i7 = obj()
i7.put_img("C:\\gameproject\\nine.png")
i7.change_size(110, 110)
i7.x = round(size[0]/2) + 13
i7.y = size[1] - 235

i8 = obj()
i8.put_img("C:\\gameproject\\ten.png")
i8.change_size(110, 110)
i8.x = round(size[0]/2) + 165
i8.y = size[1] - 235


black = (0, 0, 0)
white = (255, 255, 255)
k = 0

# 4. 메인 이벤트
# 반복문(while문) 형태로 코드 구성 - 시간의 따른 사진 변화로 동영상처럼 보이게 게임 구성하기 위함
SB = 0
while SB == 0:

    # 4-1. FPS 설정(frame per second)
    # 1초에 이미지를 몇번 업데이트할꺼냐, 높을수록 부드럽게 작동하지만 많은 계산 필요
    clock.tick(60)  # 1초에 while문 60번 반복

    # 4-2. 각종 입력 감지   #  그외는 무시하고 게임 캐릭터를 움직이기 위한 키에 대한 작업
    # 동작이 여러개가 누를 수 있으니까 for문으로 구성 - 리스트 형태로 이 함수에 저장되어 하나씩 뽑아 확인, 동작
    for event in pygame.event.get():    # pygame.event.get() 이 함수는 실시간으로 키보드나 마우스의 동작을 받음
        if event.type == pygame.QUIT:
            SB = 1

    # 4-3. 입력, 시간에 따른 변화   # 그 변화를 코드로 집어넣음
    k += 1  # while문이 돌아갈때 마다 k증가

    # 4-4. 그리기(변화 반영)    # 변화가 반영된 후 배경화면, 캐릭터나 지형 등 화면 상에 보이는 것들 그리기
    screen.fill(white)
    i1.show()
    i2.show()
    i3.show()
    i4.show()
    i5.show()
    i6.show()
    i7.show()
    i8.show()

    #screen.blit(i1, (i1_x, i1_y))
    # blit함수에 들어가는 위치는 이미지의 왼쪽 위의 모서리이기 때문에 이미지를 원하는 위치에 놓으려면, 이미지의 크기만큼 값을 보정해야 함.
    # i1_sx, i1_sy = i1.get_size()를 통해 이미지의 크기를 받아올 수 있음

    # # 4-5. 업데이트
    pygame.display.flip()

# 5. 게임 종료 코드 입력
pygame.quit()
#활동량 채우기
