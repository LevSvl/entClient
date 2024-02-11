import pygame 
from pygame import font 
import configparser
import random 
import win32
from win32 import win32gui
import input_dict
#объявление всех используемых библиотек
pygame.init()
pygame.display.init()
font.init()
pygame.mixer.init()
#переменные файла config
config_path = "config.ini"
config = configparser.ConfigParser()
#переменные fps
config_fps = input_dict.get_fps(config,config_path)
fps = int(config_fps["fps"])
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
#переменные управления
map=input_dict.get_controls_encrypted(config,config_path)
ingame_map=input_dict.get_controls_notencrypted(config,config_path)
#переменные цветов
color = (255,255,255)  
color_light = (170,170,170)   
color_dark = (100,100,100)   
#переменные шрифтов 
bigfont = pygame.font.SysFont('Corbel',40)
smallfont = pygame.font.SysFont('Corbel',35)  
ingame_bigfont = pygame.font.SysFont('Corbel',30)
ingame_smallfont = pygame.font.SysFont('Corbel',25)
#переменные звука
sound1 = pygame.mixer.Sound('main_menu.wav')
sound2 = pygame.mixer.Sound('background.wav')

def points_counting(screen,score):
    if score==None:
        score= 0 
    text_surface = ingame_bigfont.render(f"Счёт: {score}", True, (0, 0, 0))
    screen.blit(text_surface, (screen_width-(screen_width-200),screen_height-(screen_height-600)))
    
def open_ingame_menu(info):
    active = 0
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        #распаковка массива
        game_screen = info[0]
        buttons_coord = info[1]
        buttons_text = info[2]
        back_to_game_button = buttons_coord[0]
        settings_button = buttons_coord[1]
        to_main_menu_button = buttons_coord[2]
        settings_back_button = buttons_coord[3]
        #game_screen, координаты кнопок, текст кнопок, мышь
        panel=pygame.Surface((panel_width, panel_height))# размер окна
        panel.fill((60,25,60))#цвет окна
        panel.set_alpha(255)#прозрачность 0-255 (прозрачный-непрозрачный)
        game_screen.blit(panel,(screen_width/2-panel_width/2,screen_height/2-panel_height/2))#координаты окна
        text = 'INGAME MENU'
        a = ingame_bigfont.render(text, 1, (0, 0, 255))# первый аргумент- текст, второй - сглаживание, третий(вторая пара скобок) - код цвета текста
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  
                #кнопка вернуться в игру 
                if back_to_game_button[0] <= mouse[0] <= back_to_game_button[2] and back_to_game_button[1] <= mouse[1] <= back_to_game_button[3]:
                    running = False
                #кнопка настройки
                if settings_button[0] <= mouse[0] <= settings_button[2] and settings_button[1] <= mouse[1] <= settings_button[3]:
                    buttons_coord = []
                    buttons_coord.append(back_to_game_button)
                    buttons_coord.append(settings_button)
                    buttons_coord.append(to_main_menu_button)
                    buttons_coord.append(settings_back_button)
                    info = []
                    info.append(game_screen)
                    info.append(buttons_coord)
                    info.append(buttons_text)
                    open_ingame_settings(info)
                    running = False
                #кнопка выйти в главное меню
                if to_main_menu_button[0] <= mouse[0] <= to_main_menu_button[2] and to_main_menu_button[1] <= mouse[1] <= to_main_menu_button[3]:
                    sound2.stop()
                    main_menu_start()
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
    return active

