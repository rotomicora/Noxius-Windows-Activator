import os, fade, time
from colorama import Fore

w = Fore.LIGHTWHITE_EX
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
b = Fore.LIGHTBLUE_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
black = Fore.LIGHTBLACK_EX

gui = """
          ╔══════════════════════════════════════════════════════╗
          ║         [!] projectnoxius.xyz/discord [!]            ║
          ╠══════════════════════════════════════════════════════╣
          ║          ╔╗╔ ╔═╗ ═╗╔═ ╦ ╦ ╦ ╔═╗                      ║
          ║          ║║║ ║ ║ ╔╩╚╗ ║ ║ ║ ╚═╗   rotomicora#0001    ║
          ║          ╝╚╝ ╚═╝ ╩  ╩ ╩ ╚═╝ ╚═╝                      ║
          ║    ╔════════════════════════════════════════════╗    ║
          ║ ╔══╝    [!] Noxius Windows 10 Activator [!]     ╚══╗ ║
          ╠═╝         [>] docs.projectnoxius.xyz [<]           ╚═╣
          ╚══════════════════════════════════════════════════════╝
"""

choices = """
               ╔═════════════════════════════════════════╗
               ║    [!] projectnoxius.xyz/discord [!]    ║
               ╠═════════════════════════════════════════╣
               ║                                         ║
               ║  [1] Windows 10 Home                    ║
               ║                                         ║
               ║  [2] Windows 10 Home N                  ║
               ║                                         ║
               ║  [3] Windows 10 Pro                     ║
               ║                                         ║
               ║  [4] Windows 10 Pro N                   ║
               ║                                         ║
               ║  [5] Windows 10 Enterprise              ║
               ║                                         ║
               ║  [6] Windows 10 Enterprise N            ║
               ║                                         ║
               ║  [7] Windows 10 Education               ║
               ║                                         ║
               ║  [8] Windows 10 Education N             ║
               ║                                         ║
               ╚═════════════════════════════════════════╝
"""
os.system("@mode con cols=80 lines=40")
def slowprint(msg):
    for char in msg:
        print(char, end="", flush=True)
        time.sleep(0.5/20)
    print()

faded_gui = fade.pinkred(gui)
faded_choices = fade.pinkred(choices)
def activate():
    os.system("title Noxius Windows 10 Activator - rotomicora#0001")
    os.system("cls")
    print(faded_gui)
    print(faded_choices)
    choices_ask = input(f"{m}[{w}>{m}] {black}Enter your {y}Windows 10 {black}Version -{m}>{y} ")
    if choices_ask == "1":
        os.system("title Activating Windows 10 Home - Noxius Windows Activator")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Activating {y}Windows 10 Home {black}...")
        os.system("slmgr //B /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr //B /skms kms8.msguides.com")
        os.system("slmgr //B /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Successfully {y}Activated {black}Windows 10 Home!")
        os.system("pause >nul")
    elif choices_ask == "2":
        os.system("title Activating Windows 10 Home N - Noxius Windows Activator")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Activating {y}Windows 10 Home N {black}...")
        os.system("slmgr //B /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM")
        os.system("slmgr //B /skms kms8.msguides.com")
        os.system("slmgr //B /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Successfully {y}Activated {black}Windows 10 Home N!")
        os.system("pause >nul")
    elif choices_ask == "3":
        os.system("title Activating Windows 10 Pro - Noxius Windows Activator")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Activating {y}Windows 10 Pro {black}...")
        os.system("slmgr //B /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr //B /skms kms8.msguides.com")
        os.system("slmgr //B /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Successfully {y}Activated {black}Windows 10 Pro!")
        os.system("pause >nul")
    elif choices_ask == "4":
        os.system("title Activating Windows 10 Pro N - Noxius Windows Activator")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Activating {y}Windows 10 Pro N {black}...")
        os.system("slmgr //B /ipk MH37W-N47XK-V7XM9-C7227-GCQG9")
        os.system("slmgr //B /skms kms8.msguides.com")
        os.system("slmgr //B /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Successfully {y}Activated {black}Windows 10 Pro N!")
        os.system("pause >nul")
    elif choices_ask == "5":
        os.system("title Activating Windows 10 Enterprise - Noxius Windows Activator")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Activating {y}Windows 10 Enterprise {black}...")
        os.system("slmgr //B /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr //B /skms kms8.msguides.com")
        os.system("slmgr //B /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Successfully {y}Activated {black}Windows 10 Enterprise!")
        os.system("pause >nul")
    elif choices_ask == "6":
        os.system("title Activating Windows 10 Enterprise N - Noxius Windows Activator")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Activating {y}Windows 10 Enterprise N {black}...")
        os.system("slmgr //B /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4")
        os.system("slmgr //B /skms kms8.msguides.com")
        os.system("slmgr //B /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Successfully {y}Activated {black}Windows 10 Enterprise N!")
        os.system("pause >nul")
    elif choices_ask == "7":
        os.system("title Activating Windows 10 Education - Noxius Windows Activator")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Activating {y}Windows 10 Education {black}...")
        os.system("slmgr //B /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
        os.system("slmgr //B /skms kms8.msguides.com")
        os.system("slmgr //B /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Successfully {y}Activated {black}Windows 10 Education!")
        os.system("pause >nul")
    elif choices_ask == "8":
        os.system("title Activating Windows 10 Education N - Noxius Windows Activator")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Activating {y}Windows 10 Education N {black}...")
        os.system("slmgr //B /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ")
        os.system("slmgr //B /skms kms8.msguides.com")
        os.system("slmgr //B /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}>{m}] {black}Successfully {y}Activated {black}Windows 10 Education N!")
        os.system("pause >nul")
    else:
        slowprint(f"{m}[{y}ERROR{m}] {r}Invalid Windows 10 Version!")
        activate()

activate()
