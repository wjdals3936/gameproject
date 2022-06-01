# 게임 종료 처리
# 성공 : 화면 내에 모든 버블이 사라지면 성공
# 실패 : 바닥에 어떤 정해진 높이보다 버블이 낮게 내려오면 실패
import time
import sys
import os
import random
import math
from turtle import width
import pygame

# button class


class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            screen.blit(img_in, (x, y))


def quitgame():
    pygame.quit()
    sys.exit()


def change_state(k):
    k = 1

# 버블 클래스 생성


class Bubble(pygame.sprite.Sprite):
    def __init__(self, image, color, position=(0, 0), row_idx=-1, col_idx=-1):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position)
        self.radius = 18
        self.row_idx = row_idx
        self.col_idx = col_idx

    def set_rect(self, position):
        self.rect = self.image.get_rect(center=position)

    def draw(self, screen, to_x=None):
        if to_x:
            screen.blit(self.image, (self.rect.x + to_x, self.rect.y))
        else:
            screen.blit(self.image, self.rect)

    def set_angle(self, angle):
        self.angle = angle
        self.rad_angle = math.radians(self.angle)

    def move(self):
        to_x = self.radius * math.cos(self.rad_angle)
        to_y = self.radius * math.sin(self.rad_angle) * -1

        self.rect.x += to_x
        self.rect.y += to_y

        if self.rect.left < 0 or self.rect.right > screen_width:
            self.set_angle(180 - self.angle)

    def set_map_index(self, row_idx, col_idx):
        self.row_idx = row_idx
        self.col_idx = col_idx

    def drop_downward(self, height):
        self.rect = self.image.get_rect(
            center=(self.rect.centerx, self.rect.centery + height))


# 버블 클래스 생성


class Bubble(pygame.sprite.Sprite):
    def __init__(self, image, color, position=(0, 0), row_idx=-1, col_idx=-1):  # 매소드정의
        super().__init__()  # 상속받은 부모 클래스의 init 매소드 호출
        self.image = image
        self.color = color
        # sprite를 상속받은 클래스는 image와 rect 무조건 필요함
        self.rect = image.get_rect(center=position)
        self.radius = 18  # 버블의 발사 속도 # 게임 진행 속도
        self.row_idx = row_idx  # 초기화해주기
        self.col_idx = col_idx  # 현재 버블이 맵 기준 어디에 있는지 알 수 있음

    def set_rect(self, position):
        self.rect = self.image.get_rect(center=position)

    # 화면에 나타내기
    def draw(self, screen, to_x=None):
        if to_x:  # 화면 흔들기
            screen.blit(self.image, (self.rect.x + to_x, self.rect.y))
        else:
            screen.blit(self.image, self.rect)

    # 각도 클래스 정의
    def set_angle(self, angle):
        self.angle = angle
        self.rad_angle = math.radians(self.angle)  # 60분법을 호도법으로 변환해줌

    # 버블의 움직임 설정(라디안이용)
    def move(self):
        to_x = self.radius * math.cos(self.rad_angle)  # x좌표로 이동하는 값(cos)
        # y좌표로 이동하는 값(sin) # 파이게임에서는 y가 밑으로 내려갈수록 +값
        to_y = self.radius * math.sin(self.rad_angle) * -1

        self.rect.x += to_x  # x로 to_x만큼 이동
        self.rect.y += to_y  # y로 to_y만큼 이동

        # 벽에 충돌시 버블 진행방향 설정
        if self.rect.left < 0 or self.rect.right > screen_width:  # 화면 왼쪽 경계를 벗어나거나 오른쪽 경계를 벗어나면
            self.set_angle(180 - self.angle)  # 180도에서 현재 방향을 뺀 각도로 튕겨나감

    def set_map_index(self, row_idx, col_idx):
        self.row_idx = row_idx
        self.col_idx = col_idx

    # 벽 내리는 함수 정의
    def drop_downward(self, height):
        self.rect = self.image.get_rect(
            center=(self.rect.centerx, self.rect.centery + height))

