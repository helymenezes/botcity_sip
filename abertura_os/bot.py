import pandas as pd
import tkinter as tk
import time
from tkinter import messagebox
from botcity.core import DesktopBot
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    
    path_excel = r'abertura_os\abrir.xlsx'
    
    try:
        cad = pd.read_excel(path_excel)
    except FileNotFoundError:
        print(f"File not found: {path_excel}")
        return
    
    # Print the columns of the DataFrame to debug the KeyError
    print("Columns in the Excel file:", cad.columns)
    
    # Use the correct column name from the printed columns
    # Adjust the column name as necessary based on the output
    if 'IDSERVICOSCONJ' in cad.columns:
        data = cad[['IDSERVICOSCONJ']]
        data['IDSERVICOSCONJ'] = data['IDSERVICOSCONJ'].astype(str)
    else:
        print("Column 'IDSERVICOSCONJ' not found in the Excel file.")
        return
    
    bot.execute(r'C:\Users\Usuario\OneDrive - ONE ENGENHARIA INDUSTRIA E COMERCIO LTDA\Área de Trabalho\Gestao Produção.appref-ms')
    if not bot.find( "iserir_usuario", matching=0.97, waiting_time=10000):
        not_found("iserir_usuario")
        return
    bot.click()
    bot.paste('hely')
    bot.enter()
    bot.paste('hrs500')
    bot.enter()
    bot.enter()
    if not bot.find( "selecionar_servicos", matching=0.97, waiting_time=10000):
        not_found("selecionar_servicos")
        return
    bot.move()
    bot.click()
    if not bot.find( "selecionar_pesquisar_iniciar_os", matching=0.97, waiting_time=10000):
        not_found("selecionar_pesquisar_iniciar_os")
        return
    bot.click()    
    bot.move()
    bot.click()
    if not bot.find( "selecionar_id_one", matching=0.97, waiting_time=10000):
        not_found("selecionar_id_one")
        return
    bot.move()
    bot.click()

    start_process(bot, data)
    
def start_process(bot, data):
    while True:
        for i, row in data.iterrows():
            codigo_one = row['IDSERVICOSCONJ']  # Ajuste conforme o nome da coluna correta  

            bot.kb_type(codigo_one)
            time.sleep(5)
            bot.tab()
            time.sleep(5)
            bot.enter()  # Pressiona enter para 
            
            
            time.sleep(5)
            if not bot.find_text( "novo+", threshold=130, waiting_time=10000):
                not_found("novo+")
            bot.move()
            bot.click()
            time.sleep(5)
            
            if not bot.find( "incluir_novo_registro", matching=0.97, waiting_time=50000):
                not_found("incluir_novo_registro")
                return  # Reinicia o loop ao encontrar um elemento não encontrado
            bot.move()
            bot.click()
            bot.enter(presses=7)
            time.sleep(5)
            for _ in range(3):
                bot.type_down()
            bot.enter()
            bot.type_down()
            bot.enter()
            time.sleep(5)
            for _ in range(9):
                bot.type_down()
            bot.enter()
            time.sleep(5)
            for _ in range(4):
                bot.type_down()
            time.sleep(5)
            if not bot.find( "save", matching=0.97, waiting_time=10000):
                not_found("save")
                return  # Reinicia o loop ao encontrar um elemento não encontrado
            bot.move()
            bot.click(wait_after=30000)
            bot.enter()

            time.sleep(10)

            if not bot.find( "enter_close", matching=0.97, waiting_time=10000):
                not_found("enter_close")
                return  # Reinicia o loop ao encontrar um elemento não encontrado
            bot.move()
            bot.click()

            time.sleep(30)
            
            if not bot.find_text( "closed_cad", threshold=230, waiting_time=10000):
                not_found("closed_cad")
            bot.move()
            bot.click()
            
            time.sleep(30)
            
            if i == len(data) - 1:
                alert(f'O último número do Código ONE é {codigo_one}')
                break  # Reinicia o loop

def not_found(label):
    print(f"Element not found: {label}")

def alert(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Alerta", message)
    root.destroy()

if __name__ == '__main__':
    main()