def open_ingame_settings(info):
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        #распаковка массива
        game_screen = info[0]
        buttons_coord = info[1]
        buttons_text = info[2]
        back_to_game_button = buttons_coord[0]
        settings_button = buttons_coord[1]
        to_main_menu_button = buttons_coord[2]
        settings_back_button = buttons_coord[3]
        #game_screen, buttons_coord, buttons_text, mouse
        panel=pygame.Surface((panel_width, panel_height))# размер окна
        panel.fill((60,25,60))#цвет окна
        panel.set_alpha(255)#прозрачность 0-255 (прозрачный-непрозрачный)
        game_screen.blit(panel,(screen_width/2-panel_width/2,screen_height/2-panel_height/2))#координаты окна
        text = 'SETTINGS'
        a = ingame_bigfont.render(text, 1, (0, 0, 255))# первый аргумент- текст, второй - сглаживание, третий(вторая пара скобок) - код цвета текста
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #обработка кнопки вернуться во внутриигровое меню
                if settings_back_button[0] <= mouse[0] <= settings_back_button[2] and settings_back_button[1] <= mouse[1] <= settings_back_button[3]:
                    running = False
        if settings_back_button[0] <= mouse[0] <= settings_back_button[2] and settings_back_button[1] <= mouse[1] <= settings_back_button[3]:  #смена подсветки при наведении мыши
            pygame.draw.rect(game_screen,color_light,[settings_back_button[0],settings_back_button[1],ingame_button_width,ingame_button_height])  
        else:  #подсветка без наведенной мыши
            pygame.draw.rect(game_screen,color_dark,[settings_back_button[0],settings_back_button[1],ingame_button_width,ingame_button_height])
        game_screen.blit(a, (screen_width/2-95,screen_height/2-120))
        game_screen.blit(buttons_text[3] , (to_main_menu_button[0]+10,to_main_menu_button[1]+5))
        i=0
        for key in map:
            i+=1
            repaired_key=f'{key}'.replace('_',' ').capitalize()#преобразование отображения ключа: move_left -> Move left
            b = ingame_smallfont.render(f'{repaired_key}:   {ingame_map[key]}', 1, (0, 0, 255))
            game_screen.blit(b, (back_to_game_button[0]+10,back_to_game_button[1]+20*i))
        pygame.display.flip() # Обновляем экран для появления вышенаписанного
    buttons_coord = []
    buttons_coord.append(back_to_game_button)
    buttons_coord.append(settings_button)
    buttons_coord.append(to_main_menu_button)
    buttons_coord.append(settings_back_button)
    info = []
    info.append(game_screen)
    info.append(buttons_coord)
    info.append(buttons_text)
    open_ingame_menu(info)

def show_pause(info):
    font.init()
    game_screen = info[0]
    text = 'PAUSE'
    a = ingame_bigfont.render(text, 1, (255, 255, 255),(0, 0, 255)) # первый аргумент- текст, второй - сглаживание, третий - код цвета текста, четвертый- код цвета фона
    game_screen.blit(a, (screen_width-200,screen_height-(screen_height-600)))
    pygame.display.flip()

def open_settings(info):
    running = True
    while running:
        screen = info[0]
        panel=pygame.Surface((panel_width, panel_height))# размер окна
        panel.fill((60,25,60))#цвет окна
        panel.set_alpha(255)#прозрачность 0-255 (прозрачный-непрозрачный)
        screen.blit(panel,(screen_width/2-panel_width/2,screen_height/2-panel_height/2))#координаты окна
        text = 'SETTINGS'
        a = ingame_bigfont.render(text, 1, (0, 0, 255))# первый аргумент- текст, второй - сглаживание, третий(вторая пара скобок) - код цвета текста
        settings_back_button = [screen_width/2-menu_button_width/2,screen_height/2+menu_button_height,screen_width/2+menu_button_width/2,screen_height/2+menu_button_height*2]
        button_text = smallfont.render('Back ' , True , color)
        mouse = pygame.mouse.get_pos() #(x,y) координаты мыши
        for event in pygame.event.get():     
            #проверка, куда нажала мышь:  
            if event.type == pygame.MOUSEBUTTONDOWN: 
                #кнопка start 
                if settings_back_button[0] <= mouse[0] <= settings_back_button[2] and settings_back_button[1] <= mouse[1] <= settings_back_button[3]:
                    running = False
        if settings_back_button[0] <= mouse[0] <= settings_back_button[2] and settings_back_button[1] <= mouse[1] <= settings_back_button[3]:  #смена подсветки при наведении мыши
            pygame.draw.rect(screen,color_light,[settings_back_button[0],settings_back_button[1],menu_button_width,menu_button_height])  
        else:  #подсветка без наведенной мыши
            pygame.draw.rect(screen,color_dark,[settings_back_button[0],settings_back_button[1],menu_button_width,menu_button_height])  
        screen.blit(a, (screen_width/2-menu_button_width/2+5,screen_height/2-120))
        screen.blit(button_text , (settings_back_button[0]+40,settings_back_button[1]+5))
        i=0
        for key in map:
            i+=1
            repaired_key=f'{key}'.replace('_',' ').capitalize()#преобразование отображения ключа: move_left -> Move left
            b = ingame_smallfont.render(f'{repaired_key}:   {ingame_map[key]}', 1, (0, 0, 255))
            screen.blit(b, (settings_back_button[0]+10,settings_back_button[1]-150+20*i))
        pygame.display.flip()

