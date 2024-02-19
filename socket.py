import socket
import subprocess

# Получаем имя компьютера
hostname = socket.gethostname()
print("Имя компьютера:", hostname)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("172.16.2.52", 80))
ip_address = sock.getsockname()[0]
print("IP-адрес:", ip_address)
print("press 'Esc' to quit...")
from msvcrt import getch
key=getch()
if ord(pressedKey) == 27:    
   sys.exit()
