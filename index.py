#! /usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from functools import partial
from math import sqrt


class App:
    global COR, FONTE
    
    COR =\
        {
            'back': '#c0c0c0',
            'container': '#666',
            'calFrame': '#dddddd',
            'valuesInOut': '#eeeeee',
            'botao': '#333',
            'botaoLetra': '#eee'
        }
    
    FONTE =\
        {
            'valorEntra': ('Manjari', '13', 'bold'),
            'valorSai': ('Manjari', '21', 'bold'),
            'valorSai__ERRO': ('Manjari', '16', 'italic'),
            'botoes': ('Manjari', '12', 'bold'),
            'operador': ('Manjari', '11',),
        }
    
    def __init__(self, root):
        self.wrt  = ''
        self.wrt2 = ''
        # FUNDO
        self.back_frame = Label(root)
        self.back_frame['bg'] = COR['back']
        self.back_frame.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=1)
        # CONTAINER
        self.container_frame = Label(self.back_frame)
        self.container_frame['bg'] = COR['container']
        self.container_frame.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=1, pady=9, padx=9)
        
        # FRAME DOS VALORES A CALCULAR
        self.calcFrame = Frame(self.container_frame)
        self.calcFrame['bg'] = COR['calFrame']
        self.calcFrame.pack(side=TOP, anchor=N, fill=X, pady=12, padx=12)
            # VALORES DE ENTRADA
        self.valores_de_entrada = Listbox(self.calcFrame, selectbackground='#eee', activestyle=UNDERLINE)
        self.valores_de_entrada['height'] = 2
        self.valores_de_entrada['bg'] = COR['valuesInOut']
        self.valores_de_entrada['font'] = FONTE['valorEntra']
        self.valores_de_entrada.pack(side=TOP, anchor=N, fill=X, pady=6, padx=9)
            # VALORES DE SAÍDA
        self.valores_de_saida = Listbox(self.calcFrame, selectbackground='#eee', activestyle=UNDERLINE)
        self.valores_de_saida['justify'] = RIGHT
        self.valores_de_saida['height'] = 2
        self.valores_de_saida['bg'] = COR['valuesInOut']
        self.valores_de_saida['font'] = FONTE['valorSai']
        self.valores_de_saida['justify'] = RIGHT
        self.valores_de_saida.pack(side=BOTTOM, anchor=N, fill=X, pady=6, padx=9)
        
        # BOTÕES NUMÉRICOS
        self.buttonFrame = Frame(self.container_frame)
        self.buttonFrame['bg'] = COR['container']
        self.buttonFrame.pack(side=LEFT, anchor=CENTER, fill=BOTH, pady=12, padx=12)
        # BOTÕES DE SUPERIORES (7 - 9)
        self.bt7_9 = Frame(self.buttonFrame)
        self.bt7_9['bg'] = COR['container']
        self.bt7_9.pack(pady=12)
            # BOTÃO Nº 7
        self.bt7 = Button(self.bt7_9)
        self.bt7['width'] = 4
        self.bt7['bg'] = COR['botao']
        self.bt7['text'] = '7'
        self.bt7['font'] = FONTE['botoes']
        self.bt7['pady'] = 6
        self.bt7['fg'] = COR['botaoLetra']
        self.bt7.pack(side=LEFT, anchor=NW, padx=9)
        self.bt7.bind('<1>', partial(self.escreverNaTela, '7'))
            # BOTÃO Nº 8
        self.bt8 = Button(self.bt7_9)
        self.bt8['width'] = 4
        self.bt8['bg'] = COR['botao']
        self.bt8['text'] = '8'
        self.bt8['font'] = FONTE['botoes']
        self.bt8['pady'] = 6
        self.bt8['fg'] = COR['botaoLetra']
        self.bt8.pack(side=LEFT, anchor=NW,)
        self.bt8.bind('<1>', partial(self.escreverNaTela, '8'))
            # BOTÃO Nº 9
        self.bt9 = Button(self.bt7_9)
        self.bt9['width'] = 4
        self.bt9['bg'] = COR['botao']
        self.bt9['text'] = '9'
        self.bt9['pady'] = 6
        self.bt9['font'] = FONTE['botoes']
        self.bt9['fg'] = COR['botaoLetra']
        self.bt9.pack(side=LEFT, anchor=NW, padx=9)
        self.bt9.bind('<1>', partial(self.escreverNaTela, '9'))
        
        # BOTÃO C (cler)
        self.btClear = Button(self.bt7_9)
        self.btClear['width'] = 4
        self.btClear['bg'] = COR['botao']
        self.btClear['text'] = 'C'
        self.btClear['font'] = FONTE['operador']
        self.btClear['fg'] = COR['botaoLetra']
        self.btClear['pady'] = 6
        self.btClear.pack(side=LEFT, anchor=N)
        self.btClear.config(command=self.clearContent)
        
        # BOTÕES CENTRAIS 1 (4 - 6)
        self.bt4_6 = Frame(self.buttonFrame,)
        self.bt4_6['bg'] = COR['container']
        self.bt4_6.pack()
            # BOTÃO Nº 4
        self.bt4 = Button(self.bt4_6)
        self.bt4['width'] = 4
        self.bt4['bg'] = COR['botao']
        self.bt4['text'] = '4'
        self.bt4['font'] = FONTE['botoes']
        self.bt4['pady'] = 6
        self.bt4['fg'] = COR['botaoLetra']
        self.bt4.pack(side=LEFT, anchor=NW, pady=6, padx=9)
        self.bt4.bind('<1>', partial(self.escreverNaTela, '4'))
            # BOTÃO Nº 5
        self.bt5 = Button(self.bt4_6)
        self.bt5['width'] = 4
        self.bt5['bg'] = COR['botao']
        self.bt5['text'] = '5'
        self.bt5['font'] = FONTE['botoes']
        self.bt5['pady'] = 6
        self.bt5['fg'] = COR['botaoLetra']
        self.bt5.pack(side=LEFT, anchor=NW, pady=6)
        self.bt5.bind('<1>', partial(self.escreverNaTela, '5'))
            # BOTÃO Nº 6
        self.bt6 = Button(self.bt4_6)
        self.bt6['width'] = 4
        self.bt6['bg'] = COR['botao']
        self.bt6['text'] = '6'
        self.bt6['font'] = FONTE['botoes']
        self.bt6['pady'] = 6
        self.bt6['fg'] = COR['botaoLetra']
        self.bt6.pack(side=LEFT, anchor=NW, pady=6, padx=9)
        self.bt6.bind('<1>', partial(self.escreverNaTela, '6'))
        
        # BOTÃO × (multiply)
        self.btTimes = Button(self.bt4_6)
        self.btTimes['padx'] = 6
        self.btTimes['bg'] = COR['botao']
        self.btTimes['text'] = '×'
        self.btTimes['font'] = FONTE['operador']
        self.btTimes['fg'] = COR['botaoLetra']
        self.btTimes['pady'] = 6
        self.btTimes.pack(side=LEFT, anchor=NW, pady=6)
        self.btTimes.bind('<1>', partial(self.escreverNaTela, '×'))
        
        # BOTÃO ÷ (divide)
        self.btDiv = Button(self.bt4_6)
        self.btDiv['padx'] = 6
        self.btDiv['bg'] = COR['botao']
        self.btDiv['text'] = '÷'
        self.btDiv['font'] = FONTE['operador']
        self.btDiv['fg'] = COR['botaoLetra']
        self.btDiv['pady'] = 6
        self.btDiv.pack(side=LEFT, anchor=NW, pady=6, padx=6)
        self.btDiv.bind('<1>', partial(self.escreverNaTela, '÷ '))
        
        # BOTÕES CENTRAIS 2 (1 - 3)
        self.bt1_3 = Frame(self.buttonFrame)
        self.bt1_3['bg'] = COR['container']
        self.bt1_3.pack(pady=12)
            # BOTÃO Nº 1
        self.bt1 = Button(self.bt1_3)
        self.bt1['width'] = 4
        self.bt1['bg'] = COR['botao']
        self.bt1['text'] = '1'
        self.bt1['font'] = FONTE['botoes']
        self.bt1['pady'] = 6
        self.bt1['fg'] = COR['botaoLetra']
        self.bt1.pack(side=LEFT, anchor=NW, padx=9)
        self.bt1.bind('<1>', partial(self.escreverNaTela, '1'))
            # BOTÃO Nº 2
        self.bt2 = Button(self.bt1_3)
        self.bt2['width'] = 4
        self.bt2['bg'] = COR['botao']
        self.bt2['text'] = '2'
        self.bt2['font'] = FONTE['botoes']
        self.bt2['pady'] = 6
        self.bt2['fg'] = COR['botaoLetra']
        self.bt2.pack(side=LEFT, anchor=NW)
        self.bt2.bind('<1>', partial(self.escreverNaTela, '2'))
            # BOTÃO Nº 3
        self.bt3 = Button(self.bt1_3)
        self.bt3['width'] = 4
        self.bt3['bg'] = COR['botao']
        self.bt3['text'] = '3'
        self.bt3['font'] = FONTE['botoes']
        self.bt3['pady'] = 6
        self.bt3['fg'] = COR['botaoLetra']
        self.bt3.pack(side=LEFT, anchor=NW, padx=9)
        self.bt3.bind('<1>', partial(self.escreverNaTela, '3'))
        
        # BOTÃO + (plus)
        self.btSoma = Button(self.bt1_3)
        self.btSoma['padx'] = 6
        self.btSoma['bg'] = COR['botao']
        self.btSoma['text'] = '+'
        self.btSoma['font'] = FONTE['operador']
        self.btSoma['fg'] = COR['botaoLetra']
        self.btSoma['pady'] = 6
        self.btSoma.pack(side=LEFT, anchor=NW)
        self.btSoma.bind('<1>', partial(self.escreverNaTela, '+'))
        # self.btSoma.bind('<1>', partial(self.calcular, '+'))
        
        # BOTÃO - (minus)
        self.btSub = Button(self.bt1_3)
        self.btSub['padx'] = 6
        self.btSub['bg'] = COR['botao']
        self.btSub['text'] = '-'
        self.btSub['font'] = FONTE['operador']
        self.btSub['fg'] = COR['botaoLetra']
        self.btSub['pady'] = 6
        self.btSub.pack(side=LEFT, anchor=NW, padx=4)
        self.btSub.bind('<1>', partial(self.escreverNaTela, '-'))
        # self.btSub.bind('<1>', partial(self.calcular, '-'))
        
        # BOTÕES INFERIORES (0, 00, π)
        self.bt0_Flt = Frame(self.buttonFrame)
        self.bt0_Flt['bg'] = COR['container']
        self.bt0_Flt.pack()
            # BOTÃO 0
        self.bt0 = Button(self.bt0_Flt)
        self.bt0['width'] = 4
        self.bt0['bg'] = COR['botao']
        self.bt0['text'] = '0'
        self.bt0['font'] = FONTE['botoes']
        self.bt0['pady'] = 6
        self.bt0['fg'] = COR['botaoLetra']
        self.bt0.pack(side=LEFT, anchor=NW, pady=6, padx=9)
        self.bt0.bind('<1>', partial(self.escreverNaTela, '0'))
            # BOTÃO , (ponto flutuante)
        self.btFloatPoint = Button(self.bt0_Flt)
        self.btFloatPoint['width'] = 4
        self.btFloatPoint['bg'] = COR['botao']
        self.btFloatPoint['text'] = ','
        self.btFloatPoint['font'] = FONTE['botoes']
        self.btFloatPoint['pady'] = 6
        self.btFloatPoint['fg'] = COR['botaoLetra']
        self.btFloatPoint.pack(side=LEFT, anchor=NW, pady=6)
        self.btFloatPoint.bind('<1>', partial(self.escreverNaTela, ','))
            # BOTÃO √ (raíz quadrada)
        self.btRaizQ = Button(self.bt0_Flt)
        self.btRaizQ['width'] = 4
        self.btRaizQ['bg'] = COR['botao']
        self.btRaizQ['text'] = '√'
        self.btRaizQ['font'] = FONTE['botoes']
        self.btRaizQ['fg'] = COR['botaoLetra']
        self.btRaizQ['pady'] = 6
        self.btRaizQ.pack(side=LEFT, anchor=NW, pady=6, padx=9)
        self.btRaizQ.bind('<1>', partial(self.escreverNaTela, '√'))
            # BOTÃO = (igual)
        self.btIgual = Button(self.bt0_Flt)
        self.btIgual['width'] = 3
        self.btIgual['bg'] = COR['botao']
        self.btIgual['text'] = '='
        self.btIgual['font'] = FONTE['botoes']
        self.btIgual['pady'] = 6
        self.btIgual['fg'] = COR['botaoLetra']
        self.btIgual.pack(side=LEFT, anchor=NW, pady=6)
        self.btIgual.bind('<1>', partial(self.calcular))
        

    def escreverNaTela(self, text, event):
        self.wrt += text
        self.valores_de_entrada.delete(0, 100)
        self.valores_de_entrada.insert(END, self.wrt)
        
        self.valores_de_saida.delete(0, 100)
        self.valores_de_saida['fg'] = 'black'
        self.valores_de_saida['font'] = FONTE['valorSai']
        
        
    def clearContent(self):
        self.valores_de_saida.delete(0, 100)
        self.valores_de_entrada.delete(0, 100)
        self.wrt = ''
    
    def calcular(self, event):
        self.valores_de_saida.delete(0, 100)

        # SOMA OS VALORES
        if '+' in self.wrt and '√' not in self.wrt:
            # pega os valores para calcular
            valorA = self.wrt[:self.wrt.find('+')]
            valorB = self.wrt[self.wrt.find('+')+1:]
            # remove a virgula
            valorA = valorA.replace(',', '.')
            valorB = valorB.replace(',', '.')
            
            # posicaoDoOperador = valores.find('+')
            resultado = f'{float(valorA) + float(valorB)}'
            if float(resultado) % 1 == 0.0:
                resultado = int(float(resultado))
                self.valores_de_saida.insert(END, f"{resultado}")
            else:
                self.valores_de_saida.insert(END, f"{resultado}")
        
        # SUBTRAI OS VALORES
        elif '-' in self.wrt and '√' not in self.wrt:
            # pega os valores para calcular
            valorA = self.wrt[:self.wrt.find('-')]
            valorB = self.wrt[self.wrt.find('-')+1:]
            # remove a virgula
            valorA = valorA.replace(',', '.')
            valorB = valorB.replace(',', '.')
            
            # posicaoDoOperador = valores.find('+')
            resultado = f'{float(valorA) - float(valorB)}'
            if float(resultado) % 1 == 0.0:
                resultado = int(float(resultado))
                self.valores_de_saida.insert(END, f"{resultado}")
            else:
                self.valores_de_saida.insert(END, f"{resultado}")

        # MULTIPLICA OS VALORES
        elif '×' in self.wrt and '√' not in self.wrt:
            # pega os valores para calcular
            valorA = self.wrt[:self.wrt.find('×')]
            valorB = self.wrt[self.wrt.find('×')+1:]
            # remove a virgula
            valorA = valorA.replace(',', '.')
            valorB = valorB.replace(',', '.')
            
            # posicaoDoOperador = valores.find('+')
            resultado = f'{float(valorA) * float(valorB)}'
            if float(resultado) % 1 == 0.0:
                resultado = int(float(resultado))
                self.valores_de_saida.insert(END, f"{resultado}")
            else:
                self.valores_de_saida.insert(END, f"{resultado}")

        # FAZ A DIVISÃO
        elif '÷' in self.wrt and '√' not in self.wrt:
            # pega os valores para calcular
            valorA = self.wrt[:self.wrt.find('÷')]
            valorB = self.wrt[self.wrt.find('÷')+1:]
            # remove a virgula
            valorA = valorA.replace(',', '.')
            valorB = valorB.replace(',', '.')
            
            # posicaoDoOperador = valores.find('+')
            resultado = f'{float(valorA) / float(valorB)}'
            if float(resultado) % 1 == 0.0:
                resultado = int(float(resultado))
                self.valores_de_saida.insert(END, f"{resultado}")
            else:
                self.valores_de_saida.insert(END, f"{resultado:.11}")
        
        # CALCULA  A RAÍZ QUADRADA
        elif (self.wrt[0] == '√') and ('+' not in self.wrt) and ('-' not in self.wrt) and ('×' not in self.wrt) and ('÷' not in self.wrt):
            # remove a raíz e a vírgula
            radicando = self.wrt.replace('√', '')
            radicando = radicando.replace(',', '.')
            resultado = f'{sqrt(float(radicando))}'
            
            if float(resultado) % 1 == 0.0:
                resultado = int(float(resultado))
                self.valores_de_saida.insert(END, f"{resultado}")
            else:
                self.valores_de_saida.insert(END, f"{resultado:.11}")
        
        # ERRO
        else:
            self.valores_de_saida['fg'] = 'red'
            self.valores_de_saida['font'] = FONTE['valorSai__ERRO']
            self.valores_de_saida.insert(END, 'EXPRESSÃO MAL FORMADA')
        
        self.wrt = ''


win = Tk()


win.title('Calculadora')
win.geometry('345x432')
win.maxsize(width=345, height=432)
win.minsize(width=345, height=432)
# CARREGAR AS IMAGENS
icon_image = PhotoImage(file='image/calculator-icon.png')
win.iconphoto(False, icon_image)
App(win)
win.mainloop()
