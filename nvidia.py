from tkinter import *
from PIL import Image, ImageTk
import os
# config 
root = Tk()

# size windows
root.geometry("600x500")

# title
root.title("Nvidia Installler")

#  not resize windows
root.resizable(width=False, height=False)

# background color = black
root.configure(bg='black')


# imge gorup

# opne files img 
img  = Image.open("completion.png") 

# resize img to 600x500
resize_image = img.resize((600, 500))

#  ....
photo=ImageTk.PhotoImage(resize_image)

# show img in programe
lab=Label(image=photo) .pack()   # center 





# funtion choice install nvidia
def show():
    r = brave.get()
    if r == 1:
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-340xx-dkms nvidia-340xx-utils lib32-nvidia-340xx-utils nvidia-settings --noconfirm")
        os.system("clear;echo reboot you computer;echo ")
    elif r == 2:
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-390xx-dkms nvidia-390xx-utils lib32-nvidia-390xx-utils nvidia-settings --noconfirm")
        os.system("clear;echo reboot you computer;echo ")
        
    elif r == 3:
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-470xx-dkms nvidia-470xx-utils lib32-nvidia-470xx-utils nvidia-settings --noconfirm")
        os.system("clear;echo reboot you computer;echo ")
    elif r == 4:
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-525xx-dkms nvidia-525xx-utils lib32-nvidia-525xx-utils nvidia-settings --noconfirm")
        os.system("clear;echo reboot you computer;echo ")
    elif r == 5:
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-535xx-dkms nvidia-535xx-utils lib32-nvidia-535xx-utils nvidia-settings --noconfirm")
        os.system("clear;echo reboot you computer;echo ")
    else:
        exit()
    

# brave = number 1-5
brave = IntVar()


Radiobutton(text="340xx",variable=brave,value=1,command=show) .place(x=70,y=300)
Radiobutton(text="390xx",variable=brave,value=2,command=show) .place(x=70,y=330)
Radiobutton(text="470xx",variable=brave,value=3,command=show) .place(x=70,y=360)
Radiobutton(text="525xx",variable=brave,value=4,command=show) .place(x=70,y=390)
Radiobutton(text="535xx",variable=brave,value=5,command=show) .place(x=70,y=420)

scan = Button(root,text="EXIT",command=show) .place(x=500,y=435)






root.mainloop()
