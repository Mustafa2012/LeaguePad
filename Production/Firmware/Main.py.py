import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# I2C bus on the XIAO RP2040
i2c = busio.I2C(board.GP4, board.GP2)  
driver = SSD1306(
    
    i2c=i2c,
    
    device_address=0x3C,
)

display = Display(display=driver, width=128, height=64)

display.entries = [
    TextEntry(text="Booting up...", x=128, y=0, x_anchor="R", y_anchor="T"), # text in Top Right corner
    TextEntry(text="ON", x=128, y=64, x_anchor="R", y_anchor="B"), # text in Bottom Right corner
    TextEntry(text="Hackpad", x=64, y=32, x_anchor="M", y_anchor="M"), # text in the Middle of screen
]
keyboard.extensions.append(display)

keyboard.extensions.append(MediaKeys())

# column and row pins
keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)  
keyboard.row_pins = (board.GP6, board.GP7, board.GP0)  

# Set the diode orientation
keyboard.diode_orientation = DiodeOrientation.COL2ROW

xxx = KC.NO
___ = KC.TRNS


# Define the keymap
keyboard.keymap = [
        # First Layer
        [
            KC.1, KC.2, KC.3, KC.4,
            KC.Q, KC.W, KC.E, KC.R,
            KC.P, KC.FB, KC.D, KC.F,
        ], 
    ]

if __name__ == '__main__':
    keyboard.go()
