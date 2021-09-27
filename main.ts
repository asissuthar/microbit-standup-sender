radio.setGroup(1)
radio.setTransmitPower(7)
loops.everyInterval(3000, function () {
    radio.sendNumber(0)
})
