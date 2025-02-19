from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import bw2color_image
root=Tk()
root.title('Deoldify Your Images')
root.geometry("900x900")
root.configure(background="light blue")

my_label1=Label(root,text="Deoldify Your Images",font=("Arial italic",55),bg="light blue",fg="Blue");
my_label1.pack(pady=50)

def open():
    
    global my_image
    global file_name
    root.filename=filedialog.askopenfilename(initialdir=r"C:\Users\sanje\Documents\python projects 2020\gec\Deoldify\bw-colorization\images",title="Select a File",
                                             filetypes=(("jpg files","*.jpg"),("png files","*.png")))
    my_label=Label(root,text=root.filename).pack()
    file_name=root.filename
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()
def submit():
    global file_name
    print(file_name)
    bw2color_image.coloring(file_name)


my_btn=Button(root,text="Upload File",command=open,height=2,width=10,bg="white",fg="blue",borderwidth=20,font="Times 15 bold").pack()
my_btn=Button(root,text="submit",command=submit,height=2,width=10,bg="white",fg="blue",font="Times 10 bold").pack(pady=30)

root.mainloop()
