#!/usr/bin/env python
import time
import pantilthat as xy

xy.idle_timeout(0.25)

tilt_y = xy.get_tilt()

if tilt_y < 90:
    tilt_y = tilt_y+2
    xy.tilt(tilt_y)
    time.sleep(0.25)