def open_game():
    pygame.init()
    game_screen = pygame.display.set_mode((screen_width, screen_height),pygame.NOFRAME)
    pygame.display.set_caption("Драматическое столкновение")
    sound2.play(-1)
    # характеристики окружности и прямоугольника
    bomb = pygame.image.load('bomb.png')
    bomb = pygame.transform.scale(bomb, (25, 25))
    chest = pygame.image.load('chest.png')
    chest = pygame.transform.scale(chest,(25,25))
    ship = pygame.image.load('ship.png')
    ship = pygame.transform.scale(ship,(150,100))
    ocean = pygame.image.load('ocean.png')
    ocean = pygame.transform.scale(ocean,(screen_width,screen_height))
    circle_radius = 10
    rect_width = 100
    rect_height = 50
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)
    ship_pos = [screen_width // 2, screen_height - rect_height*10]
    positions = []
    npc_speed = 2
    player_speed = 2
    #счет
    score = 0
    #переменные внутригровых меню
    buttons_text=[ingame_smallfont.render('Back to game' , True , color),ingame_smallfont.render('Settings' , True , color),ingame_smallfont.render('To main menu' , True , color),ingame_smallfont.render('Back' , True , color)]
    #координаты кнопок [первые два значения - левый верхний угол, остальные- правый нижний угол ]
    back_to_game_button = [screen_width/2-ingame_button_width/2,screen_height/2-ingame_button_height*2,screen_width/2+ingame_button_width/2,screen_height/2-ingame_button_height]
    settings_button = [screen_width/2-ingame_button_width/2,screen_height/2-ingame_button_height/2,screen_width/2+ingame_button_width/2,screen_height/2+ingame_button_height/2]
    to_main_menu_button = [screen_width/2-ingame_button_width/2,screen_height/2+ingame_button_height,screen_width/2+ingame_button_width/2,screen_height/2+ingame_button_height*2]
    settings_back_button = [screen_width/2-ingame_button_width/2,screen_height/2+ingame_button_height,screen_width/2+ingame_button_width/2,screen_height/2+ingame_button_height*2]
    #переменные паузы
    active,pause,inactive=0,1,1
    state=active    #переменная паузы
    ingame_menu=inactive   #переменная внутриигрового меню
    ingame_menu_settings = inactive #переменная раздела настроек внутриигрового меню
    running=True    #переменная главного цикла
    while running:
        #проверка, свёрнуто ли окно
        wnd = win32gui.FindWindow(None,"Драматическое столкновение")
        if (wnd == win32gui.GetForegroundWindow()):
            #не свёрнуто, ничего не происходит
            pass
        else:
            #свёрнуто, игра ставится на паузу
            state=pause
            info=[game_screen]
            show_pause(info)
        #обработка кнопок вызова паузы и внутриигрового меню
        for event in pygame.event.get():
            #нажатие клавиши
            if event.type == pygame.KEYDOWN:
                #нажатие 'p'
                if event.key == pygame.K_p:    
                    if state == pause:
                        if ingame_menu==inactive:
                            state=active
                    else:
                        state=pause
                        info=[game_screen]
                        show_pause(info)
                #нажатие 'Escape'
                if event.key == pygame.K_ESCAPE:
                    pygame.mouse.set_visible(True)
                    #если до нажатия игра была на паузе
                    if state==pause:
                        buttons_coord = []
                        buttons_coord.append(back_to_game_button)
                        buttons_coord.append(settings_button)
                        buttons_coord.append(to_main_menu_button)
                        buttons_coord.append(settings_back_button)
                        info = []
                        info.append(game_screen)
                        info.append(buttons_coord)
                        info.append(buttons_text)
                        state = open_ingame_menu(info)
                    #если игра не была на паузе до нажатия
                    else:
                        state=pause
                        buttons_coord = []
                        buttons_coord.append(back_to_game_button)
                        buttons_coord.append(settings_button)
                        buttons_coord.append(to_main_menu_button)
                        buttons_coord.append(settings_back_button)
                        info = []
                        info.append(game_screen)
                        info.append(buttons_coord)
                        info.append(buttons_text)
                        state = open_ingame_menu(info)
        #код обеспечения движения объектов
        if state == active:#проверка переменной паузы
            pygame.mouse.set_visible(False) #убирает курсор мыши в игре
            #управление движением
            key = pygame.key.get_pressed()
            if key[map['move_left']]:
                ship_pos[0] -= player_speed
            if key[map['move_right']]:
                ship_pos[0] += player_speed
            if key[map['move_up']]:
                ship_pos[1] -= player_speed
            if key[map['move_down']]:
                ship_pos[1] += player_speed
            # движение падающих объектов
            for i in range(len(positions)):
                positions[i][1] +=npc_speed
            # создание падающих объектов
            if random.random() < 0.02:
                x = random.randint(0, screen_width)
                num = random.randint(1, 10)
                #разделение падающих объектов на полезные и вредные False - вредные(окружности) true - полезные(треугольники)
                if num % 2 == 0:
                    positions.append([x, 0, False])
                else:
                    positions.append([x, 0, True])
            # проверка столкновений с игроком
            for pos in positions:
                distance_x = abs(pos[0] - ship_pos[0])
                distance_y = abs(pos[1] - ship_pos[1])
                if pos[2]:
                    if distance_x < (rect_width/2 + circle_radius) and distance_y < (rect_height/2 + circle_radius):
                        score += 1
                        positions.remove(pos)
                else:
                    if distance_x < (rect_width/2 + circle_radius) and distance_y < (rect_height/2 + circle_radius):
                        score  -= 1
                        positions.remove(pos)
            # убираем падающие объекты за пределами окна
            positions = [pos for pos in positions if pos[1] < screen_height]
            #заполняем фон 
            game_screen.blit(ocean,(0,0))
            #отрисовка падающих объектов
            for pos in positions:
                if pos[2]:
                    #pygame.draw.polygon(game_screen, (0, 0, 255), [[pos[0], pos[1]-10], [pos[0]+10, pos[1]+10], [pos[0]-10, pos[1]+10]])
                    game_screen.blit(chest,(pos[0],pos[1]))
                else:
                    #pygame.draw.circle(game_screen, (255, 0, 0), pos[:2], circle_radius)
                    game_screen.blit(bomb, (pos[0],pos[1]))
            #отрисовка игрока
            game_screen.blit(ship, (ship_pos[0],ship_pos[1]))
            #учет и вывод очков
            points_counting(game_screen,score)
            #вызываем всё вышеуказанное
            pygame.display.update()
            pygame.time.Clock().tick(fps)  

def main_menu_start():
    sound1.play(-1)
    hand = pygame.SYSTEM_CURSOR_HAND 
    pygame.mouse.set_cursor(hand)
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
                    sound1.stop()
                    open_game()
                #кнопка settings
                if settings_button[0] <= mouse[0] <= settings_button[2] and settings_button[1] <= mouse[1] <= settings_button[3]:
                    info = []
                    info.append(screen)
                    open_settings(info)
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