import tensorflow as tf
import tensorflow.keras as keras

print("GPUS: ", tf.config.list_physical_devices('GPU'))
print("Tensorflow: ", tf.__version__)
print("Keras: ", keras.__version__)
