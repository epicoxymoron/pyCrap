import configparser

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read("settings.cfg")
