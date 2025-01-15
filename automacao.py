#https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Passo 1: abrir sistema da empresa
#Passo 2: logar
#Passo 3: importar base de dados
#passo 5: repetir passso 4 até acabar

import pyautogui as pag
from time import sleep
pag.PAUSE = 0.3

pag.press('win')

pag.write('opera')

pag.press('enter')

pag.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

pag.press('enter')

sleep(3)

pag.click(x=614, y=362)

pag.write('leoziho@google.com')
pag.press('tab')

pag.write('12345678')

pag.click(x=806, y=523)
import pandas as pd

produtos = r'C:\Users\leona\Documents\GitHub\Automacao\produtos.csv'
base = pd.read_csv(produtos)
sleep(1)
pag.press('tab')

