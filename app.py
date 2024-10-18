# importando biblioteca de automação
# há a necessidade de instalação 'pip install pyautogui'
import pyautogui as auto

auto.PAUSE = 1.0

auto.press("win")
auto.write("chrome")
auto.press("enter")
auto.hotkey("alt", "space")
auto.press("x")
auto.write("Python.org")
auto.press("enter")
auto.hotkey("ctrl","t")
auto.write("google.com.br")
auto.press("enter")
auto.write("logo python")
auto.press("enter")

for i in range(14):
    auto.press("tab")

auto.press("enter")

# gerar executável: instalar a biblioteca 'cx_Freeze'
# comando para gerar o executável: cxfreeze app.py --target-dir nome-pasta