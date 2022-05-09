
from fastai.vision.all import *
import fastai as fastai

print("Fastai: ", fastai.__version__)
path = untar_data(URLs.PETS)/'images'
print(path)

