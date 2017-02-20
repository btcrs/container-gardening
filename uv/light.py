#!/usr/bin/env python
import time
from envirophat import light


try:
    while True:
        uv = light.light()
        print("{}".format(uv))
        time.sleep(0.1)
