import configparser
config_path = "config.ini"
config = configparser.ConfigParser()
def get_controls_encrypted(config,config_path):
    keyboard_encryption={'a':97,'b':98,'c':99, 'd':100,'e':101, 'f':102,'g':103,'h':104,'i':105,'j':106,'k':107,'l':108, 'm':109, 'n':110, 'o':111,'p':112,'q':113,'r':114, 's':115, 't':116, 'u':117,'v':118,'w':119,'x':120, 'y':121, 'z':122}
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

def get_fps(config,config_path):
    config.read(config_path)
    input_map = dict(config.items("FPS"))
    return input_map