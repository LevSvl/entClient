import sys
import os.path  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QLabel,QLineEdit,QMainWindow,QApplication,QListWidget,QListWidgetItem
import configparser
import main_menu
import movement
import settings
import input_dict

class Main_menu(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        self.game_button.clicked.connect(self.open_game_code)
        self.settings_button.clicked.connect(self.open_settings)
        self.exit_button.clicked.connect(self.close)

    def open_settings(self):
        self.form = Settings()
        self.form.show()
        self.close()
   
    def open_game_code(self):
        self.close()
        movement.start_game()

class Settings(QtWidgets.QMainWindow, settings.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ingame_menu_close_button.clicked.connect(self.leave_to_main)
        config_path = "config.ini"
        config = configparser.ConfigParser()
        config.read(config_path)
        map = dict(config.items("Controls"))
        self.info_label.setText(f"{map}")

    def leave_to_main(self):
        self.form = Main_menu()
        self.form.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Main_menu()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    config_path = "config.ini"
    config = configparser.ConfigParser()
    if os.path.exists(config_path):
        controls_check(config,config_path)
    else:
        createConfig(config,config_path)
        controls_check(config,config_path)
    app.exec_()  # и запускаем приложение
 
def createConfig(config,config_path):
    config.add_section("Controls")
    config.set("Controls", "move_left", "a")
    config.set("Controls", "move_right", "d") 
    config.set("Controls","pause","p")  
    with open(config_path, "w") as config_file:
        config.write(config_file)

def controls_check(config,config_path):
        config.read(config_path)
        map = dict(config.items("Controls"))
        print(map)

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()