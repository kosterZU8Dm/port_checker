# port_checker
---
106 - session is not close\
111 - connection refused\
9 - ...
---
# About Socket library
AF_INET = ipv4 addresses\
SOCK_STREAM = means tcp socket
---
### First problem. 23.01.2024
1. I catch error, when I made socket outside loop of for. For fix I need move creation of socket to loop inside function.
2. I need to use function socket.connect_ex instead of socket.connect, because get an error code is better than get exception call
3. I need to increase a timeout of connect to port

### Usage
```
source venv/bin/active
pip install -r requirements.txt
python3 app.py 127.0.0.1
```