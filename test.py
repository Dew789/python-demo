import pygame
import time
import random

# 初始化
pygame.init()

# 游戏窗口大小
width, height = 480, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义颜色
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# 蛇的初始位置
snake_position = [[200, 200], [210, 200], [220, 200]]
# 蛇的初始移动方向
direction = 'RIGHT'
change_to = direction

# 食物的初始位置
food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawn = True

# 控制游戏速度
fps = pygame.time.Clock()

# 游戏结束标志
game_over = False

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            elif event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'

    # 根据方向改变蛇头位置
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snake_position[0][0] += 10
    if direction == 'LEFT':
        snake_position[0][0] -= 10
    if direction == 'UP':
        snake_position[0][1] -= 10
    if direction == 'DOWN':
        snake_position[0][1] += 10

    # 更新蛇的位置，判断游戏是否结束
    if snake_position[0][0] >= width or snake_position[0][0] < 0 or snake_position[0][1] >= height or snake_position[0][
        1] < 0:
        game_over = True
    for snake_body in snake_position[1:]:
        if snake_position[0][0] == snake_body[0] and snake_position[0][1] == snake_body[1]:
            game_over = True

    # 如果蛇头吃到食物，增长蛇的长度
    if snake_position[0][0] == food_position[0] and snake_position[0][1] == food_position[1]:
        food_spawn = False
    else:
        snake_position.pop()

    # 如果食物被吃掉，重新生成食物
    if not food_spawn:
        food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    food_spawn = True

    # 绘制游戏窗口
    window.fill(black)
    for pos in snake_position:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # 刷新游戏窗口
    pygame.display.update()

    # 控制游戏速度
    fps.tick(20)

# 游戏结束时退出窗口
pygame.quit()
