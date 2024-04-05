# Cutting the USB cord

## Wirelessly programming CircuitPython

---

![bg left](scott_with_blinka.jpg)

# Hello
- I'm Scott
- I work for [Adafruit](https://adafruit.com)
- [@tannewt](https://tannewt.org) online

---

![bg](clue_front.jpg)

---

![bg](clue_back.jpg)

---

![bg](clue_back_usb.jpg)

---

![bg](clue_back_mcu.jpg)

---

![bg](clue_back_antenna.jpg)

---

# circuitpython.org

---

![bg](cporg0.png)

---

![bg](cporg1.png)

---

![bg](cporg2.png)

---

![bg](cporg3.png)

---

![bg](usb_hub_unplugged.jpg)

---

![bg](usb_hub_plugged.jpg)

---

![bg](clue_unplugged.jpg)

---

![bg](clue_double_tap.jpg)

---

![bg](clue_bootloader.jpg)

---

![bg](dolphin_boot.png)

---

![bg](dolphin.png)

---

![bg](dolphin_circuitpy.png)

---

![bg](dolphin_codepy.png)

---

![bg](sublime0.png)

---

![bg](sublime1.png)
![bg](tio0.png)

---

![bg](sublime1.png)
![bg](tio1.png)

---

![bg](sublime1.png)
![bg](tio2.png)

---

![bg](sublime1.png)
![bg](tio3.png)

---

![bg](sublime2.png)
![bg](tio3.png)

---

![bg](sublime3.png)
![bg](tio4.png)

---

# Workflow
<!-- 8 minutes -->

- What makes a workflow?
  - Installing CircuitPython
  - File system access
    - Editing code
    - Transferring files such as libraries
  - Print debugging output.

---
# What to what
  - Consider the devices to program from:
    - 🖥️desktop
    - 💻laptop
    - 📱phone
    - 📱tablet
  - Consider the capabilities of the device to program
    - 🔌Wired
    - 🛜Wireless

---

# Connectivity

  - **USB**: CIRCUITPY drive + serial over USB
    - Most except ESP32, ESP32-CX, micro:bit v2
    - CircuitPython version 1+
  - **Bluetooth (BLE)**: Good for on the go, iOS and Android
    - nRF52840, ESP32-S3 and CX coming soon 🤞
    - CircuitPython version 7+
  - **WiFi**: Good for stationary with multiple devices
    - ESP32, ESP32-SX, ESP32-CX, Pico W
    - CircuitPython version 8+

---

# Status

| | USB |
| - | - |
| Install | ✅🧑‍💻✅💻⚠️📱 |
| Upgrade | ✅🧑‍💻✅💻⚠️📱 |
| File System |✅🧑‍💻✅💻⚠️📱 |
| Edit Code |✅🧑‍💻✅💻⚠️📱 |
| Print Output |✅🧑‍💻✅💻⚠️📱 |

- ❌None ⚠️Partial ✅Supported
- 🧑‍💻API 💻Desktop 📱Mobile

---

# Status

| | USB | WiFi | BLE |
| - | - | - | - |
| Install | ✅🧑‍💻✅💻⚠️📱 | ?🧑‍💻?💻?📱 | ?🧑‍💻?💻?📱 |
| Upgrade | ✅🧑‍💻✅💻⚠️📱 | ?🧑‍💻?💻?📱 | ?🧑‍💻?💻?📱 |
| File System |✅🧑‍💻✅💻⚠️📱 | ?🧑‍💻?💻?📱 | ?🧑‍💻?💻?📱 |
| Edit Code |✅🧑‍💻✅💻⚠️📱 | ?🧑‍💻?💻?📱 | ?🧑‍💻?💻?📱 |
| Print Output |✅🧑‍💻✅💻⚠️📱 | ?🧑‍💻?💻?📱 | ?🧑‍💻?💻?📱 |

- ❌None ⚠️Partial ✅Supported
- 🧑‍💻API 💻Desktop 📱Mobile
---

# Installing CircuitPython

- **USB** is easy with `*BOOT` drive via UF2 bootloader
- **USB serial** is easy with circuitpython.org installer for supported boards
- **BLE** is custom
- **WiFi** no bootloader support

---

# circuitpython.org
## Installing w/o `*BOOT`

---

![bg](webinstall0.png)

---

![bg](webinstall1.png)

---

![bg](webinstall2.png)

---

![bg](webinstall3.png)

---

![bg](webinstall4.png)

---

![bg](webinstall5.png)


---

![bg](webinstall6.png)

---

![bg](webinstall7.png)

<!-- missed 8 -->

---

![bg](webinstall9.png)

---

![bg](webinstall10.png)

---

![bg](webinstall11.png)

---

![bg](webinstall12.png)

---

![bg](webinstall13.png)

---

![bg](webinstall14.png)

---

![bg](webinstall15.png)

---

![bg](webinstall16.png)

---

![bg](webinstall17.png)

---

# settings.toml

```toml
CIRCUITPY_WIFI_SSID = "wifi_ssid"
CIRCUITPY_WIFI_PASSWORD = "wifi_password"
CIRCUITPY_WEB_API_PASSWORD = "hello"
CIRCUITPY_WEB_API_PORT = 80
```
---

# http://circuitpython.local
## No https!

---

![bg](ww0.png)

---

![bg](ww1.png)

---

![bg](ww2.png)

---

![bg](ww3.png)

---

![bg](ww4.png)

---

![bg](ww5.png)

---

![bg](ww6.png)

---

# [code.circuitpython.org](https://code.circuitpython.org)

---

![bg](cporg.png)

---

![bg](codecp0.png)

---

![bg](codecp1.png)

---

![bg](codecp2.png)

---

![bg](codecp3.png)

---

![bg](codecp4.png)

<!-- 5 minutes -->

<!-- code.circuitpython.org supports code editing from a browser via storage or Bluetooth APIs (webkit only).
  - circuitpython.local supports local editing over WiFi without internet. /code/ can be used when online for a richer experience. -->

---

# 📱 Mobile

<!-- 5 minutes -->


---

![bg left:26% h:720px](adafruit_ios_glider.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

---

![bg left:26% h:720px](glider0.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

---

![bg](clue_blue_blink.jpg)

---

![bg left:26% h:720px](glider1.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

---

![bg left:26% h:720px](glider2.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

---

![bg left:26% h:720px](glider3.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

---
![bg left:26% h:720px](glider4.png)
# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

---
![bg left:26% h:720px](glider5.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)


---

![bg left:26% h:720px](files0.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

---

![bg left:26% h:720px](files1.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

---

![bg left:26% h:720px](files2.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

---

![bg left:26% h:720px](files3.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)
- Bug! 🐛


---

![bg left:26% h:720px](adafruit_ios_connect.png)

# Bluefruit Connect
- Bluefruit Connect connects to the serial portion of the API.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.bluefruit.le.connect) and [iOS](https://apps.apple.com/us/app/bluefruit-connect/id830125974)

---

![bg left:26% h:720px](connect0.png)

# Bluefruit Connect
- Bluefruit Connect connects to the serial portion of the API.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.bluefruit.le.connect) and [iOS](https://apps.apple.com/us/app/bluefruit-connect/id830125974)

---

![bg left:26% h:720px](connect1.png)

# Bluefruit Connect
- Bluefruit Connect connects to the serial portion of the API.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.bluefruit.le.connect) and [iOS](https://apps.apple.com/us/app/bluefruit-connect/id830125974)

---

![bg left:26% h:720px](connect2.png)

# Bluefruit Connect
- Bluefruit Connect connects to the serial portion of the API.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.bluefruit.le.connect) and [iOS](https://apps.apple.com/us/app/bluefruit-connect/id830125974)

---

![bg left:26% h:720px](connect3.png)

# Bluefruit Connect
- Bluefruit Connect connects to the serial portion of the API.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.bluefruit.le.connect) and [iOS](https://apps.apple.com/us/app/bluefruit-connect/id830125974)

---

![bg left:26% h:720px](ezgif.com-gif-maker1.gif)

# PyLeap
- PyLeap is project repository app that makes it easy to load a full projects wirelessly. No more blank page syndrome.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.pyleap) and [iOS](https://apps.apple.com/us/app/pyleap/id1582204203)
- Bug! 🐛

---

# 🧑‍💻 Behind the scenes

<!-- 5 minutes -->

- [Workflow Documentation](https://docs.circuitpython.org/en/latest/docs/workflows.html)
- BLE Workflow
  - Serial over Nordic UART Service but with different UUIDs
  - Custom FileTransfer service
- Web workflow
  - MDNS for discovery
  - HTTP API for file access
  - WebSocket

---

# Status

| | USB | WiFi | BLE |
| - | - | - | - |
| Install | ✅🧑‍💻✅💻⚠️📱 | ❌🧑‍💻❌💻❌📱 | ⚠️🧑‍💻❌💻❌📱 |
| Upgrade | ✅🧑‍💻✅💻⚠️📱 | ⚠️🧑‍💻❌💻❌📱 | ⚠️🧑‍💻❌💻❌📱 |
| File System |✅🧑‍💻✅💻⚠️📱 | ✅🧑‍💻✅💻✅📱 | ✅🧑‍💻✅💻✅📱 |
| Edit Code |✅🧑‍💻✅💻⚠️📱 | ✅🧑‍💻✅💻✅📱 | ✅🧑‍💻✅💻✅📱 |
| Print Output |✅🧑‍💻✅💻⚠️📱 | ✅🧑‍💻✅💻❌📱 | ✅🧑‍💻✅💻✅📱 |

- ❌None ⚠️Partial ✅Supported
- 🧑‍💻API 💻Desktop 📱Mobile
---

# Status (really)

| | USB | WiFi | BLE |
| - | - | - | - |
| Install | ✅🧑‍💻✅💻🐛📱 | ❌🧑‍💻❌💻❌📱 | ⚠️🧑‍💻❌💻❌📱 |
| Upgrade | ✅🧑‍💻✅💻🐛📱 | ⚠️🧑‍💻❌💻❌📱 | ⚠️🧑‍💻❌💻❌📱 |
| File System |✅🧑‍💻✅💻🐛📱 | 🐛🧑‍💻🐛💻🐛📱 | 🐛🧑‍💻🐛💻🐛📱 |
| Edit Code |✅🧑‍💻✅💻🐛📱 | 🐛🧑‍💻🐛💻🐛📱 | 🐛🧑‍💻🐛💻🐛📱 |
| Print Output |✅🧑‍💻✅💻🐛📱 | 🐛🧑‍💻🐛💻❌📱 | 🐛🧑‍💻🐛💻🐛📱 |

- ❌None ⚠️Partial ✅Supported 🐛Bugs
- 🧑‍💻API 💻Desktop 📱Mobile

---

# App source links

- File Glider [iOS](https://github.com/adafruit/Glider-for-iOS) [Android](https://github.com/adafruit/Glider-for-Android)
- BluefruitConnect [iOS](https://github.com/adafruit/Bluefruit_LE_Connect_v2) [Android](https://github.com/adafruit/Bluefruit_LE_Connect_Android)
- PyLeap [iOS](https://github.com/adafruit/PyLeap-iOS) [Android](https://github.com/adafruit/PyLeap-Android)

<!-- Call to action: wireless programming workflows require new tools. Help us build and refine them to make coding easy and accessible for all. -->

---

# Thanks

- Antonio and Trevor for the mobile apps
- Melissa for code.circuitpython.org
- Liz for testing all of these

---

# Links

- [https://circuitpython.org](circuitpython.org)
- [https://github.com/tannewt/presentations/20240407-pycascades](https://github.com/tannewt/presentations/20240407-pycascades)
