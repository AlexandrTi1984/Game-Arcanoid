
# Game Arkanoid  

Children's game Arkanoid written using "pgzero". 

🎮🕹


## Installation libraries:

```python
pip install pgzero
```
    
## Screenshots / Video

![App Screenshot](screenshot/pic1.gif)




## Usage/Examples

```python
import pgzrun
from pgzero.builtins import Actor, keyboard
import random

....
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
...
```
