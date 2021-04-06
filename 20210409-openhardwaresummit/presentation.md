# An *interface* is a boundary between two things

## Scott (@tannewt)

---

# A *well designed* interface enables abstraction, compatibility and collaboration

^ Abstraction lets one ignore the "how" of *what* the interface does. Abstract interfaces enable multiple uses of the same interface which increases compatibility between things. Open interfaces allow others to work against the same abstractions and collaborate on different things.

---

![right fit](featherwings.jpg)
![left fit](feathers.jpg)

---

https://github.com/adafruit/awesome-feather/

---

In open hardware there are three common category of interfaces:

* Mechanical
* Electrical
* Software

---

![](3d_printing_feathers-6-case.jpg)

^ *Outside In* mechanical design may be designing for an existing case. In this case, the print was designed inside out. The second hole is a slot to accomodate different feather lengths. This is a sign of flexibility in the interface that if unbounded could lead to incompatibility and break the abstraction provide by the Feather interface.

---

# Mechanical

* Board size
* Mounting holes
* Component size
* Electrical connection location

![right fit](feather_fab_print.png)

---
![](neopixel_featherwing.jpg)

---

![](neopixel_featherwing_back.jpg)

---

# Electrical

* Builds on *mechanical* through contact position
* Designated function(s)/protocol(s)
* Voltage levels
* Input/output

---

![fit](feather_electrical.png)

---

![fit](feather_huzzah_masked.jpg)

---

Show examples with commented init code. Point out SCL/SDA naming greatly simplifies things

---

# Software

* Names!
* Interaction
* Default software
* Bootloader

---

# Think Outside In

---

* The feather pin numbering was different because the inside numbers were different than those of the other feathers. In particular, the Espressif Arduino core doesn't do number mapping to allow consistent numbers across boards. It assumes inside out numbering. Vendors tend to do this a bunch (Pico does as well.) It's better to abstract the numbering from the get-go so that new boards in the same form factor don't need to break the inside out numbering.

---

# Be Explicit

^ When designing a new product or interface be explicit with requirements. Any omited detail may lead to incompatibilities in the future.

* The feather spec lays out that

---

# Be Strict

When implementing

---

Designing a perfect interface is impossible but a good interface isn't. By thinking outside in, being explicit on specs and strict in implementation you'll have the best shot at producing an interface that enables abstraction, compatibility and collaboration.
