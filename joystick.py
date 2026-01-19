import serial
import time
import pyautogui
import webbrowser 

# --- CONFIGURATION ---
SERIAL_PORT = 'COM3'  # Check your specific port
BAUD_RATE = 9600
URL_TO_OPEN_1 = "https://www.youtube.com"
URL_TO_OPEN_2 = "https://www.netflix.com/es/"

# --- BROWSER CONFIGURATION (OPTIONAL: CHROME INCOGNITO) ---
# Typical Chrome path on Windows. %s is a placeholder for the URL.
# The '--incognito' flag is the trick.
# chrome_path = '"C:/Program Files/Google/Chrome/Application/chrome.exe" %s --incognito'

# STATE VARIABLES
menu_open = False   
web_open = False    

try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2) # Wait for Arduino reset
    print(f"Connected to {SERIAL_PORT}")

    while True:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            if not line: continue

            try:
                data = line.split(",")
                if len(data) != 3: continue 
                
                x_axis = int(data[0])
                y_axis = int(data[1])
                z_axis = int(data[2]) # Button state (0 = Pressed)
                
                # ---------------------------------------------------------
                # 1. RIGHT (Alt + Tab -> Switch Window)
                # ---------------------------------------------------------
                if x_axis >= 723:
                    if not menu_open:
                        pyautogui.keyDown('alt')
                        pyautogui.press('tab')
                        menu_open = True
                        time.sleep(0.4) 
                    else:
                        pyautogui.press('right')
                        time.sleep(0.4)

                # ---------------------------------------------------------
                # 2. LEFT (Open YouTube)
                # ---------------------------------------------------------
                elif x_axis <= 300:
                    if not web_open:
                        print(f"Opening {URL_TO_OPEN_1}...")
                        
                        webbrowser.open(URL_TO_OPEN_1)
                        
                        """
                        # USE .get() TO FORCE INCOGNITO MODE IF CONFIGURED
                        try:
                            # webbrowser.get(chrome_path).open(URL_TO_OPEN_1) 
                        except:
                            print("Chrome path not found, opening default browser...")
                            webbrowser.open(URL_TO_OPEN_1)
                        """    
                        web_open = True
                        
                        if menu_open:
                            pyautogui.keyUp('alt')
                            menu_open = False
                        

                # ---------------------------------------------------------
                # 3. CENTER (Reset States)
                # ---------------------------------------------------------
                elif 450 < x_axis < 600:
                    if menu_open:
                        pyautogui.keyUp('alt')
                        menu_open = False
                    
                    if web_open:
                        web_open = False

                # ---------------------------------------------------------
                # 4. BUTTON PRESS (Minimize All / Show Desktop)
                # ---------------------------------------------------------
                if z_axis == 0:
                    pyautogui.hotkey('win', 'd')
                    time.sleep(0.5)


                # ---------------------------------------------------------
                # 5. UP (Close Tab - Ctrl + W)
                # ---------------------------------------------------------
                elif y_axis >= 723:
                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(0.5)
                 

                # ---------------------------------------------------------
                # 6. DOWN (Open Netflix)
                # ---------------------------------------------------------
                elif y_axis <= 300:
                    if not web_open:
                        print(f"Opening {URL_TO_OPEN_2}...")
                        
                        try:
                            webbrowser.open(URL_TO_OPEN_2)
                        except:
                            print("Error opening browser...")
                            
                        web_open = True
                        
                        if menu_open:
                            pyautogui.keyUp('alt')
                            menu_open = False
                    

            except ValueError:
                pass 

except serial.SerialException:
    print("Connection Error. Check the USB port.")
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
    pyautogui.keyUp('alt') # Safety release
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()