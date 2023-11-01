from socket import *
from threading import *
from PIL import ImageTk, Image
import tkinter as tk

Hostname = gethostname()
Host_IP = gethostbyname(Hostname)
win = tk.Tk()
image_index = 0
images = [
    ImageTk.PhotoImage(Image.open("images/pop1.png")),
    ImageTk.PhotoImage(Image.open("images/pop2.png")),
]


def change_image():
    global image_index, lab
    image_index = (image_index + 1) % len(images)
    image = images[image_index]
    lab.configure(image=image)
    lab.image = image


def start_server():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("{}".format(Host_IP), 6543))
    while True:
        server.listen()
        user, addr = server.accept()
        while True:
            data = user.recv(1)
            if not data:
                break
            change_image()

print (Host_IP)
new_thread = Thread(target=start_server)
new_thread.start()

win.title('POPcatPOP')
win.geometry("500x454+400+300")
win.config(bg='#C45B90')
win.resizable(width=False, height=False)
img = ImageTk.PhotoImage(Image.open("images/pop1.png"))
lab = tk.Label(win, image=img)
lab.pack()
win.mainloop()