# 발사대 클래스 생성


class Pointer(pygame.sprite.Sprite):
    def __init__(self, image, position, angle):
        super().__init__()
        self.image = image  # 각도가 바뀔 때 마다 그 각도로 이미지가 업데이트됨
        self.rect = image.get_rect(center=position)
        self.angle = angle  # 회전
        self.original_image = image  # 항상 0도 # 각도를 계산 할 때 원본 이미지에서 계산되도록
        self.position = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # 회전
    def rotate(self, angle):
        self.angle += angle

        if self.angle > 170:  # 밑으로 회전하지 않게 범위 제한
            self.angle = 170
        elif self.angle < 10:
            self.angle = 10

        self.image = pygame.transform.rotozoom(
            self.original_image, self.angle, 1)  # 마지막 객체는 이미지 크기 배수를 의미
        # 이미지의 회전과 상관없이 발사대의 rect정보는 처음 지정한 중심좌표기준으로 그려짐
        self.rect = self.image.get_rect(center=self.position)

# 맵 만들기


def setup():
    global map  # 함수안에서 전역변수 만들때 global 사용
    # lv1
    map = [
        # ["R", "R", "Y", "Y", "B", "B", "G", "G"] = list("RRYYBBGG")
        list("RRYYBBGG"),
        list("RRYYBBG/"),  # / : 버블이 위치할 수 없는 곳
        list("BBGGRRYY"),
        list("BGGRRYY/"),
        list("........"),  # . : 비어 있는 곳
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........")  # 11번째 줄
    ]

    # lv2
    # map = [
    #     list("...YY..."),
    #     list("...G.../"),
    #     list("...R...."),
    #     list("...B.../"),
    #     list("...R...."),
    #     list("...G.../"),
    #     list("...P...."),
    #     list("...P.../"),
    #     list("........"),
    #     list("......./"),
    #     list("........")
    # ]

    # lv3
    # map = [
    #     list("G......G"),
    #     list("RGBYRGB/"),
    #     list("Y......Y"),
    #     list("BYRGBYR/"),
    #     list("...R...."),
    #     list("...G.../"),
    #     list("...R...."),
    #     list("......./"),
    #     list("........"),
    #     list("......./"),
    #     list("........")
    # ]

    # 버블 맵에 그리기

    # 맵 전달받기 # row_idx = 몇 번째 인덱스인지 , row = 한 줄씩 list 불러오기
    for row_idx, row in enumerate(map):
        # 한칸씩 받기 # col_idx = 한 줄 안에서 몇 번째인지,  col = 한줄 불러온 걸 한 칸씩 끊어서 받음
        for col_idx, col in enumerate(row):
            if col in [".", "/"]:  # 비어있는 공간은
                continue  # 버블을 만들지 않음
            position = get_bubble_position(row_idx, col_idx)  # 튜플 형태로 받아짐
            image = get_bubble_image(col)
            # 버블 객체(image, col....)를 통해 만들고 클래스 객체를 버블그룹에 추가
            bubble_group.add(Bubble(image, col, position, row_idx, col_idx))


def get_bubble_position(row_idx, col_idx):  # 맵의 좌표
    # 센터에 위치하기 위해 (BUBBLE_WIDTH // 2) 더해줌
    pos_x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
    # + wall_height 하는 이유는 벽이 내려온 길이 고려해서
    pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2) + wall_height
    if row_idx % 2 == 1:  # 홀수 번째 줄이라면
        pos_x += CELL_SIZE // 2  # x죄표 오른쪽으로 CELL_SIZE // 2 만큼 이동
    return pos_x, pos_y


def get_bubble_image(color):
    if color == "R":
        return bubble_images[0]
    elif color == "Y":
        return bubble_images[1]
    elif color == "B":
        return bubble_images[2]
    elif color == "G":
        return bubble_images[3]
    # elif color == "P":
        return bubble_images[4]
    else:  # BLACK
        return bubble_images[-1]  # 리스트의 맨마지막 값 반환을 의미


