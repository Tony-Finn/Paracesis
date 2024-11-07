import os
import time

script = True

# Functions

while script == True:
    # Intro
    os.system('clear')
    print("  _____                                    _      ")
    print(" |  __ \                                  (_)     ")
    print(" | |__) |__ _  _ __  __ _   ___  ___  ___  _  ___ ")
    print(" |  ___// _` || '__|/ _` | / __|/ _ \/ __|| |/ __|")
    print(" | |   | (_| || |  | (_| || (__|  __/\__ \| |\__  ")
    print(" |_|    \__,_||_|   \__,_| \___|\___||___/|_||___/")
    print("Made by @Tony_f1nn")
    print(" ")
    print(" ")
    print(" ")
    # Real menu
    print("[1] Update system [2] Show device specs [3] SSH setup")
    print("[4] FTP Setup (un-safe) [5] FTP Setup (safe) [6] VNC Setup")

    ans = input("Number: ")

    if ans == "1":
        print("Updating system...")
        time.sleep(3)
        os.system('sudo apt update')
        os.system('clear')
        print("Updated")
        script = False
        break
    if ans == "2":
        print("Installing/Updating Neofetch...")
        time.sleep(3)
        os.system('sudo apt install neofetch')
        print("App Installed! Now launching...")
        os.system('neofetch')
        script = False
        break
    if ans == "3":
        print("Installing/Updating SSH...")
        os.system('sudo apt install ssh')
        print("Setting firewall settings...")
        time.sleep(3)
        os.system('sudo apt install ufw')
        os.system('sudo ufw allow ssh')
        print("Creating RSA keys...")
        time.sleep(3)
        os.system('sudo ssh-keygen')
        print("Listing status...")
        time.sleep(2)
        os.system('sudo systemctl status ssh')
        script = False
        break
    if ans == "4":
        print("Installing main app...")
        time.sleep(3)
        os.system('sudo apt install ftp')
        os.system('sudo apt install vsftpd')
        os.system('sudo apt install ufw')
        print("Setting firewall...")
        os.system('sudo ufw allow 443')
        os.system('sudo ufw allow 20')
        os.system('sudo ufw allow 21')
        print("Delete the hashtag where it says [local_enable=YES]")
        time.sleep(6)
        os.system('sudo nano /etc/vsftpd.conf')
        print("Now delete the hashtag at [Write_enable=YES]")
        time.sleep(6)
        os.system('sudo nano /etc/vsftpd.conf')
        os.system('sudo /etc/init.d/vsftpd restart')
        os.system('ftp localhost')
        script = False
        break
    if ans == "5":
        print("Feature not yet added")
        script = False
        break
    if ans == "6":
        print("Installing VNC...")
        time.sleep(3)
        os.system('sudo apt install xfce4 xfce4-goodies')
        os.system('sudo apt install tightvncserver')
        print("Create a password for Access, then a read-only password (optional)")
        time.sleep(3)
        os.system('vncserver')
        auto = input("Would you like to run on startup? [Y/N]")
        if auto == "Y" or "y":
            print("Stoping process...")
            time.sleep(3)
            os.system('vncserver -kill :3')
            os.system('vncserver -kill :2')
            os.system('vncserver -kill :1')
            print("Creating backup configuration...")
            time.sleep(2)
            os.system('sudo mv ~/.vnc/xstartup ~/.vnc/xstartup.bak')
            print("Creating configuration...")
            os.system('cd ~/Downloads')
            vncconf = open('xstartup', 'w')
            vncconf.write('#!/bin/bash')
            vncconf.write('\n')
            vncconf.write('xrdb $HOME/.Xresources')
            vncconf.write('\n')
            vncconf.write('startxfce4 &')
            vncconf.close()
            print("Moving startup file...")
            time.sleep(3)
            os.system('sudo mv ~/Downloads/xstartup ~/.vnc/')
            print("Executing...")
            time.sleep(2)
            os.system('sudo chmod +x ~/.vnc/xstartup')
            os.system('sudo vncserver -localhost')
            print("Done!")
            script = False
            break
        if auto == "N" or "n":
            print("Skipping...")
            time.sleep(2)
            print("Done!")
            script = False
            break
    else:
        print("Input error")
        script = False
        break
