import cv2
import skimage
import tensorflow as tf
import torch

print("Tensorflow: ", tf.__version__)
print("GPU: ", tf.config.list_physical_devices('GPU'))

print("Pytorch: ", torch.__version__)
print("GPU: ", torch.cuda.is_available())
if (torch.cuda.is_available()):
    print("Device count:", torch.cuda.device_count())