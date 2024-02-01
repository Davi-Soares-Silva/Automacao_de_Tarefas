import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.5
data_frame = pd.read_csv("planilha.csv", delimiter = ";")
pyautogui.press("win")
pyautogui.write("Emitir_Nota")
pyautogui.press("backspace")
pyautogui.press("enter")
time.sleep(2)

for linha in data_frame.index:
    
    pyautogui.click(x=563, y=265)

    pyautogui.write(data_frame.loc[linha, "Data_emissao"])
    pyautogui.press("tab")

    pyautogui.write(str(data_frame.loc[linha, "Codigo_pedido"]))   
    pyautogui.press("tab")

    pyautogui.write(data_frame.loc[linha, "Nome_Cliente"])
    pyautogui.press("tab")

    pyautogui.write(str(data_frame.loc[linha, "Endereco"]))
    pyautogui.press("tab")

    pyautogui.write(str(data_frame.loc[linha, "Codigo_Produto"]))
    pyautogui.press("tab")

    pyautogui.write(data_frame.loc[linha, "Nome_Produto"])
    pyautogui.press("tab")

    pyautogui.write(str(data_frame.loc[linha, "Valor"]))
    pyautogui.press("tab")

    pyautogui.write(str(data_frame.loc[linha, "Quantidade"]))
    pyautogui.press("tab")

    pyautogui.write(str(data_frame.loc[linha, "Valor_Total"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)




