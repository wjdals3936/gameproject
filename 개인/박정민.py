import pygame

# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [640, 480]   # size변수는 창의 크기를 리스트 형태로 저장한 것

# screen변수 저장 #그리기 단계에 screen변수에 그림 집어 넣을 예정
screen = pygame.display.set_mode(size)

title = "My Game"   # 제목 표시줄 설정
pygame.display.set_caption(title)   # 창의 크기와 제목 저장

# 3. 게임 내 필요한 설정 - 여러 변수들 지정
clock = pygame.time.Clock()  # 시계를 설정하여 나중에 FPS기능 이용


i1 = pygame.image.load(
    "C:\\gameproject\\first.png").convert_alpha()  # 이미지 불러옴
# 확장자가 jpg면 pygame.image.load()에서 끝내지만 확장자가 png라면 .convert_alpha()를 덧붙여야 함

i1 = pygame.transform.scale(i1, (110, 110))  # 이미지변수설정 #이미지사이즈지정
# 화면에 표현하려면 그리기 단계에서 screen.blit(이미지파일변수, (0, 0)) 함수 이용해서 화면에 나타내기
# pygame.transform.scale(이미지파일변수, (가로크기, 세로크기)) 함수를 이용해서 그림사이즈바꾸기

i1_sx, i1_sy = i1.get_size()  # 두가지 값이 튜플형태로 나오기 때문에 결과값이 각각의 변수에 저장됨.
# size[0]=640  #중앙에 오고 싶으면 /2   # round는 반올림 함수
i1_x = round(size[0]/2 - 270)
# size[1]=480    #조금 위로 올리려면 - 원하는 만큼의 숫자 -i1_sy(아이스크림의 가로길이만큼 빼주어 화면으로 올라오게 한다.)
i1_y = size[1] - i1_sy - 20
# 그리기 단계에서 screen.blit(이미지변수명, (변수명_x, 변수명_y)) 함수를 통해 화면에 나타내기

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
    screen.blit(i1, (i1_x, i1_y))
    # blit함수에 들어가는 위치는 이미지의 왼쪽 위의 모서리이기 때문에 이미지를 원하는 위치에 놓으려면, 이미지의 크기만큼 값을 보정해야 함.
    # i1_sx, i1_sy = i1.get_size()를 통해 이미지의 크기를 받아올 수 있음

    # # 4-5. 업데이트
    pygame.display.flip()

# 5. 게임 종료 코드 입력
pygame.quit()
