import pygame
import random
from PyQt5 import QtWidgets
import configparser
import input_dict
config_path = "config.ini"
config = configparser.ConfigParser()

from network import TCPClient


def start_game():
    net = TCPClient()
    with net:
        pygame.init()
        screen_width = 640
        screen_height = 480
        game_screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('По цветам')
        # переменные для паузы
        running, pause = 0,1
        state = running

        # цвета окружностей
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (100, 255, 0)
        blue = (0, 0, 255)
        black = (0, 0, 0)
        yellow = (255, 255, 0)

        # цвет, скорость, начальная позиция окружности
        circle_radius = 30
        circle_speed = 3

        start_pos1 = [screen_width//3, -circle_radius]
        start_pos2 = [screen_width - (screen_width//3), -circle_radius]
        # circle_color = random.choice([red, green, blue, yellow, white])
        circle_color = red
        circle_pos = start_pos1.copy()
        circle_landed = False


        circle_color2 = green 
        circle_pos2 = start_pos2.copy()
        circle_landed2 = False
        # Соединение с сервером
        # net.validate_start_params(circle_color)

        # список приземлившихся окружностей и их позиций
        landed_circles = []

        while True:
            for event in pygame.event.get():
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_p:    
                        if state == pause:
                            state= running
                        else:
                            state=pause
                    if event.key == pygame.K_ESCAPE:                      
                        if state == pause:
                            state=running
                        else:
                            state=pause
            if state==running:
                # если окружность не приземлилась
                if not circle_landed:
                    # меняем направление по нажатию клавиши
                    keys = pygame.key.get_pressed()
                    if keys[input_dict.controls_get(config,config_path)['move_left']]:
                        circle_pos[0] -= circle_speed
                    if keys[input_dict.controls_get(config,config_path)['move_right']]:
                        circle_pos[0] += circle_speed

                    # После вычисления позиции кружка полученная информация 
                    # Отправляется на сервер, сразу поле этого к серверу
                    # Выполняется запрос о позиции кружка второго игрока
                    net.send_pos_info(circle_pos[0])
                    # x = net.get_pos_info()

                    # проверяем, столкнулась ли окружность с другой приземлившейся окружностью
                    for landed_circle in landed_circles:
                        landed_rect = pygame.Rect(landed_circle[0]-circle_radius,
                                                   landed_circle[1]-circle_radius,
                                                     circle_radius*2, circle_radius*2)
                        
                        falling_rect = pygame.Rect(circle_pos[0]-circle_radius,
                                                    circle_pos[1]-circle_radius,
                                                    circle_radius*2, circle_radius*2)
                                                
                        if landed_rect.colliderect(falling_rect):
                            circle_landed = True
                            collision_x = circle_pos[0]
                            collision_y = landed_circle[1] - circle_radius*2
                            landed_circles.append((collision_x, collision_y, circle_color))
                            break
                                                    
                    # если окружность не столкнулась с другой приземлившейся окружностью
                    if not circle_landed:
                        # окружность движется вниз
                        circle_pos[1] += circle_speed
                        # проверяем, достигла ли окружность дна
                        if circle_pos[1] + circle_radius > screen_height:
                            circle_pos[1] = screen_height - circle_radius
                            circle_landed = True
                            # добавляем окружность и ее позицию в список приземлившихся окружностей
                            landed_circles.append((circle_pos[0], circle_pos[1], circle_color))
                     
                if circle_landed:
                    # если окружность приземлилась, задаем параметры новой
                    circle_pos = start_pos1.copy()
                    # circle_color = random.choice([red, green, blue, yellow, white])
                    circle_landed = False



                if not circle_landed2:
                    # меняем направление по нажатию клавиши
                    keys = pygame.key.get_pressed()
                    if keys[input_dict.controls_get(config,config_path)['move_left']]:
                        circle_pos[0] -= circle_speed
                    if keys[input_dict.controls_get(config,config_path)['move_right']]:
                        circle_pos[0] += circle_speed

                    # После вычисления позиции кружка полученная информация 
                    # Отправляется на сервер, сразу поле этого к серверу
                    # Выполняется запрос о позиции кружка второго игрока
                    net.send_pos_info(circle_pos[0])
                    # x = net.get_pos_info()

                    # проверяем, столкнулась ли окружность с другой приземлившейся окружностью
                    for landed_circle in landed_circles:
                        landed_rect = pygame.Rect(landed_circle[0]-circle_radius,
                                                   landed_circle[1]-circle_radius,
                                                     circle_radius*2, circle_radius*2)
                        
                                              
                        falling_rect2 = pygame.Rect(circle_pos2[0]-circle_radius,
                                                    circle_pos2[1]-circle_radius,
                                                    circle_radius*2, circle_radius*2) 
                        
                        if landed_rect.colliderect(falling_rect2):
                            circle_landed2 = True
                            collision_x2 = circle_pos2[0]
                            collision_y2 = landed_circle[1] - circle_radius*2
                            landed_circles.append((collision_x2, collision_y2, circle_color2))
                            break
                                                    

                    # если окружность не столкнулась с другой приземлившейся окружностью
                    if not circle_landed2:
                        # окружность движется вниз
                        circle_pos2[1] += circle_speed

                        # проверяем, достигла ли окружность дна
                        if circle_pos2[1] + circle_radius > screen_height:
                            circle_pos2[1] = screen_height - circle_radius
                            circle_landed2 = True
                            # добавляем окружность и ее позицию в список приземлившихся окружностей
                            landed_circles.append((circle_pos2[0], circle_pos2[1], circle_color2))                        

                if circle_landed2:
                    # если окружность приземлилась, задаем параметры новой
                    circle_pos2 = start_pos2.copy()
                    # circle_color = random.choice([red, green, blue, yellow, white])
                    circle_landed2 = False

                




                # рисуем окружности
                game_screen.fill(black)
                for landed_circle in landed_circles:
                    pygame.draw.circle(game_screen, landed_circle[2], (landed_circle[0], landed_circle[1]), circle_radius)

                # кружок текущего игрока    
                pygame.draw.circle(game_screen, circle_color, circle_pos, circle_radius)
                # кружок второго игрока
                pygame.draw.circle(game_screen, circle_color2, circle_pos2, circle_radius)
                # добавить кружки на окно
                pygame.display.update()

                # частота обновления экрана
                pygame.time.Clock().tick(60)

            elif state == pause:
                pass