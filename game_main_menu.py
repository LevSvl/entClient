import pygame 
from pygame import font 
import configparser 
import input_dict
font.init()
config_path = "config.ini"
config = configparser.ConfigParser()
#переменные окон
config_screen=input_dict.get_screen(config,config_path)
screen_width=int(config_screen["screen_width"])
screen_height=int(config_screen["screen_width"])
panel_width = int(config_screen["panel_width"])
panel_height = int(config_screen["panel_height"])
#переменные кнопок
config_button = input_dict.get_buttons(config,config_path)
menu_button_width = int(config_button["menu_button_width"])
menu_button_height = int(config_button["menu_button_height"])
ingame_button_width = int(config_button["ingame_button_width"])
ingame_button_height = int(config_button["ingame_button_height"])
#переменные цветов
color = (255,255,255)  
color_light = (170,170,170)   
color_dark = (100,100,100)   
#переменные шрифтов 
bigfont = pygame.font.SysFont('Corbel',40)
smallfont = pygame.font.SysFont('Corbel',35)  
ingame_bigfont = pygame.font.SysFont('Corbel',30)
ingame_smallfont = pygame.font.SysFont('Corbel',25)

def open_settings():
    print("Settings")
    
def open_game():
    game_screen = pygame.display.set_mode((screen_width, screen_height),pygame.NOFRAME)
    pygame.display.set_caption("Драматическое столкновение")
    # характеристики окружности и прямоугольника
    circle_pos = [screen_width/2, 50]
    circle_radius = 20
    rect_pos = [screen_width/2, screen_height/2]
    rect_width = 100
    rect_height = 50
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)
    speed = 5
    #переменные внутригровых меню
    buttons_text=[ingame_smallfont.render('Back to game' , True , color),ingame_smallfont.render('Settings' , True , color),ingame_smallfont.render('To main menu' , True , color)]
    #координаты кнопок [первые два значения - левый верхний угол, остальные- правый нижний угол ]
    to_main_menu_button = [screen_width/2-ingame_button_width/2,screen_height/2+ingame_button_height,screen_width/2+ingame_button_width/2,screen_height/2+ingame_button_height*2]
    settings_button = [screen_width/2-ingame_button_width/2,screen_height/2-ingame_button_height/2,screen_width/2+ingame_button_width/2,screen_height/2+ingame_button_height/2]
    back_to_game_button = [screen_width/2-ingame_button_width/2,screen_height/2-ingame_button_height*2,screen_width/2+ingame_button_width/2,screen_height/2-ingame_button_height]
    #переменные паузы
    active,pause,inactive=0,1,1
    state=active
    menu=inactive
    running=True
    while running:
        mouse = pygame.mouse.get_pos() #(x,y) координаты мыши
        for event in pygame.event.get():
            #нажатие клавиши
            if event.type == pygame.KEYDOWN:
                #нажатие 'p'
                if event.key == pygame.K_p:    
                    if state == pause:
                        if menu==inactive:
                            state=active
                    else:
                        state=pause
                        text = 'PAUSE'
                        a = ingame_bigfont.render(text, 1, (100, 100, 100),(0, 0, 255)) # первый аргумент- текст, второй - сглаживание, третий - код цвета текста, четвертый- код цвета фона
                        game_screen.blit(a, (screen_width-200,screen_height-(screen_height-600)))
                        pygame.display.flip()
                #нажатие 'Escape'
                if event.key == pygame.K_ESCAPE:
                    #если до нажатия игра была на паузе
                    if state==pause:
                        if menu==inactive: 
                            menu=active
                            panel=pygame.Surface((screen_width, screen_height))# размер окна
                            panel.fill((60,25,60))#цвет окна
                            panel.set_alpha(255)#прозрачность 0-255 (прозрачный-непрозрачный)
                            game_screen.blit(panel,(0,0))#координаты окна
                            text = 'Ingame Menu'
                            a = ingame_bigfont.render(text, 1, (0, 0, 255))# первый аргумент- текст, второй - сглаживание, третий(вторая пара скобок) - код цвета текста
                            game_screen.blit(a, (screen_width/2-60,screen_height/2-60))
                            pygame.display.flip() # Обновляем экран для появления вышенаписанного
                        else:
                            state=active
                            menu=inactive
                    #если игра не была на паузе до нажатия
                    else:
                        state=pause
                        menu=active
                        panel=pygame.Surface((panel_width, panel_height))# размер окна
                        panel.fill((60,25,60))#цвет окна
                        panel.set_alpha(255)#прозрачность 0-255 (прозрачный-непрозрачный)
                        game_screen.blit(panel,(screen_width/2-panel_width/2,screen_height/2-panel_height/2))#координаты окна
                        text = 'INGAME MENU'
                        a = ingame_bigfont.render(text, 1, (0, 0, 255))# первый аргумент- текст, второй - сглаживание, третий(вторая пара скобок) - код цвета текста
                        if back_to_game_button[0] <= mouse[0] <= back_to_game_button[2] and back_to_game_button[1] <= mouse[1] <= back_to_game_button[3]:  #смена подсветки при наведении мыши
                            pygame.draw.rect(game_screen,color_light,[back_to_game_button[0],back_to_game_button[1],ingame_button_width,ingame_button_height])  
                        else:  #подсветка без наведенной мыши
                            pygame.draw.rect(game_screen,color_dark,[back_to_game_button[0],back_to_game_button[1],ingame_button_width,ingame_button_height])                 
                        if settings_button[0] <= mouse[0] <= settings_button[2] and settings_button[1] <= mouse[1] <= settings_button[3]:  #смена подсветки при наведении мыши
                            pygame.draw.rect(game_screen,color_light,[settings_button[0],settings_button[1],ingame_button_width,ingame_button_height])  
                        else:  #подсветка без наведенной мыши
                            pygame.draw.rect(game_screen,color_dark,[settings_button[0],settings_button[1],ingame_button_width,ingame_button_height]) 
                        if to_main_menu_button[0] <= mouse[0] <= to_main_menu_button[2] and to_main_menu_button[1] <= mouse[1] <= to_main_menu_button[3]:  #смена подсветки при наведении мыши
                            pygame.draw.rect(game_screen,color_light,[to_main_menu_button[0],to_main_menu_button[1],ingame_button_width,ingame_button_height])  
                        else:  #подсветка без наведенной мыши
                            pygame.draw.rect(game_screen,color_dark,[to_main_menu_button[0],to_main_menu_button[1],ingame_button_width,ingame_button_height])
                        game_screen.blit(a, (screen_width/2-95,screen_height/2-120))
                        game_screen.blit(buttons_text[0] , (back_to_game_button[0]+20,back_to_game_button[1]+5))
                        game_screen.blit(buttons_text[1] , (settings_button[0]+40,settings_button[1]+5))
                        game_screen.blit(buttons_text[2] , (to_main_menu_button[0]+10,to_main_menu_button[1]+5))
                        pygame.display.flip() # Обновляем экран для появления вышенаписанного
            if event.type == pygame.MOUSEBUTTONDOWN:
                #кнопка вернуться в игру 
                if back_to_game_button[0] <= mouse[0] <= back_to_game_button[2] and back_to_game_button[1] <= mouse[1] <= back_to_game_button[3]:
                    state=active
                    menu=inactive
                #кнопка выйти в главное меню
                if to_main_menu_button[0] <= mouse[0] <= to_main_menu_button[2] and to_main_menu_button[1] <= mouse[1] <= to_main_menu_button[3]:
                    running=False
                        
        if state==active:
            # окружность движется вниз
            circle_pos[1] += speed

            # проверяем (используя формулу расстояния),
            # столкнулась ли окружность с прямоугольником
            circle_x = circle_pos[0]
            circle_y = circle_pos[1]
            rect_x = rect_pos[0]
            rect_y = rect_pos[1]
            distance_x = abs(circle_x - rect_x)
            distance_y = abs(circle_y - rect_y)
            if distance_x <= (rect_width/2 + circle_radius) and distance_y <= (rect_height/2 + circle_radius):
                circle_color = red # изменяем цвет фигур
                rect_color = green # в момент столкновения
            else:
                circle_color = green
                rect_color = black

            # рисуем окружность и прямоугольник на экране
            game_screen.fill((white))
            pygame.draw.circle(game_screen, circle_color, circle_pos, circle_radius)
            pygame.draw.rect(game_screen, rect_color, (rect_pos[0]-rect_width/2, rect_pos[1]-rect_height/2, rect_width, rect_height))

            pygame.display.update()

            # останавливаем движение окружности, если она
            # столкнулась с прямоугольником
            if circle_pos[1] + circle_radius >= rect_pos[1] - rect_height/2:
                speed = 0

            # задаем частоту обновления экрана
            pygame.time.Clock().tick(60)

