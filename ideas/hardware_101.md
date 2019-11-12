# CircuitPython 101: Intro to Hardware

## Pitch
CircuitPython brings one of our favorite languages to physical devices but the hardware world includes lots of new jargon (MCU, I2C, SPI, USB, RAM, ROM to name a few). Come learn the hardware basics as I demystify the most common terms used when discussing how to hook up sensors to CircuitPython.

## Description
The goal of this talk is to demystify a number of electronics terms to make getting started easier. The focus will be on terms encountered when first getting started with CircuitPython and when connecting external sensors and displays to a board running CircuitPython.

* CircuitPython Basics - 7 minutes
    * Connecting to CircuitPython
        * USB - Universal Serial Bus
        * BLE - Bluetooth Low Energy
    * MCU - Basics of a microcontroller
        * RAM - volatile storage of data such as Python objects
        * ROM -
    * PCB - Circuit boards connect circuit components together and make certain connections available to external devices.
* Protocol basics - 7 minutes
    * It's all about moving bits
    * Logic level dictates what is a one or zero
    * Voltage is relative and always needs ground
    * Pull ups and downs are default values for a wire
    * Clocks dictate when data is valid
    * Multiple wires make up a bus
* Common protocols - 7 minutes
    * NeoPixel - set timing, single wire, lots of blinky
    * I2C - Inter Integrated Circuit - Shared bus with slow clock
    * SPI - Serial Peripheral Interface - Solo bus with fast clock
    * Basic debugging with logic analyzer
* SoC - System on a Chip 4 minutes
    * Same basic idea but much wider buses, short wires and faster frequencies.

## Notes
This is a new talk.

I am heavily involved with CircuitPython and would love to see more folks involved
