radio.set_group(1)
radio.set_transmit_power(7)

def on_every_interval():
    radio.send_number(0)
loops.every_interval(3000, on_every_interval)
