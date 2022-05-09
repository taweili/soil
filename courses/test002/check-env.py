import tensorflow as tf
import torch
import skimage
import cv2

print("Tensorflow: ", tf.__version__)
print("GPU: ", tf.config.list_physical_devices('GPU'))

print("Pytorch: ", torch.__version__)
print("GPU: ", torch.cuda.is_available())