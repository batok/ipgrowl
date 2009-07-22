import socket, Growl
notifier = Growl.GrowlNotifier("ipgrowl.py", ["ip"])
notifier.register()
notifier.notify("ip",socket.gethostbyname(socket.gethostname()),"Your Ip address",sticky=True)
