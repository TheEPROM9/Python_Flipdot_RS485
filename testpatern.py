import numpy as np
from pyflipdot.sign import HanoverSign
from pyflipdot.pyflipdot import HanoverController
from serial import Serial

# Create a serial port (update with port name on your system)
ser = Serial('/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0')

# Create a controller
controller = HanoverController(ser)

# Add a sign
# Note: The sign's address is set via it's potentiometer
#sign = HanoverSign(address=1, width=96, height=8)
sign = HanoverSign(address=1, width=144, height=19)
controller.add_sign('dev', sign)

# Create a 'checkerboard' image
image = sign.create_image()
# [ x , y ]
# : = Solid Line
# ; = Every Other LED
image[2, 1] = True
image[3, 1] = True
image[4, 1] = True
image[5, 1] = True

image[2, 6] = True
image[3, 6] = True
image[4, 6] = True
image[5, 6] = True

image[1, 2] = True
image[1, 3] = True
image[1, 4] = True
image[1, 5] = True

image[6, 2] = True
image[6, 3] = True
image[6, 4] = True
image[6, 5] = True

image[3, 3] = True
image[4, 3] = True
image[3, 4] = True
image[4, 4] = True

#image[4, 91] = True
#image[4, 92] = True
#image[3, 92] = True
#image[3, 91] = True

#image[2, 94] = True
#image[3, 94] = True
#image[4, 94] = True
#image[5, 94] = True

#image[2, 89] = True
#image[3, 89] = True
#image[4, 89] = True
#image[5, 89] = True

#image[1, 93] = True
#image[1, 92] = True
#image[1, 91] = True
#image[1, 90] = True

#image[6, 93] = True
#image[6, 92] = True
#image[6, 91] = True
#image[6, 90] = True

image[4, 140] = True
image[4, 139] = True
image[3, 140] = True
image[3, 139] = True

image[2, 142] = True
image[3, 142] = True
image[4, 142] = True
image[5, 142] = True

image[2, 137] = True
image[3, 137] = True
image[4, 137] = True
image[5, 137] = True

image[1, 141] = True
image[1, 140] = True
image[1, 139] = True
image[1, 138] = True

image[6, 141] = True
image[6, 140] = True
image[6, 139] = True
image[6, 138] = True


# Write the image
controller.draw_image(image)
