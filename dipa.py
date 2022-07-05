from cProfile import label
from cgitb import text
from contextlib import redirect_stderr
from importlib.resources import path
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from turtle import width
import cv2 as cv
import cv2 
from matplotlib import pyplot as plt
import numpy as np

root = Tk()
root.title('DIPA')

my_menu = Menu(root)

# define the size of the window
root.geometry("500x250")

# Allow Window to be resizable
root.resizable(width = True, height = True)

root.config(menu=my_menu)

# file functions
def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)

def openfilename():
    filename = filedialog.askopenfilename(initialdir="D:\python-opencv\images", title="Select a file", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg")))
    return filename

def file_open():
    global img
    global path

    # Select the Imagename  from a folder
    path = openfilename()
 
    # opens the image
    img = cv2.imread(path, cv2.COLOR_BGR2RGB)
    # Image.open(path)
    img = Image.fromarray(img)
     
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)
 
    # cv_img = cv2.cvtColor(cv2.imread("background.jpg"), cv2.COLOR_BGR2RGB)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)
  
    # create a label
    panel = Label(root, image = img)
     
    # set the image as img
    panel.image = img
    panel.grid(row = 2)

# tool functions
def tool_crop():
    pass

def tool_histo():
    img = cv2.imread(path)
    cv2.imshow("Image", img)

    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def tool_histo_equi():
    pass

# filter functions 
def filter_mean():
    pass

def filter_median():
    pass

def filter_gaussian():
    # using imread()  
    img = cv2.imread(path)

    dst = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT) 
    
    cv2.imshow('image', np.hstack((img, dst)))
    cv2.waitKey(0)

def filter_sobel():
    pass

def filter_canny():
    pass

def filter_prewitt():
    pass

def filter_caplaci():
    pass

# hide all frames
def hide_all_frames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()

# Create a menu item 
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an tool menu item

tool_menu = Menu(my_menu)
my_menu.add_cascade(label="Tools", menu=tool_menu)
tool_menu.add_command(label="Crop", command=tool_crop)
tool_menu.add_command(label="Histogram", command=tool_histo)
tool_menu.add_command(label="Histogram Equilization", command=tool_histo_equi)

# create a filter menu item 

filter_menu = Menu(my_menu)
my_menu.add_cascade(label="filter", menu=filter_menu)
filter_menu.add_command(label="Mean", command=filter_mean)
filter_menu.add_command(label="Median", command=filter_median)
filter_menu.add_command(label="Gaussian", command=filter_gaussian)
filter_menu.add_command(label="Caplaci", command=filter_caplaci)
filter_menu.add_separator()
filter_menu.add_command(label="Sobel", command=filter_sobel)
filter_menu.add_command(label="Prewitt", command=filter_prewitt)
filter_menu.add_command(label="Canny", command=filter_canny)

# create an Layer menu item 

layer_menu = Menu(my_menu)
my_menu.add_cascade(label="Layer", menu=layer_menu)
layer_menu.add_command(label="New")
layer_menu.add_command(label="Duplicate Layer")
layer_menu.add_command(label="Delete")
layer_menu.add_separator()   
layer_menu.add_command(label="Layer Properties")
layer_menu.add_command(label="Layer Style")
layer_menu.add_command(label="Smart Filter")
layer_menu.add_separator()
layer_menu.add_command(label="New Fill Layer")
layer_menu.add_command(label="New Adjustment Layer")
layer_menu.add_command(label="Layer Content Options")
layer_menu.add_command(label="Layer Mask")

# create an analysis menu item 

analysis_menu = Menu(my_menu)
my_menu.add_cascade(label="Analysis", menu=analysis_menu)
analysis_menu.add_command(label="Set Measurment Scale")
analysis_menu.add_command(label="Select Data Points")
analysis_menu.add_command(label="Record Measurements") 
analysis_menu.add_separator()   
analysis_menu.add_command(label="Rooler Tool") 
analysis_menu.add_command(label="Count Tool")

# create a view menu item 

view_menu = Menu(my_menu)
my_menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Proof Setup")
view_menu.add_command(label="Proof Colors") 
view_menu.add_command(label="Pixel Aspect ratio") 
view_menu.add_separator()
view_menu.add_command(label="Zoom In")
view_menu.add_command(label="Zoom Out")
view_menu.add_command(label="Fit On Screen")
view_menu.add_command(label="Actual Pixels")

# create a help menu item 

help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Photoshop Help")
help_menu.add_command(label="Legal Notices") 
help_menu.add_command(label="System Info") 

# Create some frames
file_new_frame = Frame(root, bd=2, relief="raised", bg="yellow")
edit_cut_frame = Frame(root, bd=2, relief="raised")

root.mainloop()