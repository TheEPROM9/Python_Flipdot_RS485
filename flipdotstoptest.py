from pyflipdot.pyflipdot import HanoverController
from serial import Serial

# Create a serial port (update with port name on your system)
ser = Serial('/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0')

# Create a controller
controller = HanoverController(ser)

# Start the test sequence on any connected signs
controller.stop_test_signs()
