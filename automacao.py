#https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Passo 1: abrir sistema da empresa
#Passo 2: logar
#Passo 3: importar base de dados
#passo 5: repetir passso 4 até acabar

import pyautogui as pag
from time import sleep
import pandas as pd

produtos = r'C:\Users\leona\Documents\GitHub\Automacao\produtos.csv'
base = pd.read_csv(produtos)
pag.PAUSE = 0.4

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


sleep(1)
for linha in base.index:
    pag.click(x=585, y=242)
    codigo = base.loc[linha, 'codigo']
    pag.write(str(codigo))
   
    pag.press('tab')
    marca = base.loc[linha, 'marca']
    pag.write(str(marca))
    pag.press('tab')

    tipo = base.loc[linha, 'tipo']
    pag.write(str(tipo))
    pag.press('tab')

    categoria = base.loc[linha, 'categoria']
    pag.write(str(categoria))
    pag.press('tab')

    preco_unitario = base.loc[linha, 'preco_unitario']
    pag.write(str(preco_unitario))
    pag.press('tab')

    custo = base.loc[linha, 'custo']
    pag.write(str(custo))
    pag.press('tab')

    obs = base.loc[linha, 'obs']
    if obs != 'nan':
        pag.write(str(obs))
    else:
        pag.write('')
    pag.scroll(1000)
    pag.press('enter')

