from tkinter import *
from PIL import Image, ImageTk
import os
# config 
root = Tk()
root.geometry("600x500")
root.title("Nvidia Installler")
root.resizable(width=False, height=False)
root.configure(bg='black')
#
# imge gorup
img  = Image.open("completion.png") 
resize_image = img.resize((600, 500))
photo=ImageTk.PhotoImage(resize_image)
lab=Label(image=photo) .pack()   #.place(x=50,y=50)
# 
\


    #gx.mainloop



#def nvidia_scan():
   # sr = txt.get()
   # gx = Tk()
   # print()
   # gx.geometry("600x500")
 #   gx.resizable(width=False, height=False)
 #   gx.configure(bg='black')
 #   Label(gx,text="[ * ] Nvidia system proputy = ") .place(x=100)
 #   #Label(gx,text=sr) .place(x=250)
  #  Button(gx,text="Nvidia 340xx") .place(x=100,y=100)
  #  Button(gx,text="Nvidia 390xx") .place(x=100,y=130)
 #   Button(gx,text="Nvidia 470xx") .place(x=100,y=160)
  #  Button(gx,text="Nvidia 525xx") .place(x=100,y=190)
   # Button(gx,text="Nvidia 535xx") .place(x=100,y=220)

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
    


brave = IntVar()
#txt = StringVar()
#Entry(root,textvariable=txt) .place(x=200,y=300)

Radiobutton(text="340xx",variable=brave,value=1,command=show) .place(x=70,y=300)
Radiobutton(text="390xx",variable=brave,value=2,command=show) .place(x=70,y=330)
Radiobutton(text="470xx",variable=brave,value=3,command=show) .place(x=70,y=360)
Radiobutton(text="525xx",variable=brave,value=4,command=show) .place(x=70,y=390)
Radiobutton(text="535xx",variable=brave,value=5,command=show) .place(x=70,y=420)

scan = Button(root,text="EXIT",command=show) .place(x=500,y=435)






root.mainloop()
