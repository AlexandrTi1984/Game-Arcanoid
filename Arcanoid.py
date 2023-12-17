import pgzrun
from pgzero.builtins import Actor, keyboard
import random
import time
difficult = 1  # уровень сложности
my_score = 0   # начальный счет
bar_list =[]
ball_x_speed = -4
ball_y_speed = -4
ball_speed_txt = 1
# Создаем окно
TITLE = 'Арканоид'
WIDTH = 600
HEIGHT = 430
game_over = False

#Создание двигающейся панели и мячика
paddle = Actor("paddlered.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ballblue.png")
ball.y = 10
ball.x = random.randint(0,30)


'фуннкция рисования кирпичей'
def place_bars(x,y,image):
    bar_x = x
    bar_y = y
    for i in range(6):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bar_list.append(bar)

#выводим на экран
def draw():
    global my_score, ball_speed_txt, difficult
    # if game_over == False:
    if difficult == 1 :
        screen.blit("7.jpeg", (0, 0))
    elif difficult == 2:
        screen.blit("5.jpg", (0,0))
    elif difficult > 2:
        screen.blit("6.jpg", (0,0))
    screen.draw.text(f'Score   {my_score}', (10, 10),fontsize=30) # рисуем счет
    screen.draw.text(f'Speed ball X{ball_speed_txt}', (15, 30),fontsize=20) # рисуем счет
    screen.draw.text(f'Difficult {difficult}', (15, 45), fontsize=20)  # рисуем  сложность
    paddle.draw()
    ball.draw()
    for bar in bar_list:
        bar.draw()
    # else:
    #     screen.fill('blue')
    #     screen.draw.text(f'Game Over, You Score is {my_score}', (250, 150))
        # time.sleep(3)
        # exit()

def update ():
    global ball_x_speed, ball_y_speed, my_score, ball_speed_txt, difficult,coloured_box_list,paddle,ball
    if keyboard.left:
        paddle.x = paddle.x - random.randint(2,8)
        if paddle.x<55:   # чтоб ползунок за экран не выходил
            paddle.x = 55
    if keyboard.right:
        paddle.x = paddle.x + random.randint(2,8)
        if paddle.x>555:  # чтоб ползунок за экран не выходил
            paddle.x =553
    update_ball()
    for bar in bar_list:
        if ball.colliderect(bar):  #colliderect() — это встроенная функция, которая проверяет, столкнулись ли два объекта
            #print(f'Координаты мяча {ball.y} координаты кирпича {bar.y}')
            # Если выбит первый ряд - 1 очко, 2 ряд - 2, 3 ряд - 3 очка
            if bar.y == 100:
                my_score += 3
            elif bar.y == 150:
                my_score += 2
            elif bar.y == 200:
                my_score += 1
            bar_list.remove(bar)
            #print(my_score)
            ball_y_speed *= -1
            if len(bar_list) == 0: #Если все выбиты - рисуем заново, увеличиваем скорость мяча
                ball_x_speed += -2
                # рисуем другого цвета кирпичи, мяч и платформу
                coloured_box_list = ['element_blue_rectangle.png',
                                     'element_red_rectangle_glossy.png',
                                     'element_yellow_rectangle_glossy.png']
                ball.image = "ballgrey.png"
                paddle.image = 'paddleblu.png'
                ball_y_speed += -2
                ball_speed_txt += 1
                difficult += 1
                z=0
                for i in coloured_box_list:
                    place_bars(120, z+100, i)
                    z += 50
    if paddle.colliderect(ball):
        ball_y_speed *= -1
        rand = random.randint (0,1)
        if rand:
            ball_x_speed *= -1

def update_ball ():
    global ball_x_speed, ball_y_speed, game_over
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if ball.x >=WIDTH or ball.x <=0:
        ball_x_speed *=-1
    if ball.y >= HEIGHT:  # шарик упал ниже границы ползунка
       # game_over = True
        draw()
       # time.sleep(3)
        exit()
    if ball.y <=0 or ball.y >= HEIGHT:
        ball_y_speed *=-1

coloured_box_list=['element_grey_rectangle_glossy.png',
                   'element_green_rectangle_glossy.png',
                   'element_purple_rectangle_glossy.png']
x = 120
y = 100
for i in coloured_box_list:
    place_bars(x,y,i)
    y += 50
pgzrun.go()