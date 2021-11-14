import numpy as np
from ipywidgets import interact, fixed 
from PIL import Image 

def imshow(X , resize = None): 
    """
    X : is input array e.g.[256*256], could be image or any random array
    resize : e.g. (64,64) : np.resize or  ipywidget interacte function can be used as well 
   You should create a way to resize an image from an array X.
   The use of widgets is optional but you can take a look to interact.
   We should be able to install this package in Google Colab from your Git
   repo.
    """
    im = Image.fromarray(X) # convert input array to PIL image type 
    im.resize(resize,  resample=0) # use build in resize function for img type 

    return im 
