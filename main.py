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
          ║ ╔══╝     [!] Noxius Windows Activator [!]       ╚══╗ ║
          ╠═╝         [>] docs.projectnoxius.xyz [<]           ╚═╣
          ╚══════════════════════════════════════════════════════╝
"""

choices_windows = """
                ╔═════════════════════════════════════════╗
                ║    [!] projectnoxius.xyz/discord [!]    ║
                ╠═════════════════════════════════════════╣
                ║                                         ║
                ║            [1] Windows 7                ║
                ║                                         ║
                ║            [2] Windows 10               ║
                ║                                         ║
                ║            [3] Windows 11               ║
                ║                                         ║
                ╚═════════════════════════════════════════╝
"""

choices_win11 = """
               ╔═════════════════════════════════════════╗
               ║          [-] Windows 11 [-]             ║
               ╠═════════════════════════════════════════╣
               ║                                         ║
               ║                                         ║
               ║        [1] Windows 11 Home              ║
               ║                                         ║
               ║        [2] Windows 11 Pro               ║
               ║                                         ║
               ║        [3] Windows 11 Enterprise        ║
               ║                                         ║
               ║        [4] Windows 11 Education         ║
               ║                                         ║
               ║        [99] Back                        ║
               ║                                         ║
               ╚═════════════════════════════════════════╝
"""

choices_win10 = """
               ╔═════════════════════════════════════════╗
               ║          [-] Windows 10 [-]             ║
               ╠═════════════════════════════════════════╣
               ║                                         ║
               ║                                         ║
               ║        [1] Windows 10 Home              ║
               ║                                         ║
               ║        [2] Windows 10 Home N            ║
               ║                                         ║
               ║        [3] Windows 10 Pro               ║
               ║                                         ║
               ║        [4] Windows 10 Pro N             ║
               ║                                         ║
               ║        [5] Windows 10 Enterprise        ║
               ║                                         ║
               ║        [6] Windows 10 Enterprise N      ║
               ║                                         ║
               ║        [7] Windows 10 Education         ║
               ║                                         ║
               ║        [8] Windows 10 Education N       ║
               ║                                         ║
               ║        [99] Back                        ║
               ║                                         ║
               ╚═════════════════════════════════════════╝
"""

choices_win7 = """
                ╔═════════════════════════════════════════╗
                ║           [-] Windows 7 [-]             ║
                ╠═════════════════════════════════════════╣
                ║                                         ║
                ║                                         ║
                ║        [1] Windows 7 Home               ║
                ║                                         ║
                ║        [2] Windows 7 Pro                ║
                ║                                         ║
                ║        [3] Windows 7 Ultimate           ║
                ║                                         ║
                ║        [4] Windows 7 Enterprise         ║
                ║                                         ║
                ║        [99] Back                        ║
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
faded_choices = fade.pinkred(choices_windows)
faded_choices_win7 = fade.pinkred(choices_win7)
faded_choices_win11 = fade.pinkred(choices_win11)
faded_choices_win10 = fade.pinkred(choices_win10)

def choices():
    os.system("cls")
    os.system("title Noxius Windows Activator - rotomicora#0001")
    print(faded_gui)
    print(faded_choices)
    choices_ask = input(f"{m}[{w}>{m}] {black}Enter your {y}Windows {black}Version -{m}>{y} ")
    if choices_ask == "1":
        activate_win7()
    elif choices_ask == "2":
        activate_win10()
    elif choices_ask == "3":
        activate_win11()
    else:
        slowprint(f"{m}[{y}ERROR{m}] {r}Invalid {y}Windows {r}Version{m}!")
        choices()

