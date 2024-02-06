import sys
import os.path  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel,QLineEdit,QWidget,QComboBox,QVBoxLayout
import configparser
import launcher_menu
import settings
import game_main_menu

config_path = "config.ini"
config = configparser.ConfigParser()

class Main_menu(QtWidgets.QMainWindow, launcher_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.game_button.clicked.connect(self.open_game_code)
        self.settings_button.clicked.connect(self.open_settings)
        self.exit_button.clicked.connect(self.close)

    def open_settings(self):
        self.form = Settings()
        self.form.show()
        self.close()
   
    def open_game_code(self):
        self.close()
        game_main_menu.main_menu_start()

class Settings(QtWidgets.QMainWindow, settings.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ingame_menu_close_button.clicked.connect(self.leave_to_main)
        config.read(config_path)
        control_map = dict(config.items("Controls"))
        screen_map = dict(config.items("Screen"))
        i=0
        #выведение информации об управлении 
        for key in control_map:
            i+=10
            repaired_key=f'{key}'.replace('_',' ').capitalize()
            self.key_label = QLabel(f'{repaired_key}', self) 
            self.key_label.setObjectName(f'{key}')
            self.key_label.setGeometry(QtCore.QRect(30, 30+i*2, 60, 60))
            self.key_value_label = QLabel(f'{control_map[key]}', self)
            self.key_value_label.setGeometry(QtCore.QRect(150, 30+i*2, 60, 60))
            self.key_value_label.setObjectName(f'{key}_value')
            self.key_input = QLineEdit(f'{control_map[key]}', self)
            self.key_input.setGeometry(QtCore.QRect(200, 50+i*2, 80, 20))
            self.key_input.textChanged.connect(self.settings_change)
            self.key_input.setObjectName(f'input_{key}')
        self.settings_label = QLabel("Настройки экрана:",self)
        self.settings_label.setGeometry(QtCore.QRect(30, self.key_input.y()+30, 120, 60))
        #создание dropdown меню для выбора разрешения экрана
        self.parameter_label = QLabel('Screen resolution',self)
        self.parameter_label.setGeometry(QtCore.QRect(self.settings_label.x(), self.settings_label.y()+40, 160, 30))
        self.combo =QComboBox(self)
        self.combo.addItem(f"{screen_map['screen_width']} x {screen_map['screen_height']}")
        if f"{screen_map['screen_width']}"=="1920":
            self.combo.addItem("640 x 480")
        else:
            self.combo.addItem("1920 x 1080")
        self.combo.setGeometry(self.parameter_label.x()+180, self.parameter_label.y(), 150, 30)
        self.combo.currentTextChanged.connect(self.settings_change)

    def settings_change(self):
        self.key_button = QtWidgets.QPushButton('Применить изменения',self)
        self.key_button.setGeometry(QtCore.QRect(self.parameter_label.x(), self.parameter_label.y()+40, 160, 30))
        self.key_button.clicked.connect(self.change_value)
        self.key_button.show()

    def change_value(self):
        for key in dict(config.items("Controls")):
            if key ==self.findChild(QLabel, f"{key}").text():
                new_value=self.findChild(QLineEdit, f"input_{key}").text()
                config.set("Controls",f"{key}",f"{new_value}")
                with open('config.ini', "w") as config_file:
                    config.write(config_file)
        new_resolution=self.combo.currentText()
        new_screen_width=new_resolution.split(' ')[0]
        new_screen_height = new_resolution.split(' ')[2]
        config.set("Screen","screen_width",f'{new_screen_width}')
        config.set("Screen","screen_height",f'{new_screen_height}')
        with open('config.ini', "w") as config_file:
            config.write(config_file)
        self.close()
        os.system('python launcher.py')


    def leave_to_main(self):
        self.form = Main_menu()
        self.form.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main_menu()
    window.show() 
    config_path = "config.ini"
    config = configparser.ConfigParser()
    if os.path.exists(config_path):
        pass
    else:
        createConfig(config,config_path)
    app.exec_()  # и запускаем приложение
 
def createConfig(config,config_path):
    config.add_section("Controls")
    config.add_section("Screen")
    config.set("Controls", "move_left", "a")
    config.set("Controls", "move_right", "d") 
    config.set("Screen", "screen_width", "1920")
    config.set("Screen", "screen_height", "1080") 
    with open(config_path, "w") as config_file:
        config.write(config_file)

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()