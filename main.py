import os
os.system("cls")
import time
import sys
import importlib
from colorama import Fore, Style
print(f"""{Fore.BLUE}
                ╭─────────────────╮
                │{Fore.RED}BL{Fore.RED}OO{Fore.RED}DFETCH{Fore.GREEN} v0.0.1{Fore.BLUE}│
╔═════════════════════════════════════════════════╗
║   {Fore.RED}▄︻デ══━一{Fore.RED}💥{Fore.RED}───────────────────────────💢───{Fore.BLUE} ̗̀ {Fore.RED}⁍{Fore.BLUE}  
║\\         _____________________________         /║
║ \\       |  {Fore.GREEN}P A C K A G E  H U N T E R{Fore.BLUE} |       / ║
║  \\      |     {Fore.RED}I N  T H E  D A R K{Fore.BLUE}     |      /  ║  
║   \\     |     {Fore.RED}~by redbith & s3cret{Fore.BLUE}    |     /   ║
╚═════════════════════════════════════════════════╝
║                 \\ Available on /                ║ 
║                  ──────────────                 ║
║ Kali Linux | Arch | Void Linux | Debian--Ubuntu ║
╚═════════════════════════════════════════════════╝
║                                                
 ⠀⣠⣖⣖⠦⡀⢰⡆⢀⣠⡦⠄                               
║⠰⠟⠁⠉⣦⢥⣼⡿⠛⠙⢦⡈⡄                             
  ⠀⠀⠀⣿⡟⢹⡇⠀⠀⣸⠼⠁⠀   Powered By RedRealm Team       
║ ⠀⣴⣶⣧⡗⢸⣇⣤⡾⡉⠀⠀⠀    
 ⠀ ⠉⠀⡯⡟⢸⠁⠀⢳⠈⡄⠀⠀  ✉ scriptpy777@gmail.com    
║⠀⠀ ⢀⡇⠇⢸⠀⠀⠈⣁⣨⠀⠀  github.com/Red-BITH/BLOODFETCH                          
 ⠀⢠⡾⠿⠿⠧⣏⣐⠶⠀⢣⣃⡱⠂                             
║ ⠈⠀⠀⠀⠀⠈⠁⠀⠀⠀⠉⠀⠀                               
╚═ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══


""")
def bullet():
    road = "|-------"
    bullet = "⁍"
    target = "⭕"
    
    for i in range(len(road)+1):
        sys.stdout.write(f"\r{road[:i]}{bullet}{' '*(len(road)-i)}{target}|")
        sys.stdout.flush()
        time.sleep(0.3)
    
    
    print(f"\r|         💢 ̗̀ ⁍"+"|")
    time.sleep(0.3)

    print(f"\033[A|         💢 ̗̀  ⁍|",flush=True)
    print("\nType anything to start")
    

bullet()

input("➤")
#--------------------------------------------------------------------------
os.system("cls")
print(f"""{Fore.BLUE}
                ╭─────────────────╮
                │{Fore.RED}BL{Fore.RED}OO{Fore.RED}DFETCH{Fore.GREEN} v0.0.1{Fore.BLUE}│
╔═════════════════════════════════════════════════╗
║   {Fore.RED}▄︻デ══━一{Fore.RED}💥{Fore.RED}───────────────────────────💢───{Fore.BLUE} ̗̀ {Fore.RED}⁍{Fore.BLUE}  
║\\         _____________________________         /║
║ \\       |  {Fore.GREEN}P A C K A G E  H U N T E R{Fore.BLUE} |       / ║
║  \\      |     {Fore.RED}I N  T H E  D A R K{Fore.BLUE}     |      /  ║  
║   \\     |     {Fore.RED}~by redbith & s3cret{Fore.BLUE}    |     /   ║
╚═════════════════════════════════════════════════╝""")
print("║" + "TOOL CATEGORIES".center(49) + "║")
print(f"""║ 0 ⇨ Info Gathering     | 5 ⇨ Exploitation Tools{Fore.BLUE} ║
║ {Fore.RED}1 ⇨ Vulnerability Scan | 6 ⇨ Sniffing/Spoofing{Fore.BLUE}  ║
║ {Fore.RED}2 ⇨ Web App  Attacks   | 7 ⇨ Maintaining Access{Fore.BLUE} ║
║ {Fore.RED}3 ⇨ Password Attacks   | 8 ⇨ Post Exploitation{Fore.BLUE}  ║
║ {Fore.RED}4 ⇨ Wireless Attacks   | 9 ⇨ Social Engineering{Fore.BLUE} ║""")
print("║" + f"{Fore.RED}    99 ⇨ EXIT".center(49) + f"{Fore.BLUE}     ║")
print(f"╚═════════════════════════════════════════════════╝")

