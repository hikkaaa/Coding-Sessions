'''tutorial by: https://data-flair.training/blogs/cartoonify-image-opencv-python/'''

# OpenCV : cross-platform library for Computer Vision (applications like video and 
# image capturing and processing). 
# when do you use it? In image transformation, object detection, face recognition, etc.

# The aim of this program is to tranform images into its cartoon

# image processing
import importlib
import cv2 

# open filebox
import easygui

# store image
import numpy as np
# read image stored at particular path
import imageio
import sys
import matplotlib.pyplot as plt
import os 
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

#main window
top=tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',20,'bold'))

def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)

def save(resized6, ImagePath):
    # saving image using imwrite()
    new_name = 'cartoonified_image'
    path1 = os.path.dirname(ImagePath)
    extension = os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, new_name+extension)
    cv2.imwrite(path, cv2.cvtColor(resized6, cv2.COLOR_RGB2BGR))
    I = 'Image saved by name ' + new_name + ' at ' + path
    tk.messagebox.showinfo(title = None, message = I)

def cartoonify(ImagePath):
    # read image
    # image is stored in form of numbers
    originalmage = cv2.imread(ImagePath)
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)

    # confirm that image is chosen
    if originalmage is None: 
        print('Cannot find any image. Choose appropriate image file.')
        sys.exit()
    
    # resize the image after each transformation to diplay all images on a similar scale at last
    resized1 = cv2.resize(originalmage, (960, 540))

    # converting an image to grayscale
    grayscaleimage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)
    resized2 = cv2.resize(grayscaleimage, (960, 540))

    # apply median blur to smoothen an image
    smooth_grayscale = cv2.medianBlur(grayscaleimage, 5)
    resized3 = cv2.resize(smooth_grayscale, (960, 540))

    # cartoon effect = highlighted edges and smooth colors
    # retrieving the edges for cartoon effect by using thresholding technique
    get_edge = cv2.adaptiveThreshold(smooth_grayscale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    resized4 = cv2.resize(get_edge, (960, 540))

    # work on smooth colors 
    # apply bilateral filter to remove noise and keep adge sharp as required
    colorimage = cv2.bilateralFilter (originalmage, 9, 300, 300)
    resized5 = cv2.resize(colorimage, (960, 540))

    # finally, give a cartoon effect
    cartooon_image = cv2.bitwise_and(colorimage, colorimage, mask=get_edge)
    resized6 = cv2.resize(cartooon_image, (960, 540))

    # plotting the whole transition
    images = [resized1, resized2, resized3, resized4, resized5, resized6]
    fig, axes = plt.subplots(3, 2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace = 0.1, wspace = 0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')

    # save button code
    save1 = Button(top, text='Save cartoon image', command=lambda:save(ImagePath, resized6), padx=30, pady=5)
    save1.configure(background='#364156', foreground='white', font=('calibri', 10,'bold'))
    save1.pack(side=TOP, pady=50)
    plt.show()

upload0 = Button(top, text='Cartoonify an Image', command=upload, padx=10, pady=5)
upload0.configure(background='#364156', foreground='white', font=('calibri', 10,'bold'))
upload0.pack(side=TOP, pady=50)

top.mainloop()




