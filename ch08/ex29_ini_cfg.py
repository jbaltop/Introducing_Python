# p252

import configparser

cfg = configparser.ConfigParser()

print(cfg.read("data/settings.cfg"))
print(cfg)
print(cfg["french"])
print(cfg["french"]["greeting"])
print(cfg["files"]["bin"])
