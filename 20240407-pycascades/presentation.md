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

![bg](dolphin.png)

---

![bg](dolphin_circuitpy.png)

---

![bg](dolphin_codepy.png)

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

  - USB: CIRCUITPY drive + serial over USB
    - Most except ESP32, ESP32-CX, micro:bit v2
  - Bluetooth: Good for on the go, iOS and Android
    - nRF52840, ESP32-S3 and CX coming soon 🤞
  - WiFi: Good for stationary with multiple devices
    - ESP32, ESP32-SX, ESP32-CX, Pico W

---

# settings.toml

```toml
CIRCUITPY_WIFI_SSID = "wifi_ssid"
CIRCUITPY_WIFI_PASSWORD = "wifi_password"
CIRCUITPY_WEB_API_PASSWORD = "hello"
CIRCUITPY_WEB_API_PORT = 80
```

---

# 📱 Mobile

<!-- 5 minutes -->

---

![bg left:26% h:720px](adafruit_ios.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

---

![bg left:26% h:720px](glider0.png)

# File Glider
- File Glider connects a CP device into the mobile OS file API so other apps can be used with it.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.glider) and [iOS](https://apps.apple.com/us/app/file-glider/id1583976527)

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

![bg left:26% h:720px](adafruit_ios.png)

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

# PyLeap
- PyLeap is project repository app that makes it easy to load a full projects wirelessly. No more blank page syndrome.
- On [Android](https://play.google.com/store/apps/details?id=com.adafruit.pyleap) and [iOS](https://apps.apple.com/us/app/pyleap/id1582204203)

---

# [code.circuitpython.org](https://code.circuitpython.org)

---

![bg](cporg.png)

<!-- 5 minutes -->

<!-- code.circuitpython.org supports code editing from a browser via storage or Bluetooth APIs (webkit only).
  - circuitpython.local supports local editing over WiFi without internet. /code/ can be used when online for a richer experience. -->

---

# Behind the scenes

<!-- 5 minutes -->

- Behind the scenes - 5 minutes
  - Bluetooth services
  - HTTP API

---

# Status

| | USB | WiFi | BLE |
| - | - | - | - |
| Install | ✅🧑‍💻✅💻⚠️📱 | ❌🧑‍💻❌💻❌📱 | ⚠️🧑‍💻❌💻❌📱 |
| Upgrade | ✅🧑‍💻✅💻⚠️📱 | ⚠️🧑‍💻❌💻❌📱 | ⚠️🧑‍💻❌💻❌📱 |
| File System |✅🧑‍💻✅💻⚠️📱 | ✅🧑‍💻✅💻✅📱 | ✅🧑‍💻✅💻✅📱 |
| Edit Code |✅🧑‍💻✅💻⚠️📱 | ✅🧑‍💻✅💻✅📱 | ✅🧑‍💻✅💻✅📱 |
| Print Output |✅🧑‍💻✅💻⚠️📱 | ✅🧑‍💻✅💻✅📱 | ✅🧑‍💻✅💻✅📱 |

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
| Print Output |✅🧑‍💻✅💻🐛📱 | 🐛🧑‍💻🐛💻🐛📱 | 🐛🧑‍💻🐛💻🐛📱 |

- ❌None ⚠️Partial ✅Supported 🐛Bugs
- 🧑‍💻API 💻Desktop 📱Mobile

<!-- Call to action: wireless programming workflows require new tools. Help us build and refine them to make coding easy and accessible for all. -->

---

# Thanks

- Antonio and Trevor for the mobile apps
- Melissa for code.circuitpython.org

---

# Links

- [https://circuitpython.org](circuitpython.org)
- [https://github.com/tannewt/presentations/20240407-pycascades](https://github.com/tannewt/presentations/20240407-pycascades)