def main_menu_start():
    pygame.init()  
    #переменные для создания экрана
    buttons_text=[smallfont.render('Start' , True , color),smallfont.render('Settings' , True , color),smallfont.render('Quit' , True , color)]
    screen = pygame.display.set_mode((screen_width, screen_height),pygame.NOFRAME)  
    pygame.display.set_caption('Own Game')
    running=True 
    while running:  
        screen.fill((60,25,60)) 
        mouse = pygame.mouse.get_pos() #(x,y) координаты мыши
        #координаты кнопок [первые два значения - левый верхний угол, остальные- правый нижний угол ]
        quit_button = [screen_width/2-70,screen_height/2+40,screen_width/2+70,screen_height/2+80]
        settings_button = [screen_width/2-70,screen_height/2-20,screen_width/2+70,screen_height/2+20]
        start_button = [screen_width/2-70,screen_height/2-80,screen_width/2+70,screen_height/2-40]
        for event in pygame.event.get():     
            if event.type == pygame.QUIT:  
                running= False
            #проверка, куда нажала мышь:  
            if event.type == pygame.MOUSEBUTTONDOWN: 
                #кнопка start 
                if start_button[0] <= mouse[0] <= start_button[2] and start_button[1] <= mouse[1] <= start_button[3]:
                    open_game()
                #кнопка settings
                if settings_button[0] <= mouse[0] <= settings_button[2] and settings_button[1] <= mouse[1] <= settings_button[3]:
                    open_settings()
                #кнопка quit
                if quit_button[0] <= mouse[0] <= quit_button[2] and quit_button[1] <= mouse[1] <= quit_button[3]:  
                    running=False  
        #смена подсветки кнопки при наведении мыши
        if start_button[0] <= mouse[0] <= start_button[2] and start_button[1] <= mouse[1] <= start_button[3]:  #смена подсветки при наведении мыши
            pygame.draw.rect(screen,color_light,[start_button[0],start_button[1],menu_button_width,menu_button_height])  
        else:  #подсветка без наведенной мыши
            pygame.draw.rect(screen,color_dark,[start_button[0],start_button[1],menu_button_width,menu_button_height])                 
        if settings_button[0] <= mouse[0] <= settings_button[2] and settings_button[1] <= mouse[1] <= settings_button[3]:  #смена подсветки при наведении мыши
            pygame.draw.rect(screen,color_light,[settings_button[0],settings_button[1],menu_button_width,menu_button_height])  
        else:  #подсветка без наведенной мыши
            pygame.draw.rect(screen,color_dark,[settings_button[0],settings_button[1],menu_button_width,menu_button_height]) 
        if quit_button[0] <= mouse[0] <= quit_button[2] and quit_button[1] <= mouse[1] <= quit_button[3]:  #смена подсветки при наведении мыши
            pygame.draw.rect(screen,color_light,[quit_button[0],quit_button[1],menu_button_width,menu_button_height])  
        else:  #подсветка без наведенной мыши
            pygame.draw.rect(screen,color_dark,[quit_button[0],quit_button[1],menu_button_width,menu_button_height])  
        #отображение текста на кнопках
        screen.blit(buttons_text[0] , (start_button[0]+40,start_button[1]+5))
        screen.blit(buttons_text[1] , (settings_button[0]+15,settings_button[1]+5))
        screen.blit(buttons_text[2] , (quit_button[0]+40,quit_button[1]+5))
        
        pygame.display.update()  

    pygame.quit()