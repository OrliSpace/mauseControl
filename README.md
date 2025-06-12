# mauseControl

##How to run the project?

- pip install -r requirements.txt
- create .env file with the verables:
    SERVER_IP=
    SERVER_PORT=12345


python - move mause

pyautogui.moveTo(400, 300)       # מזיז את הסמן למיקום (x, y)
pyautogui.mouseDown()            # לוחץ (מבלי לשחרר)
pyautogui.mouseUp()              # משחרר לחיצה
pyautogui.rightClick()           # לחיצה ימנית
pyautogui.doubleClick()          # לחיצה כפולה

pyautogui.FAILSAFE = True (ברירת מחדל) שמפסיק את הסקריפט אם הסמן מגיע לפינה השמאלית העליונה של המסך.