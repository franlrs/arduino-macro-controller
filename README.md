# 🕹️ Arduino Macro Joystick (Python Bridge Automation)

![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

A physical productivity controller that executes Windows shortcuts and web automation using an analog joystick. It bridges hardware inputs with OS commands using a background **Python** script.

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://github.com/user-attachments/assets/1f167181-09fa-4b92-938f-b07e2cf4e67d" width="350" alt="Project Photo">
        <br />
        <em>The Physical Setup</em>
      </td>
      <td align="center" width="20">
        </td>
      <td align="center">
        <img src="https://github.com/user-attachments/assets/477b14e8-6ed8-4af5-b6f8-3d8639584a7c"
" width="350" alt="Control Scheme">
        <br />
        <em>Control Mappings & Description</em>
      </td>
    </tr>
  </table>
</div>

---

### 💡 The Engineering (The Workaround)

**The Challenge:**
The Arduino Uno (unlike the Leonardo/Micro) lacks native HID (Human Interface Device) capabilities, meaning it cannot be directly recognized as a USB keyboard or mouse by the computer to execute shortcuts.

**The Solution:**
I created a **Serial-to-Automation Bridge**.
1.  **Arduino:** Reads raw analog values (X/Y axis) and digital states (button) and streams them via Serial Port.
2.  **Python:** Listens to the stream, interprets the coordinates, and uses `pyautogui` to inject system-level keystrokes and `webbrowser` for navigation.

> **Result:** A custom macro controller using entry-level hardware without needing complex firmware reflashing or HID-specific boards.

---

### 🛠️ Hardware & Software

* **Board:** Arduino Uno.
* **Input:** Analog Joystick Module (KY-023 or similar).
* **Languages:** C++ (Arduino) and Python 3.x.
* **Python Libraries:** `pyserial`, `pyautogui`.

### 🔌 Wiring (Pinout)

Configuration based on the provided sketch:

| Joystick Pin | Arduino Pin | Description |
| :--- | :--- | :--- |
| **VRx** | A0 | X-Axis Analog Input |
| **VRy** | A1 | Y-Axis Analog Input |
| **SW** | D2 | Digital Switch (Button) |
| **VCC** | 5V | Power |
| **GND** | GND | Ground |

---

### 🎮 Controls & Mapping

The Python script maps the physical movements to the following actions:

| Movement | Action | Function |
| :--- | :--- | :--- |
| **Right** (X > 723) | `Alt` + `Tab` | Switch Windows / App Switcher |
| **Left** (X < 300) | Open URL | Opens YouTube |
| **Up** (Y > 723) | `Ctrl` + `W` | Close current tab/window |
| **Down** (Y < 300) | Open URL | Opens Netflix |
| **Click** (Z == 0) | `Win` + `D` | Minimize All / Show Desktop |

---

### ⚙️ Customization (Make it yours!)

You can easily modify the code to trigger your own shortcuts or open different websites.

1.  **Change Websites:**
    Open `joystick.py` and modify the URL variables at the top:
    ```python
    URL_TO_OPEN_1 = "[https://www.stackoverflow.com](https://www.stackoverflow.com)" # Change this!
    URL_TO_OPEN_2 = "[https://www.spotify.com](https://www.spotify.com)"
    ```

2.  **Change Shortcuts:**
    Look for the `pyautogui.hotkey()` functions inside the loop and change the keys. For example, to make "UP" copy text instead of closing a tab:
    ```python
    # Change 'ctrl', 'w' to 'ctrl', 'c'
    pyautogui.hotkey('ctrl', 'c') 
    ```

---

### 🚀 Installation & Setup Guide

Follow these steps strictly to avoid Serial Port conflicts.

#### Step 1: Flash the Arduino
1.  Open `analog_joystick.ino` in Arduino IDE.
2.  Connect your board via USB.
3.  Select the correct Board and Port.
4.  Click **Upload**.

#### ⚠️ Step 2: IMPORTANT - Free the Port
**Once uploaded, COMPLETELY CLOSE THE ARDUINO IDE.**
> If you leave the IDE (or Serial Monitor) open, Python won't be able to access the USB port, triggering an `Access Denied` error.

#### Step 3: Python Environment
Open a terminal in the project folder and install dependencies:

```bash
pip install -r requirements.txt
```

#### Step 4: Port Configuration

Open `joystick.py` with a text editor (or VS Code) and verify the port line:

```python
SERIAL_PORT = 'COM3'  # <--- Make sure this matches your Arduino port
```

#### Step 5: Run it!

1. Keep your Arduino connected.
2. In your terminal, run the script:

```bash
python joystick.py
```

3. Move the joystick! You should see your computer reacting to the commands.

---

### 📄 License

Project developed by **franlrs**. Distributed under the [MIT License](LICENSE).