def prepare_bubbles():
    global curr_bubble, next_bubble  # 전역변수
    if next_bubble:
        curr_bubble = next_bubble
    else:
        curr_bubble = create_bubble()  # 랜덤으로 새 버블 만들기

    curr_bubble.set_rect((screen_width // 2, 624))  # 이번에 쏠 버블 위치좌표
    next_bubble = create_bubble()
    next_bubble.set_rect((screen_width // 4, 668))  # 다음에 쏠 버블 위치좌표


def create_bubble():
    color = get_random_bubble_color()
    image = get_bubble_image(color)
    return Bubble(image, color)


def get_random_bubble_color():
    colors = []  # 색깔 후보를 리스트로 만듦
    for row in map:  # 맵에 있는 row를 가져옴
        for col in row:  # 그 row에 있는 색깔들을 가져옴
            # 리스트에 없는 색깔 or 버블이 존재하지 않으면
            if col not in colors and col not in [".", "/"]:
                colors.append(col)  # 리스트의 색이 추가됨
    return random.choice(colors)  # 리스트에 있는 것중 하나 선택


def process_collision():
    global curr_bubble, fire, curr_fire_count  # 전역함수
    hit_bubble = pygame.sprite.spritecollideany(
        curr_bubble, bubble_group, pygame.sprite.collide_mask)  # 충돌한 버블 = hit_bubble
    # 투명한 영역 제외하고 진짜 이미지가 있는 영역에 하나라도 충돌되면 hit_bubble이 받음
    if hit_bubble or curr_bubble.rect.top <= wall_height:  # 버블이 충돌 했거나 천장or 벽에 닿았을 때 화면을 벗어나지 않게 설정
        # 튜플형태 # curr_bubble의 중심의 (x, y) # x,y를 별도의 변수로 활용하고 싶으면 * 붙이기_언패킹
        row_idx, col_idx = get_map_index(*curr_bubble.rect.center)
        place_bubble(curr_bubble, row_idx, col_idx)  # curr_bubble,버블 위치 시키기
        remove_adjacent_bubbles(
            row_idx, col_idx, curr_bubble.color)  # 인접한 버블 제거
        curr_bubble = None
        fire = False  # 발사여부
        curr_fire_count -= 1  # 충돌 후에 발사 기회 한번씩 뺴기


def get_map_index(x, y):
    # - wall_height 하는 이유는 벽이 내려온 길이 고려해서
    row_idx = (y - wall_height) // CELL_SIZE
    col_idx = x // CELL_SIZE
    if row_idx % 2 == 1:  # 홀수번째 줄이면
        # 현재 버블을 왼쪽으로 절반 이동 후에 계산됨
        col_idx = (x - (CELL_SIZE // 2)) // CELL_SIZE
        if col_idx < 0:
            col_idx = 0
        elif col_idx > MAP_COLUMN_COUNT - 2:
            col_idx = MAP_COLUMN_COUNT - 2
    return row_idx, col_idx


def place_bubble(bubble, row_idx, col_idx):
    map[row_idx][col_idx] = bubble.color  # 충돌하는 현재  버블의 색깔 받기
    position = get_bubble_position(row_idx, col_idx)
    bubble.set_rect(position)  # 버블위치 update
    bubble.set_map_index(row_idx, col_idx)
    bubble_group.add(bubble)  # 버블 그룸에 추가_충돌처리비교를 위해


def remove_adjacent_bubbles(row_idx, col_idx, color):
    visited.clear()  # 방문기록 초기화
    visit(row_idx, col_idx, color)
    if len(visited) >= 3:  # 같은색깔 버블이 3개 이상이면
        remove_visited_bubbles()  # 방문한 버블 삭제
        remove_hanging_bubbles()  # 붕 떠있는 버블 삭제


def visit(row_idx, col_idx, color=None):
    # 맵의 범위를 벗어나는지 확인
    if row_idx < 0 or row_idx >= MAP_ROW_COUNT or col_idx < 0 or col_idx >= MAP_COLUMN_COUNT:
        return
    # 현재 Cell 의 색상이 color 와 같은지 확인
    if color and map[row_idx][col_idx] != color:
        return
    # 빈 공간이거나, 버블이 존재할 수 없는 위치인지 확인
    if map[row_idx][col_idx] in [".", "/"]:
        return
    # 이미 방문했는지 여부 확인
    if (row_idx, col_idx) in visited:
        return
    # 방문 처리
    visited.append((row_idx, col_idx))  # 튜플형태

    # 버블이 방문할 수 있는 위치의 경우의 수
    rows = [0, -1, -1, 0, 1, 1]
    cols = [-1, -1, 0, 1, 0, -1]
    if row_idx % 2 == 1:  # 홀수번째 줄일 때
        rows = [0, -1, -1, 0, 1, 1]
        cols = [-1, 0, 1, 1, 1, 0]

    for i in range(len(rows)):  # 재귀함수 # 버블 움직임 가능한 경우 다 방문하는 함수
        visit(row_idx + rows[i], col_idx + cols[i], color)


def remove_visited_bubbles():
    bubbles_to_remove = [b for b in bubble_group if (
        b.row_idx, b.col_idx) in visited]  # 버블 그룸에서 가져와 방문한 리스트에 있는 지 받아옴
    for bubble in bubbles_to_remove:  # 방문한 적 있으면 삭제
        map[bubble.row_idx][bubble.col_idx] = "."  # 삭제
        bubble_group.remove(bubble)  # 현재 버블 초기화


def remove_not_visited_bubbles():  # 붕 떠있는 버블 삭제
    bubbles_to_remove = [b for b in bubble_group if (
        b.row_idx, b.col_idx) not in visited]
    for bubble in bubbles_to_remove:
        map[bubble.row_idx][bubble.col_idx] = "."
        bubble_group.remove(bubble)


def remove_hanging_bubbles():
    visited.clear()  # 초기화 먼저 해줌
    for col_idx in range(MAP_COLUMN_COUNT):
        if map[0][col_idx] != ".":  # 비어있지 않으면
            visit(0, col_idx)  # 방문, 색깔은 무시
    remove_not_visited_bubbles()


def draw_bubbles():  # 발사 횟수가 줄어들을수록 화면 흔들리기
    to_x = None
    if curr_fire_count == 2:  # 기회 2번 남으면
        to_x = random.randint(0, 2) - 1  # -1 ~ 1 # 약간 흔들기
    elif curr_fire_count == 1:
        to_x = random.randint(0, 8) - 4  # -4 ~ 4 # 많이 흔들기

    for bubble in bubble_group:
        bubble.draw(screen, to_x)


def drop_wall():  # 벽이미지 좌표 변경
    global wall_height, curr_fire_count
    wall_height += CELL_SIZE  # 셀 사이즈 만큼 떨어짐
    for bubble in bubble_group:
        bubble.drop_downward(CELL_SIZE)
    curr_fire_count = FIRE_COUNT  # 7번


def get_lowest_bubble_bottom():
    bubble_bottoms = [
        bubble.rect.bottom for bubble in bubble_group]  # 가장 밑에 있는 버블
    return max(bubble_bottoms)  # 리스트 안의 가장 큰 값


def change_bubble_image(image):  # 게임 종료 시 버블색 바꾸기
    for bubble in bubble_group:
        bubble.image = image


def display_game_over():  # 게임 종료 시 문구 설정
    # 화면 중앙에 위치
    screen.blit(ending_Img, (0, 0))


pygame.init()
screen_width = 448  # 길이
screen_height = 720  # 높이
screen = pygame.display.set_mode(
    (screen_width, screen_height))  # 튜플형태로 화면 설정, screen으로 받음
pygame.display.set_caption("Puzzle Bobble")  # 게임제목
clock = pygame.time.Clock()  # 변수 설정

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)  # 현재파일의경로(디렉토리)파악 #경로변수설정
# join을 써서 디렉토리+파일명경로를 합쳐서 이미지를 불러옴
background = pygame.image.load(os.path.join(current_path, "background1.png"))
# 벽 이미지 불러오기
wall = pygame.image.load(os.path.join(current_path, "wall.png"))

# 타이틀 이미지 불러오기
title = pygame.image.load(os.path.join(current_path, "title.png"))

# 종료 이미지 불러오기
ending_Img = pygame.image.load(os.path.join(current_path, "ending_img.png"))


# 시작화면 버튼
startImg = pygame.image.load(os.path.join(current_path, "starticon.png"))
quitImg = pygame.image.load(os.path.join(current_path, "quiticon.png"))
clickStartImg = pygame.image.load(
    os.path.join(current_path, "clickedStartIcon.png"))
clickQuitImg = pygame.image.load(
    os.path.join(current_path, "clickedQuitIcon.png"))


# 버블 이미지 불러오기
bubble_images = [  # 버블이 색깔이 다양하므로 리스트로 만듦
    # 투명도설정_버블간의 충돌시 이미지가 있는 동그란 부분을 기준으로 처리할 수 있음
    pygame.image.load(os.path.join(current_path, "red.png")).convert_alpha(),
    pygame.image.load(os.path.join(
        current_path, "yellow.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "bule.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "green.png")).convert_alpha(),
    #pygame.image.load(os.path.join(current_path, "purple.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "black.png")
                      ).convert_alpha()  # 게임종료시의 버블색깔
]


# 점수판 표시
# system_font = pygame.font.SysFont('verdanai', 30)  # 텍스트 객체 설정
#game_live = system_font.render("score : " + str(score_live), True, PINK, GRAY)
#game_live_rect = game_live.get_rect()
#game_live_rect.topleft = (10, 10)
#game_live = system_font.render("score : " + str(score_live), True, PINK, GRAY)

# 대기중인 버블 컵 이미지 불러오기
#nextcup_image = pygame.image.load(os.path.join(current_path, "nextcup.jpeg")).convert_alpha()
#nextcup_image = pygame.image.load("C:\project\\nextcup.jpeg").convert_alpha()
#nextcup = nextcup_image
# nextcup = pygame.transform.scale(nextcup, (40, 40))  # 사이즈 변환
# screen.blit(nextcup, (100, 680))  # 화면에 나타내기

# 발사대 이미지 불러오기
pointer_image = pygame.image.load(os.path.join(
    current_path, "conpointer.png")).convert_alpha()
# 발사대 클래스 객체 #발사대의 angle 90도로 위쪽을 보게 설정
pointer = Pointer(pointer_image, (screen_width // 2, 624), 90)

# 게임 관련 변수
CELL_SIZE = 56
BUBBLE_WIDTH = 56
BUBBLE_HEIGHT = 62
RED = (255, 0, 0)
WHITE = (255, 255, 255)
#PINK = (255, 51, 153)
#GRAY = (128, 128, 128)
MAP_ROW_COUNT = 11  # row 줄 기준 최대  갯수
MAP_COLUMN_COUNT = 8  # row 행 기준 최대 갯수
FIRE_COUNT = 7  # 쏠 수 있는 기회
# score_live = 0  # 초기 점수

# 발사대 관련 변수
# to_angle = 0 # 좌우로 움직일 각도 정보
to_angle_left = 0  # 왼쪽으로 움직일 각도 정보
to_angle_right = 0  # 오른쪽으로 움직일 각도 정보
angle_speed = 1.5  # 1.5 도씩 움직이게 됨

curr_bubble = None  # 이번에 쏠 버블
next_bubble = None  # 다음에 쏠 버블
fire = False  # 발사 여부
curr_fire_count = FIRE_COUNT
wall_height = 0  # 화면에 보여지는 벽의 높이_처음은 안보임

is_game_over = False  # 게임종료변수
game_font = pygame.font.SysFont("arialrounded", 40)  # 게임 종료 시 문구
game_result = None  # 게임 결과
game_state = False
global j
j = 2
change = 3

map = []  # 빈 리스트로 맵 선언
visited = []  # 버블이 방문한 위치 기록
bubble_group = pygame.sprite.Group()  # 전역함수
setup()  # setup 함수 호출

running = True  # 러닝변수가 ture일 동안 반복문이 계속 돌게됨
while running:
    clock.tick(60)  # (게임속도)FPS 60 으로 설정
    screen.fill((202, 228, 241))
    screen.blit(title, (0, 0))

    startButton = Button(startImg, 100, 600, 60, 20,
                         clickStartImg, 103, 603, None)

    quitButton = Button(quitImg, 300, 600, 60, 20,
                        clickQuitImg, 303, 603, quitgame)

    for event in pygame.event.get():  # 발생하는 모든 이벤트를 받음
        if event.type == pygame.QUIT:  # 종료버튼구현
            running = False

        if event.type == pygame.KEYDOWN:  # 어떤 키가 눌려졌을 때
            if event.key == pygame.K_LEFT:  # 왼쪽 화살표
                to_angle_left += angle_speed  # 발사대가 왼쪽으로 각도 변경
            elif event.key == pygame.K_RIGHT:  # 오른쪽 화살표
                to_angle_right -= angle_speed  # 발사대가 오른쪽으로 각도 변경
            elif event.key == pygame.K_SPACE:  # 스페이스키
                if curr_bubble and not fire:  # 쏠 버블이 있고 발사상태가 아닐 때
                    fire = True  # 발사처리
                    curr_bubble.set_angle(pointer.angle)

        if event.type == pygame.KEYUP:  # 어떤 키가 눌리지 않으면
            if event.key == pygame.K_LEFT:
                to_angle_left = 0
            elif event.key == pygame.K_RIGHT:
                to_angle_right = 0

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x = 100
    width = 60
    y = 600
    height = 20
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0]:
            time.sleep(1)
            change = 1

    if change == 1:
        game_state = True

    if game_state == True:
        if not curr_bubble:  # 지금 쏠 버블이 없으면
            prepare_bubbles()  # 버블을 준비해라

        if fire:  # 발사하면
            process_collision()  # 충돌 처리 함수

        if curr_fire_count == 0:  # 발사 기회가 0이면
            drop_wall()

# if process_collision():
#    print("충돌")
#   score_live = score_live + 2  # 버블 한개 당 2점

        if not bubble_group:
            game_result = "Mission Complete"  # 게임 성공 시 문구
            is_game_over = True  # 게임 성공 시
        elif get_lowest_bubble_bottom() > len(map) * CELL_SIZE:  # 가장 바닥에 있는 버블이 맵의 높이보다 커지면
            game_result = "Game Over"  # 게임 실패 시 문구
            is_game_over = True  # 게임 종료 처리
        # 게임 종료시 버블 이미지 리스트 가장 마지막 black으로 바꿈
            change_bubble_image(bubble_images[-1])

        screen.blit(background, (0, 0))  # 배경이미지 나타내기
    # bubble_group.draw(screen)
        screen.blit(wall, (0, wall_height - screen_height))

        draw_bubbles()
        pointer.rotate(to_angle_left + to_angle_right)
        pointer.draw(screen)
        if curr_bubble:
            if fire:
                curr_bubble.move()  # move 메소드
            curr_bubble.draw(screen)

        if next_bubble:
            next_bubble.draw(screen)

    # if next_bubble:
    #    nextcup.draw(screen)

        if is_game_over:  # 게임이 끝나는 조건에 도달하면
            display_game_over()  # 게임 문구 나타내기
            running = False

    pygame.display.update()  # 화면에 업데이트

pygame.time.delay(2000)  # 게임 종료시 2초 정도 딜레이 만들기
pygame.quit()
