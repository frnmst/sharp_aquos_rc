#!/usr/bin/env python

#
# Copyright (c) 2017, Franco Masotti <franco.masotti@live.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sharp_aquos_rc
import time

tv = sharp_aquos_rc.TV('192.168.1.5', 10002, 'admin', 'password', command_map='eu')

# Turn on the tv and leave a timeout for the next operations.
tv.power(1)
time.sleep(10)
# Set the volume to 0
tv.volume(0)
# Open the teletext
tv.teletext(1)
# Go to the specified page
tv.teletext_jump(103)
# Wait 60 seconds then turn off the tv.
time.sleep(60)
tv.power(0)
