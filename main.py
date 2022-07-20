def on_button_pressed_a():
    basic.show_string("OK")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(3000)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
    basic.pause(3000)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(3000)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
    basic.pause(3000)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
    basic.pause(3000)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(3000)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
    basic.pause(3000)
input.on_button_pressed(Button.B, on_button_pressed_b)

pins.analog_write_pin(AnalogPin.P0, 1023)
basic.show_leds("""
    . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
""")
basic.show_leds("""
    # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
""")
basic.show_leds("""
    # # # # #
        # # # # #
        # # . # #
        # # # # #
        # # # # #
""")
basic.show_leds("""
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
""")

def on_forever():
    pass
basic.forever(on_forever)
