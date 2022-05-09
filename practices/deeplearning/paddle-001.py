import paddle
import platform

print(platform.architecture())
print("padle: " + paddle.__version__)
paddle.utils.run_check()

