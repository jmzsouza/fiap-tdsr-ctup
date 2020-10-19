#RESOLUÇÃO DA TELA 1920 X 1080

import pyautogui
import time

# PRESSIONA BOTÃO WINDOWS DO TECLADO
pyautogui.press("win")
time.sleep(2)

# ACESSA O NAVEGADOR CHROME
pyautogui.typewrite("chrome", interval=0.2)
time.sleep(2)
pyautogui.press("enter")
time.sleep(10)
# MAXIMIZA A JANELA
pyautogui.keyDown('alt')
pyautogui.keyDown('space') 
pyautogui.keyDown('x') 
pyautogui.keyUp('x') 
pyautogui.keyUp('space') 
pyautogui.keyUp('alt') 
time.sleep(2)

# ACESSA A BARRA DE ENDEREÇO
pyautogui.moveTo(960, 50, duration=2)
pyautogui.click()
time.sleep(2)

# ACESSA A PAGINA DO FORMULARIO
pyautogui.typewrite("c:/TarefaPyAutoGui/formulario.html", interval=0.2)
pyautogui.press("enter")
time.sleep(2)

# ACESSA O CAMPO NOME
pyautogui.moveTo(960, 350, duration=2)
pyautogui.click()
time.sleep(2)
# ESCREVE NO CAMPO NOME
pyautogui.typewrite("Grupo CONNECTALL", interval=0.2)
pyautogui.press("enter")
time.sleep(1)

# ACESSA O CAMPO EMAIL
pyautogui.moveTo(960, 435, duration=1)
pyautogui.click()
time.sleep(2)
# ESCREVE NO CAMPO EMAIL
pyautogui.typewrite("connectallfiap@gmail.com", interval=0.2)
time.sleep(2)

# SELECIONA UMA OPÇÃO RADIO
pyautogui.moveTo(718, 515, duration=1)
pyautogui.click()
time.sleep(1)

# SELECIONA OS CHECKBOXS
pyautogui.moveTo(1087, 515, duration=1)
pyautogui.click()
pyautogui.moveTo(1087, 540, duration=0.5)
pyautogui.click()
pyautogui.moveTo(1087, 562, duration=0.5)
pyautogui.click()
time.sleep(2)

# ACESSA O SELECT E SELECIONA UM OPTION
pyautogui.moveTo(960, 640, duration=1)
pyautogui.click()
i = 0
while i < 4:
    pyautogui.hotkey("down", interval=0.2)
    i = i + 1
pyautogui.press("enter")
time.sleep(2)

# ACESSA O TEXTAREA
pyautogui.moveTo(960, 755, duration=1)
pyautogui.click()
time.sleep(2)
# ESCREVE NO TEXTAREA
pyautogui.typewrite("CHECKPOINT 2 - TAREFA PYAUTOGUI", interval=0.2)
pyautogui.press("enter")
pyautogui.typewrite("Esse formulario esta sendo preenchido automaticamente atraves de codigo em Python utilizando a biblioteca PyAutoGui", interval=0.2)
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.typewrite("Integrantes:", interval=0.2)
pyautogui.press("enter")
pyautogui.typewrite("Alice Russolo Losacco", interval=0.2)
pyautogui.press("enter")
pyautogui.typewrite("Ingrid Pinheiro Goncalves", interval=0.2)
pyautogui.press("enter")
pyautogui.typewrite("Joao Pedro Lombardi Vieira Soares", interval=0.2)
pyautogui.press("enter")
pyautogui.typewrite("Jonas Muniz de Souza", interval=0.2)
time.sleep(2)

# ACESSA E CLICA NO BOTAO ENVIAR
pyautogui.moveTo(960, 830, duration=1)
pyautogui.click()
time.sleep(2)