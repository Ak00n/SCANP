# coding UTF-8
import socket
import argparse

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

print(f"Scan easily your ports with SCANP\nHere's a list of common ports")

print("""
        |.............|.........|..........................|
        |NAME         |NUMBER   |DESCRIPTION               |
        |FTP-DATA     |20       |FTP                       |
        |FTP          |21       |FTP                       |
        |DNS          |53       |DNS request               |
        |HTTP         |80       |HTTP transfer             |
        |AUTH         |113      |Authentication protocol   |
        |HTTPS        |443      |Secure HTTP transfer      |    
        |MICROSOFT-DS |445      |SMB protocol              |
        |WHOAMI       |565      |ID list of whoami's users |    
        |.............|.........|..........................|  

""")


def Default():
    host = input(f"Target IP = ")

    while True:
        port = input(f'Target PORT = ("stop" to exit) ')

        if port == 'stop' or port == '"stop"':
            print("Exiting...")
            break

        try:
            port = int(port)

            if s.connect_ex((host, port)):
                print(f"The port {port} at {host} is closed or didn't send a response.")

            else:
                print(f"The port {port} at {host} is open.")

        except ValueError:
            print(f"{port} isn't an acceptable value, try with a number.")

        except socket.gaierror:
            print(f"The address {host} is probably incorrect. ")

        except OverflowError:
            print(f"The port must be between 0 and 65 535. {port} isn't the case.")


def Force():
    open_ports = []
    while True:
        host = input(f"Target IP = ")
        print("Force mode in construction")

        for port in range(0, 1000):
            if s.connect_ex((host, port)):
                print(f"The port {port} at {host} is closed or didn't send a response.")

            else:
                print(f"The port {port} at {host} is open.")
                open_ports.append(port)

        break

    if open_ports:
        print(f"Ports {open_ports} are opens.")


if SMOOTH:
    Default()

elif FORCE:
    Force()

else:
    Default()
