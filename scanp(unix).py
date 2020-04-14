# coding UTF-8
import socket
import argparse


RED = "\033[2;31m"
GREEN = "\033[1;32m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
NORMAL = "\033[0m"

FORCE = False
SMOOTH = False


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-f", "--force", help="Activate the full force scan mode.", action="store_true")
group.add_argument("-s", "--smooth", help="Default mode of scan one by one port.", action="store_true")
args = parser.parse_args()


if args.force:
    FORCE = True

if args.smooth:
    SMOOTH = True

s = socket.socket()
s.settimeout(5)

print(f"{BLUE}Scan easily your ports with {PURPLE}SCANP{NORMAL}\n{BLUE}Here's a list of common ports{NORMAL}")

print("""
        |.............|.........|..........................|
        |{3}NAME         |NUMBER   |DESCRIPTION               {1}|
        |{0}FTP-DATA {1}    |{2}20       {1}|{4}FTP                       {1}|
        |{0}FTP      {1}    |{2}21       {1}|{4}FTP                       {1}|
        |{0}DNS      {1}    |{2}53       {1}|{4}DNS request               {1}|
        |{0}HTTP     {1}    |{2}80       {1}|{4}HTTP transfert            {1}|
        |{0}AUTH     {1}    |{2}113      {1}|{4}Authentification protocol {1}|
        |{0}HTTPS    {1}    |{2}443      {1}|{4}Secure HTTP transfert     {1}|    
        |{0}MICROSOFT-DS {1}|{2}445      {1}|{4}SMB protocol              {1}|
        |{0}WHOAMI   {1}    |{2}565      {1}|{4}ID list of whoami's users {1}|    
        |.............|.........|..........................|  

""".format(PURPLE, NORMAL, GREEN, RED, BLUE))


def Default():
    while True:
        host = input(f"Target {BLUE}IP{NORMAL} = ")
        port = input(f"Target {BLUE}PORT{NORMAL} = ")

        try:
            port = int(port)

            if s.connect_ex((host, port)):
                print(f"The {BLUE}port {port} {NORMAL}at {BLUE}{host} {NORMAL}is {RED}closed or didn't send a response.{NORMAL}")
                break

            else:
                print(f"The {BLUE}port {port} {NORMAL}at {BLUE}{host} {NORMAL}is {GREEN}open.{NORMAL}")
                break

        except ValueError:
            print(f"{BLUE}{port} {RED}isn't an acceptable value, try with a number.{NORMAL}")

        except socket.gaierror:
            print(f"The {BLUE}address {host} {NORMAL}is {RED}probably incorrect. {NORMAL}")

        except OverflowError:
            print(f"{RED}The port must be between 0 and 65 535. {BLUE}{port} {RED}isn't the case.{NORMAL}")


def Force():
    while True:
        host = input(f"Target {BLUE}IP{NORMAL} = ")
        print("Force mode in construction")
        break


if SMOOTH:
    Default()

elif FORCE:
    Force()

else:
    Default()


input()
