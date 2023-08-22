import pyautogui
import pyperclip
import pandas as pd
import time

# Passo 1: Entrar no sistema da empresa (Link)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(2)
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('enter')
time.sleep(5)

# Passo 2: Fazer Login
# print(pyautogui.position())
pyautogui.click(x=3466, y=402)
pyautogui.write('admin')
time.sleep(1)
pyautogui.click(x=3478, y=467)
pyautogui.write('admin')
time.sleep(1)
pyautogui.click(x=3540, y=541)

# Passo 3: Exportar base de dados
time.sleep(2)
pyautogui.click(x=2965, y=484)
time.sleep(2)
pyautogui.click(x=3045, y=261)

# Passo 4: Calcular os indicadores
tabela = pd.read_csv(r'C:\Users\eurcvf\Desktop\Arquivos\Cursos\hashtag\python\projetos\automacao_controle_custos\Compras.csv', sep=';')

total_gasto = tabela['ValorFinal'].sum()
quantidade = tabela['Quantidade'].sum()
ticket_medio = (total_gasto / quantidade)
print(total_gasto)
print(quantidade)
print(ticket_medio)

# Passo 5: Enviar um e-mail para o diretor da empresa
time.sleep(5)
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://outlook.live.com/mail/0/')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x=2697, y=203)

time.sleep(3)
pyautogui.click(x=3321, y=326)
pyautogui.write('meuemail@gmail.com')
pyautogui.press('tab')

time.sleep(2)
pyperclip.copy('Relatório | Cálculo de Vendas')
pyautogui.hotkey('ctrl', 'v')

corpo_email = f'''

  Prezado,
  
  Segue o relatório de compras.
  
  T. Gasto: R${total_gasto:,.0f}
  Qtde Produtos: {quantidade:,.0f}
  Ticket Médio: R${ticket_medio:,.0f}
  
  Qualquer dúvida estou à disposição.
  
  Atenciosamente,
  Roberto | Analista de Dados.

'''

time.sleep(5)
pyautogui.press('tab')
pyperclip.copy(corpo_email)
pyautogui.hotkey('ctrl', 'v')

# Clicar em enviar
time.sleep(1)
pyautogui.hotkey('ctrl', 'enter')


