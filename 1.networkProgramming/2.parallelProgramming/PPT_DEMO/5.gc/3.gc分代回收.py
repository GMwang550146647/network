import sys
import gc
if __name__ == '__main__':
    gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
    print(gc.get_threshold())