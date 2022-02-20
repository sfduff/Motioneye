#!/usr/bin/env python
import time
import pantilthat as xy

xy.idle_timeout(0.25)

pan_x = xy.get_pan()

if pan_x > -90:
    pan_x = pan_x-2
    xy.pan(pan_x)
    time.sleep(0.25)