def activate_win11():
    os.system("title Noxius Windows 11 Activator - rotomicora#0001")
    os.system("cls")
    print(faded_gui)
    print(faded_choices_win11)
    choices_ask = input(f"{m}[{w}>{m}] {black}Enter your {y}Windows 11 {black}Version -{m}>{y} ")
    if choices_ask == "1":
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{w}>{m}] {black}Activating {y}Windows 11 Home {black}Version{m}...")
        os.system("slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr.vbs /skms kms.lotro.cc")
        os.system("slmgr.vbs /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}OK{m}] {black}Successfully {y}Activated {black}Windows 11 Home{m}!")
        os.system("pause >nul")
    elif choices_ask == "2":
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{w}>{m}] {black}Activating {y}Windows 11 Pro {black}Version{m}...")
        os.system("slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr.vbs /skms kms.lotro.cc")
        os.system("slmgr.vbs /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}OK{m}] {black}Successfully {y}Activated {black}Windows 11 Pro{m}!")
        os.system("pause >nul")
    elif choices_ask == "3":
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{w}>{m}] {black}Activating {y}Windows 11 Pro for Workstations {black}Version{m}...")
        os.system("slmgr.vbs /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
        os.system("slmgr.vbs /skms kms.lotro.cc")
        os.system("slmgr.vbs /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}OK{m}] {black}Successfully {y}Activated {black}Windows 11 Pro for Workstations{m}!")
        os.system("pause >nul")
    elif choices_ask == "4":
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{w}>{m}] {black}Activating {y}Windows 11 Education {black}Version{m}...")
        os.system("slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43B8YKP-D69TJ")
        os.system("slmgr.vbs /skms kms.lotro.cc")
        os.system("slmgr.vbs /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}OK{m}] {black}Successfully {y}Activated {black}Windows 11 Education{m}!")
        os.system("pause >nul")
    elif choices_ask == "99":
        choices()
    else:
        slowprint(f"{m}[{y}ERROR{m}] {r}Invalid {y}Windows 11 {r}Version{m}!")
        activate_win11()


def activate_win7():
    os.system("title Noxius Windows 7 Activator - rotomicora#0001")
    os.system("cls")
    print(faded_gui)
    print(faded_choices_win7)
    choices_ask = input(f"{m}[{w}>{m}] {black}Enter your {y}Windows 7 {black}Version -{m}>{y} ")
    if choices_ask == "1":
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{w}>{m}] {black}Activating {y}Windows 7 Home {black}Version{m}...")
        os.system("slmgr /ipk ")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}OK{m}] {g}Windows 7 Home{y} Activated{m}!")
        os.system("pause >nul")
    elif choices_ask == "2":
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{w}>{m}] {black}Activating {y}Windows 7 Pro {black}Version{m}...")
        os.system("slmgr /ipk ")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}OK{m}] {g}Windows 7 Pro{y} Activated{m}!")
        os.system("pause >nul")
    elif choices_ask == "3":
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{w}>{m}] {black}Activating {y}Windows 7 Ultimate {black}Version{m}...")
        os.system("cscript //nologo c:\windows\system32\slmgr.vbs /ipk JHY4Q-NH85H-XK8VD-9Y68P-RFQ43 >nul")
        os.system("cscript //nologo c:\windows\system32\slmgr.vbs /ipk 45KI6-6GY6Y-KHXCQ-7DDY6-TF7CD >nul")
        os.system("cscript //nologo c:\windows\system32\slmgr.vbs /ipk LOHY7-P3ERP-ZXYCV-Q2H7C-FCGFR >nul")
        os.system("cscript //nologo c:\windows\system32\slmgr.vbs /ipk h6Y9R-C9PPG-3CWTY-Y4MPW-COI2J >nul")
        os.system("cscript //nologo c:\windows\system32\slmgr.vbs /ipk 65THD-F8XX6-YG69F-9M66D-MKSTY >nul")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}OK{m}] {g}Windows 7 Ultimate{y} Activated{m}!")
        os.system("pause >nul")
    elif choices_ask == "4":
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{w}>{m}] {black}Activating {y}Windows 7 Enterprise {black}Version{m}...")
        os.system("slmgr /ipk ")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
        os.system("cls")
        print(faded_gui)
        slowprint(f"{m}[{y}OK{m}] {g}Windows 7 Enterprise{y} Activated{m}!")
        os.system("pause >nul")
    elif choices_ask == "99":
        choices()
    else:
        slowprint(f"{m}[{y}ERROR{m}] {r}Invalid {y}Windows 7 {r}Version{m}!")
        activate_win7()

def activate_win10():
    os.system("title Noxius Windows 10 Activator - rotomicora#0001")
    os.system("cls")
    print(faded_gui)
    print(faded_choices_win10)
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
    elif choices_ask == "99":
        choices()
    else:
        slowprint(f"{m}[{y}ERROR{m}] {r}Invalid Windows 10 Version!")
        activate_win10()

choices()
