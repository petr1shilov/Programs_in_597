import pygame
import random
import sqlite3
from nps_car import Nps_car
from naruto import Naruto

name_of_player = input('Hello, enter you name : ')
# name_of_player = 'Petya'

pygame.init()


#glob par
W = 800
H = 650
xn_1 = W//2
y = H // 2
hp = 3

connect = sqlite3.connect('data_score.db')
cursor = connect.cursor()
connect.commit()


# скорость передвижения 
fps = pygame.time.Clock()

# запуск дисплея 
sc = pygame.display.set_mode((W,H))

#download img
sound = pygame.mixer.music.load('hit_sound.mp3')
# sound = pygame.mixer.Sound(r'C:/Progi/saske_come_back/hit_sound.mp3')


road = pygame.image.load('road.png' )


nar = pygame.image.load('naruto.png' )
nar = pygame.transform.scale(nar, (40, 45))
nar_hp = pygame.transform.scale(nar, (20, 23))


car1 = pygame.image.load('car_up.png')
car1 = pygame.transform.scale(car1, (60, 110))

car2 = pygame.image.load('car_down.png')
car2 = pygame.transform.scale(car2,(60,110))

car_hp = pygame.image.load('HP_car.png')
car_hp = pygame.transform.scale(car_hp,(120,100))
car_hp = pygame.transform.rotate(car_hp,90)

def  show_hp():
    global hp
    show = 0 
    x =20
    while show != hp :
        sc.blit(nar_hp,(x,10))
        x += 30
        show += 1

#отрисовка дороги и наруто 
def draw_sc(): 
    sc.blit(road, (0,0))
   

# def print_on_dp (text, size):
#     font_to_sc = pygame.font.Font(None, size)
#     text1 = font_to_sc.render(text, True, (0, 0, 0))
    

#машины нпс            
car01 = Nps_car(200, 0, W, H, car1)
car02 = Nps_car(340, H, W, H, car2)
car_hp_01 = Nps_car(W//10, H//2, W, H, car_hp)
naruten = Naruto(xn_1, y, H, W, nar)


font = pygame.font.Font(None, 20)

#main cerc
while hp != 0:

    #проверка на нажатие клавиш крестик 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    
    #передвижение нпс
    if car01.move_up() == 1:
        car01.y = H
        car01.x = random.randint(0, 1) * 250 + 200

    if car02.move_down() == 1:
        car02.y = 0
        car02.x = random.randint(0, 1) * 250 + 340
        # car01.x = 100
    
    
    naruten.move_naruto()

    #dinamic paramerts    
    yn_1 = naruten.y 
    yn_4 = naruten.y + 45
    yc1_1 = car01.y
    yc1_3 = car01.y + 110
    yc2_1 = car02.y
    yc2_3 = car02.y + 110
   
     
    xn_4 = naruten.x + 40
    xc1_1 = car01.x
    xc1_2 = car01.x + 60
    xc2_1 = car02.x
    xc2_2 = car02.x + 60

    #car01
    if yn_4 >= yc1_1 and yn_1 <= yc1_3:
        if  xn_4 >= xc1_1 and naruten.x <= xc1_2:
            car01.y = 1000
            hp -= 1
            pygame.mixer.music.play(1,0.0)
            # sound.play()
            pygame.time.delay(100)
            print('hit')
       
               
    #car02
    if yn_1 <= yc2_3 and yn_4 >= yc2_1  :
        if  xn_4 >= xc2_1 and naruten.x <= xc2_2:
            car02.y = 1000
            hp -= 1
            pygame.mixer.music.play(1,0.0)
            pygame.time.delay(100) 
            print('hit')
     
    
    r = pygame.time.get_ticks()
    score = 'time score:' + str(r/1000) + 'sec'
    score_for_db = r / 1000
    text = font.render(score,True,[255,0,0])
    #draw
    draw_sc() 
    show_hp()
    naruten.draw_nar(sc) 
    # hp1 = font.render(hp,True[0,0,0])
    # sc.blit(hp,[30,20])
    sc.blit(text,(10,100))   
    car01.draw(sc)
    car02.draw(sc)
    car_hp_01.draw(sc)
    pygame.display.update()  
    fps.tick(60)   

sc.fill((255, 0, 0))
text = font.render(score,True,[0,0,0])
sc.blit(text, (W // 2 - 300, H // 2))
pygame.display.update()
pygame.time.delay(3000)
print(score)
cursor.execute(f"INSERT INTO players VALUES('{name_of_player}','{score_for_db}')")
connect.commit()
connect.close()