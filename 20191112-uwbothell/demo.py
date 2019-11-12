from adafruit_gameboy import gb

# Register's are documented here: http://marc.rawer.de/Gameboy/Docs/GBCPUman.pdf

# offset = 0xff10 # Voice 1
offset = 0xff15 # Voice 2
offset = 0xff

# Voice 1 Sweep
#   - Bit 6-4 Time
#   - Bit 3 Increase (0) or Decrease (1)
#   - Bit 2-0 Duration
gb[offset + 0] = 0b01100111
# gb[0xff10] = 0b01110111


gb[0xff11] = 0b10001111

# Voice 1 Envelope
#   - Bit 7-4 - Initial envelope volume
#   - Bit 3 - Direction
#   - Bit 2-0 number of sweep
gb[0xff12] = 0b11110011

gb[0xff13] = 0b00010011

# Voice 1
#   - Bit 7 - Start
#   - Bit 2-0 - Top 3 frequency bits
gb[0xff14] = 0x87
