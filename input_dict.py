import configparser
config_path = "config.ini"
config = configparser.ConfigParser()
def get_controls_encrypted(config,config_path):
    keyboard_encryption={'a':97, 'd':100,'w':119,'s':115, 'p':112}
    map={}
    config.read(config_path)
    input_map = dict(config.items("Controls"))
    for key in input_map:
        new_value=input_map[key]
        map[key]=keyboard_encryption[new_value]
    return(map)

def get_controls_notencrypted(config,config_path):
    config.read(config_path)
    input_map = dict(config.items("Controls"))
    return(input_map)

def get_screen(config,config_path):
    config.read(config_path)
    input_map = dict(config.items("Screen"))
    return(input_map)

def get_buttons(config,config_path):
    config.read(config_path)
    input_map = dict(config.items("Buttons"))
    return(input_map)