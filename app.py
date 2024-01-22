import socket
import sys
import pyfiglet

border = "-" * 50
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
ip_address = sys.argv[1]
ports_list = [80, 443, 25, 22, 8080, 2222, 21, 23, 5432, 3306]

print(ascii_banner)
print(border)
print(f'Scanning Target: {ip_address}')
print(border)

def check_port(ip_a):
    try:
        for x in ports_list:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(2)
            connection_result = sock.connect_ex((ip_a, x))
            #connection_result = sock.connect_ex((ip_a, x))
            #Возвращает номер ошибки, вместо вызова ошибки при выполнении 
            if connection_result == 0:
                print(f'port {x} is open. Success')
            elif connection_result == 111:
                print(f'port {x}, connection refused. Fail')
            else:
                print(f'port {x} is close. Code is {connection_result}')
            sock.close()
    except KeyboardInterrupt:
        print("\n Exiting Program")
        sys.exit()

check_port(ip_address)
