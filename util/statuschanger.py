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

def StatusChanger(token, Status):
    CustomStatus = {"custom_status": {"text": Status}} #{"text": Status, "emoji_name": "☢"} if you want to add an emoji to the status
    try:
        requests.patch("https://discord.com/api/v9/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=CustomStatus)
        print_slow(f"\n{Fore.GREEN}Statut changer avec succès en {Fore.WHITE}{Status}{Fore.GREEN} ")
    except Exception as e:
        print(f"{Fore.RED}Erreur:\n{e}\nS'est produit lors de la tentative de modification de l'état :/")
    print("Entrez n'importe quoi pour continuer. . . ", end="")
    input()
    ix.main()