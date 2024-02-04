"""input_map = {'move left': "a",'move right': "d"}
keyboard_encryption={'a':97, 'd':100}
map={}
for key in input_map:
    new_value=input_map[key]
    map[key]=keyboard_encryption[new_value]
print(map)"""
import configparser
config_path = "config.ini"
config = configparser.ConfigParser()
def controls_get(config,config_path):
    keyboard_encryption={'a':97, 'd':100, 'p':112}
    map={}
    config.read(config_path)
    input_map = dict(config.items("Controls"))
    for key in input_map:
        new_value=input_map[key]
        map[key]=keyboard_encryption[new_value]
    print(map)
    return(map)

if __name__=="__main__":
    controls_get(config,config_path)