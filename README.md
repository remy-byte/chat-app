# chat-app

Chatroom app is a python script that allows communication through a chatroom between multiple clients.  

# How does it work and technologies behind it  
The python application is made with the socket and threading modules that allow the communication between a server and multiple clients. Additionally, the python app has an user interface for every client using the tkinter module.
For more information on all the modules you can see here:
* [tkinter](https://docs.python.org/3/library/tkinter.html)
* [socket](https://docs.python.org/3/library/socket.html)
* [threading](https://docs.python.org/3/library/threading.html)


## Installation

You can install tkinter using the package manager [pip](https://pip.pypa.io/en/stable/).

```bash
pip install tk
```

## Usage

In order to run the application you need to run the "server.py" script which will allow the connection of other clients to it.  
After that, you can open the second script, the "clinent_GUI.py" that will initially prompt a login interface where you will need to enter your name.

<img src="https://user-images.githubusercontent.com/80782419/221226341-68a53bd3-a6d1-401f-b6be-1d860a245c09.png" width=20% height=20%>

Then, the login window closes, and the chatroom will appear and you will be able to communicate with the other clients that are connected to the server.  
When someone joins or leaves the server, the "server.py" script will give a notification in the command line.
You can leave the chatroom without any issues to the server by typing in chat "!DISCONNECT".

<img src="https://user-images.githubusercontent.com/80782419/221230183-7bef7202-95e5-4d6a-bedf-c65926abd186.png" width=40% height=40%>



# Additional information

In order to run the server.py and client_GUI.py scripts on your computers you have to modify the server_ip and port in each of the files using a text editor.  
These two variables will both be found in the init method of each class of the scripts.  
Example server.py script:
```bash
class Server:

    def __init__(self):


           ---> self.SERVER = socket.gethostbyname(socket.gethostname()) 
           ---> self.port = 5050


        self.address = (self.SERVER, self.port) 
        self.format = 'utf-8'
        self.clients = {}
```

If you want to run the script locally you can already do this, as the server_ip is initiallised with the local host's local ip.

# Roadmap

* Further documentation on sockets and threading modules.  
* Improving the user interface by polishing the chatroom interface and adding an emojis menu.
