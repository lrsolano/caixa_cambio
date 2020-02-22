# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:34:44 2018

@author: Leonardo Ribeiro
"""

#importação dos modulos
from tkinter import *
from tkinter import ttk
import serial
import time
from tkinter import messagebox

class menu():
    def __init__(self,parent):
        self.parent=parent
        self.Menu(parent)
        self.idxs = ""
    def Menu(self,parent):
        #abre a porta serial ao iniciar o programa
        self.ser = serial.Serial('COM5', 9600)
        self.marcs = []
        self.solenoide_serial0 = []
        #le p arquivo de texto contendo as informações
        try:
            with open('marcas.txt','r') as bd:
                
                for linhas in bd:
                    try:
                        #separa em marca e os comandos
                        (marca,solenoide)=linhas.split('=')
                        self.marcs.append(marca)
                        self.solenoide_serial0.append(solenoide) 
                    except ValueError:
                        pass
        except IOError as perr:
            return "Arquivo não econtrado"+str(perr)
        except EOFError as eoferr:
            pass
        #definindo a tela
        self.content=ttk.Frame(root, padding="3 3 12 12")
        self.content.grid(column=0, row=0, sticky=(N, W, E, S))
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(5, weight=1)
        
        #adicionando list box
        cnames = StringVar(value=self.marcs)      
        self.lbox = Listbox(self.content, listvariable=cnames, height=5)
        self.lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
        s = ttk.Scrollbar(root, orient=VERTICAL, command=self.lbox.yview)
        s.grid(column=1, row=0, sticky=(N,S))
        self.lbox['yscrollcommand'] = s.set
        
        #adicionando os botões
        Button(self.parent, text='Cadastrar', command=self.Cadastrar).grid(column=0,row=2, sticky=W)
        Button(self.parent, text='Enviar', command=self.Enviar).grid(column=1,row=2, sticky=W)
     
        #Tela de cadastro
    def Cadastrar(self):
        self.c=Toplevel(self.parent)
        self.c.title("Cadastrar novo Modelo")
        
        
        self.nome=ttk.Label(self.c,text='Nome:').grid(column=0,row=1,padx=(0,3),pady=5)
        self.nome_entry= ttk.Entry(self.c, width=30)
        self.nome_entry.grid(column=1,row=1,padx=(0,3),pady=5, columnspan = 7)
        
        #TABELA
        self.marchas=ttk.Label(self.c,text='MARCHAS').grid(column=0,row=2,padx=(5,3),pady=5)
        self.fl=ttk.Label(self.c,text='FL').grid(column=1,row=2,padx=(5,3),pady=5, sticky=W)
        self.fh=ttk.Label(self.c,text='FH').grid(column=2,row=2,padx=(5,3),pady=5, sticky=W)
        self.fh=ttk.Label(self.c,text='R').grid(column=3,row=2,padx=(5,3),pady=5, sticky=W)
        self.fh=ttk.Label(self.c,text='1').grid(column=4,row=2,padx=(5,3),pady=5, sticky=W)
        self.fh=ttk.Label(self.c,text='2').grid(column=5,row=2,padx=(5,3),pady=5, sticky=W)
        self.fh=ttk.Label(self.c,text='3').grid(column=6,row=2,padx=(5,3),pady=5, sticky=W)
        self.fh=ttk.Label(self.c,text='4').grid(column=7,row=2,padx=(5,3),pady=5, sticky=W)
        
        self.marchas=ttk.Label(self.c,text='F1').grid(column=0,row=3,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='F2').grid(column=0,row=4,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='F3').grid(column=0,row=5,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='F4').grid(column=0,row=6,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='F5').grid(column=0,row=7,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='F6').grid(column=0,row=8,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='F7').grid(column=0,row=9,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='F8').grid(column=0,row=10,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='R1').grid(column=0,row=11,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='R2').grid(column=0,row=12,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='R3').grid(column=0,row=13,padx=(5,3),pady=5)
        self.marchas=ttk.Label(self.c,text='R4').grid(column=0,row=14,padx=(5,3),pady=5)
        
        #CHECKBUTTONS F1
        self.var1_fl = IntVar()
        Checkbutton(self.c, variable=self.var1_fl, onvalue=1, offvalue=0).grid(column=1,row=3, sticky=W)
        self.var1_fh = IntVar()
        Checkbutton(self.c, variable=self.var1_fh, onvalue=2, offvalue=0).grid(column=2,row=3, sticky=W)
        self.var1_r = IntVar()
        Checkbutton(self.c, variable=self.var1_r, onvalue=3, offvalue=0).grid(column=3,row=3, sticky=W)
        self.var1_1 = IntVar()
        Checkbutton(self.c, variable=self.var1_1, onvalue=4, offvalue=0).grid(column=4,row=3, sticky=W)
        self.var1_2 = IntVar()
        Checkbutton(self.c, variable=self.var1_2, onvalue=5, offvalue=0).grid(column=5,row=3, sticky=W)
        self.var1_3 = IntVar()
        Checkbutton(self.c, variable=self.var1_3, onvalue=6, offvalue=0).grid(column=6,row=3, sticky=W)
        self.var1_4 = IntVar()
        Checkbutton(self.c, variable=self.var1_4, onvalue=7, offvalue=0).grid(column=7,row=3, sticky=W)
        
        #CHECKBUTTONS F2
        self.var2_fl = IntVar()
        Checkbutton(self.c, variable=self.var2_fl, onvalue=1, offvalue=0).grid(column=1,row=4, sticky=W)
        self.var2_fh = IntVar()
        Checkbutton(self.c, variable=self.var2_fh, onvalue=2, offvalue=0).grid(column=2,row=4, sticky=W)
        self.var2_r = IntVar()
        Checkbutton(self.c, variable=self.var2_r, onvalue=3, offvalue=0).grid(column=3,row=4, sticky=W)
        self.var2_1 = IntVar()
        Checkbutton(self.c, variable=self.var2_1, onvalue=4, offvalue=0).grid(column=4,row=4, sticky=W)
        self.var2_2 = IntVar()
        Checkbutton(self.c, variable=self.var2_2, onvalue=5, offvalue=0).grid(column=5,row=4, sticky=W)
        self.var2_3 = IntVar()
        Checkbutton(self.c, variable=self.var2_3, onvalue=6, offvalue=0).grid(column=6,row=4, sticky=W)
        self.var2_4 = IntVar()
        Checkbutton(self.c, variable=self.var2_4, onvalue=7, offvalue=0).grid(column=7,row=4, sticky=W)
        
        #CHECKBUTTONS F3
        self.var3_fl = IntVar()
        Checkbutton(self.c, variable=self.var3_fl, onvalue=1, offvalue=0).grid(column=1,row=5, sticky=W)
        self.var3_fh = IntVar()
        Checkbutton(self.c, variable=self.var3_fh, onvalue=2, offvalue=0).grid(column=2,row=5, sticky=W)
        self.var3_r = IntVar()
        Checkbutton(self.c, variable=self.var3_r, onvalue=3, offvalue=0).grid(column=3,row=5, sticky=W)
        self.var3_1 = IntVar()
        Checkbutton(self.c, variable=self.var3_1, onvalue=4, offvalue=0).grid(column=4,row=5, sticky=W)
        self.var3_2 = IntVar()
        Checkbutton(self.c, variable=self.var3_2, onvalue=5, offvalue=0).grid(column=5,row=5, sticky=W)
        self.var3_3 = IntVar()
        Checkbutton(self.c, variable=self.var3_3, onvalue=6, offvalue=0).grid(column=6,row=5, sticky=W)
        self.var3_4 = IntVar()
        Checkbutton(self.c, variable=self.var3_4, onvalue=7, offvalue=0).grid(column=7,row=5, sticky=W)
        
        
        #CHECKBUTTONS F4
        self.var4_fl = IntVar()
        Checkbutton(self.c, variable=self.var4_fl, onvalue=1, offvalue=0).grid(column=1,row=6, sticky=W)
        self.var4_fh = IntVar()
        Checkbutton(self.c, variable=self.var4_fh, onvalue=2, offvalue=0).grid(column=2,row=6, sticky=W)
        self.var4_r = IntVar()
        Checkbutton(self.c, variable=self.var4_r, onvalue=3, offvalue=0).grid(column=3,row=6, sticky=W)
        self.var4_1 = IntVar()
        Checkbutton(self.c, variable=self.var4_1, onvalue=4, offvalue=0).grid(column=4,row=6, sticky=W)
        self.var4_2 = IntVar()
        Checkbutton(self.c, variable=self.var4_2, onvalue=5, offvalue=0).grid(column=5,row=6, sticky=W)
        self.var4_3 = IntVar()
        Checkbutton(self.c, variable=self.var4_3, onvalue=6, offvalue=0).grid(column=6,row=6, sticky=W)
        self.var4_4 = IntVar()
        Checkbutton(self.c, variable=self.var4_4, onvalue=7, offvalue=0).grid(column=7,row=6, sticky=W)
        
        #CHECKBUTTONS F5
        self.var5_fl = IntVar()
        Checkbutton(self.c, variable=self.var5_fl, onvalue=1, offvalue=0).grid(column=1,row=7, sticky=W)
        self.var5_fh = IntVar()
        Checkbutton(self.c, variable=self.var5_fh, onvalue=2, offvalue=0).grid(column=2,row=7, sticky=W)
        self.var5_r = IntVar()
        Checkbutton(self.c, variable=self.var5_r, onvalue=3, offvalue=0).grid(column=3,row=7, sticky=W)
        self.var5_1 = IntVar()
        Checkbutton(self.c, variable=self.var5_1, onvalue=4, offvalue=0).grid(column=4,row=7, sticky=W)
        self.var5_2 = IntVar()
        Checkbutton(self.c, variable=self.var5_2, onvalue=5, offvalue=0).grid(column=5,row=7, sticky=W)
        self.var5_3 = IntVar()
        Checkbutton(self.c, variable=self.var5_3, onvalue=6, offvalue=0).grid(column=6,row=7, sticky=W)
        self.var5_4 = IntVar()
        Checkbutton(self.c, variable=self.var5_4, onvalue=7, offvalue=0).grid(column=7,row=7, sticky=W)
        
        #CHECKBUTTONS F6
        self.var6_fl = IntVar()
        Checkbutton(self.c, variable=self.var6_fl, onvalue=1, offvalue=0).grid(column=1,row=8, sticky=W)
        self.var6_fh = IntVar()
        Checkbutton(self.c, variable=self.var6_fh, onvalue=2, offvalue=0).grid(column=2,row=8, sticky=W)
        self.var6_r = IntVar()
        Checkbutton(self.c, variable=self.var6_r, onvalue=3, offvalue=0).grid(column=3,row=8, sticky=W)
        self.var6_1 = IntVar()
        Checkbutton(self.c, variable=self.var6_1, onvalue=4, offvalue=0).grid(column=4,row=8, sticky=W)
        self.var6_2 = IntVar()
        Checkbutton(self.c, variable=self.var6_2, onvalue=5, offvalue=0).grid(column=5,row=8, sticky=W)
        self.var6_3 = IntVar()
        Checkbutton(self.c, variable=self.var6_3, onvalue=6, offvalue=0).grid(column=6,row=8, sticky=W)
        self.var6_4 = IntVar()
        Checkbutton(self.c, variable=self.var6_4, onvalue=7, offvalue=0).grid(column=7,row=8, sticky=W)
        
        
        #CHECKBUTTONS F7
        self.var7_fl = IntVar()
        Checkbutton(self.c, variable=self.var7_fl, onvalue=1, offvalue=0).grid(column=1,row=9, sticky=W)
        self.var7_fh = IntVar()
        Checkbutton(self.c, variable=self.var7_fh, onvalue=2, offvalue=0).grid(column=2,row=9, sticky=W)
        self.var7_r = IntVar()
        Checkbutton(self.c, variable=self.var7_r, onvalue=3, offvalue=0).grid(column=3,row=9, sticky=W)
        self.var7_1 = IntVar()
        Checkbutton(self.c, variable=self.var7_1, onvalue=4, offvalue=0).grid(column=4,row=9, sticky=W)
        self.var7_2 = IntVar()
        Checkbutton(self.c, variable=self.var7_2, onvalue=5, offvalue=0).grid(column=5,row=9, sticky=W)
        self.var7_3 = IntVar()
        Checkbutton(self.c, variable=self.var7_3, onvalue=6, offvalue=0).grid(column=6,row=9, sticky=W)
        self.var7_4 = IntVar()
        Checkbutton(self.c, variable=self.var7_4, onvalue=7, offvalue=0).grid(column=7,row=9, sticky=W)
        
        
        #CHECKBUTTONS F8
        self.var8_fl = IntVar()
        Checkbutton(self.c, variable=self.var8_fl, onvalue=1, offvalue=0).grid(column=1,row=10, sticky=W)
        self.var8_fh = IntVar()
        Checkbutton(self.c, variable=self.var8_fh, onvalue=2, offvalue=0).grid(column=2,row=10, sticky=W)
        self.var8_r = IntVar()
        Checkbutton(self.c, variable=self.var8_r, onvalue=3, offvalue=0).grid(column=3,row=10, sticky=W)
        self.var8_1 = IntVar()
        Checkbutton(self.c, variable=self.var8_1, onvalue=4, offvalue=0).grid(column=4,row=10, sticky=W)
        self.var8_2 = IntVar()
        Checkbutton(self.c, variable=self.var8_2, onvalue=5, offvalue=0).grid(column=5,row=10, sticky=W)
        self.var8_3 = IntVar()
        Checkbutton(self.c, variable=self.var8_3, onvalue=6, offvalue=0).grid(column=6,row=10, sticky=W)
        self.var8_4 = IntVar()
        Checkbutton(self.c, variable=self.var8_4, onvalue=7, offvalue=0).grid(column=7,row=10, sticky=W)
        
         #CHECKBUTTONS R1
        self.var9_fl = IntVar()
        Checkbutton(self.c, variable=self.var9_fl, onvalue=1, offvalue=0).grid(column=1,row=11, sticky=W)
        self.var9_fh = IntVar()
        Checkbutton(self.c, variable=self.var9_fh, onvalue=2, offvalue=0).grid(column=2,row=11, sticky=W)
        self.var9_r = IntVar()
        Checkbutton(self.c, variable=self.var9_r, onvalue=3, offvalue=0).grid(column=3,row=11, sticky=W)
        self.var9_1 = IntVar()
        Checkbutton(self.c, variable=self.var9_1, onvalue=4, offvalue=0).grid(column=4,row=11, sticky=W)
        self.var9_2 = IntVar()
        Checkbutton(self.c, variable=self.var9_2, onvalue=5, offvalue=0).grid(column=5,row=11, sticky=W)
        self.var9_3 = IntVar()
        Checkbutton(self.c, variable=self.var9_3, onvalue=6, offvalue=0).grid(column=6,row=11, sticky=W)
        self.var9_4 = IntVar()
        Checkbutton(self.c, variable=self.var9_4, onvalue=7, offvalue=0).grid(column=7,row=11, sticky=W)
        
        #CHECKBUTTONS R2
        self.var10_fl = IntVar()
        Checkbutton(self.c, variable=self.var10_fl, onvalue=1, offvalue=0).grid(column=1,row=12, sticky=W)
        self.var10_fh = IntVar()
        Checkbutton(self.c, variable=self.var10_fh, onvalue=2, offvalue=0).grid(column=2,row=12, sticky=W)
        self.var10_r = IntVar()
        Checkbutton(self.c, variable=self.var10_r, onvalue=3, offvalue=0).grid(column=3,row=12, sticky=W)
        self.var10_1 = IntVar()
        Checkbutton(self.c, variable=self.var10_1, onvalue=4, offvalue=0).grid(column=4,row=12, sticky=W)
        self.var10_2 = IntVar()
        Checkbutton(self.c, variable=self.var10_2, onvalue=5, offvalue=0).grid(column=5,row=12, sticky=W)
        self.var10_3 = IntVar()
        Checkbutton(self.c, variable=self.var10_3, onvalue=6, offvalue=0).grid(column=6,row=12, sticky=W)
        self.var10_4 = IntVar()
        Checkbutton(self.c, variable=self.var10_4, onvalue=7, offvalue=0).grid(column=7,row=12, sticky=W)
        
        #CHECKBUTTONS R3
        self.var11_fl = IntVar()
        Checkbutton(self.c, variable=self.var11_fl, onvalue=1, offvalue=0).grid(column=1,row=13, sticky=W)
        self.var11_fh = IntVar()
        Checkbutton(self.c, variable=self.var11_fh, onvalue=2, offvalue=0).grid(column=2,row=13, sticky=W)
        self.var11_r = IntVar()
        Checkbutton(self.c, variable=self.var11_r, onvalue=3, offvalue=0).grid(column=3,row=13, sticky=W)
        self.var11_1 = IntVar()
        Checkbutton(self.c, variable=self.var11_1, onvalue=4, offvalue=0).grid(column=4,row=13, sticky=W)
        self.var11_2 = IntVar()
        Checkbutton(self.c, variable=self.var11_2, onvalue=5, offvalue=0).grid(column=5,row=13, sticky=W)
        self.var11_3 = IntVar()
        Checkbutton(self.c, variable=self.var11_3, onvalue=6, offvalue=0).grid(column=6,row=13, sticky=W)
        self.var11_4 = IntVar()
        Checkbutton(self.c, variable=self.var11_4, onvalue=7, offvalue=0).grid(column=7,row=13, sticky=W)
        
        #CHECKBUTTONS R4
        self.var12_fl = IntVar()
        Checkbutton(self.c, variable=self.var12_fl, onvalue=1, offvalue=0).grid(column=1,row=14, sticky=W)
        self.var12_fh = IntVar()
        Checkbutton(self.c, variable=self.var12_fh, onvalue=2, offvalue=0).grid(column=2,row=14, sticky=W)
        self.var12_r = IntVar()
        Checkbutton(self.c, variable=self.var12_r, onvalue=3, offvalue=0).grid(column=3,row=14, sticky=W)
        self.var12_1 = IntVar()
        Checkbutton(self.c, variable=self.var12_1, onvalue=4, offvalue=0).grid(column=4,row=14, sticky=W)
        self.var12_2 = IntVar()
        Checkbutton(self.c, variable=self.var12_2, onvalue=5, offvalue=0).grid(column=5,row=14, sticky=W)
        self.var12_3 = IntVar()
        Checkbutton(self.c, variable=self.var12_3, onvalue=6, offvalue=0).grid(column=6,row=14, sticky=W)
        self.var12_4 = IntVar()
        Checkbutton(self.c, variable=self.var12_4, onvalue=7, offvalue=0).grid(column=7,row=14, sticky=W)
        
        
        
        
        Button(self.c, text='SALVAR', command=self.Salvar).grid(column=3,row=15, sticky=W,columnspan=8)
    
    #função para salvar no txt    
    def Salvar (self):
        
        #une todas as opções do checkbox em uma string
        self.primeira_parte_texto = ""
        self.primeira_parte_texto =  str(self.var1_fl.get())+str(self.var1_fh.get())+str(self.var1_r.get())+str(self.var1_1.get())+str(self.var1_2.get())+str(self.var1_3.get())+str(self.var1_4.get())
        self.primeira_parte_texto += str(self.var2_fl.get())+str(self.var2_fh.get())+str(self.var2_r.get())+str(self.var2_1.get())+str(self.var2_2.get())+str(self.var2_3.get())+str(self.var2_4.get())
        self.primeira_parte_texto += str(self.var3_fl.get())+str(self.var3_fh.get())+str(self.var3_r.get())+str(self.var3_1.get())+str(self.var3_2.get())+str(self.var3_3.get())+str(self.var3_4.get())
        self.primeira_parte_texto += str(self.var4_fl.get())+str(self.var4_fh.get())+str(self.var4_r.get())+str(self.var4_1.get())+str(self.var4_2.get())+str(self.var4_3.get())+str(self.var4_4.get())
        self.primeira_parte_texto += str(self.var5_fl.get())+str(self.var5_fh.get())+str(self.var5_r.get())+str(self.var5_1.get())+str(self.var5_2.get())+str(self.var5_3.get())+str(self.var5_4.get())
        self.primeira_parte_texto += str(self.var6_fl.get())+str(self.var6_fh.get())+str(self.var6_r.get())+str(self.var6_1.get())+str(self.var6_2.get())+str(self.var6_3.get())+str(self.var6_4.get())
        self.primeira_parte_texto += str(self.var7_fl.get())+str(self.var7_fh.get())+str(self.var7_r.get())+str(self.var7_1.get())+str(self.var7_2.get())+str(self.var7_3.get())+str(self.var7_4.get())
        self.primeira_parte_texto += str(self.var8_fl.get())+str(self.var8_fh.get())+str(self.var8_r.get())+str(self.var8_1.get())+str(self.var8_2.get())+str(self.var8_3.get())+str(self.var8_4.get())
        self.primeira_parte_texto += str(self.var9_fl.get())+str(self.var9_fh.get())+str(self.var9_r.get())+str(self.var9_1.get())+str(self.var9_2.get())+str(self.var9_3.get())+str(self.var9_4.get())
        self.primeira_parte_texto += str(self.var10_fl.get())+str(self.var10_fh.get())+str(self.var10_r.get())+str(self.var10_1.get())+str(self.var10_2.get())+str(self.var10_3.get())+str(self.var10_4.get())
        self.primeira_parte_texto += str(self.var11_fl.get())+str(self.var11_fh.get())+str(self.var11_r.get())+str(self.var11_1.get())+str(self.var11_2.get())+str(self.var11_3.get())+str(self.var11_4.get())
        self.primeira_parte_texto += str(self.var12_fl.get())+str(self.var12_fh.get())+str(self.var12_r.get())+str(self.var12_1.get())+str(self.var12_2.get())+str(self.var12_3.get())+str(self.var12_4.get())
        
        #retorna a marca cadastrada
        self.marca = str(self.nome_entry.get())
        
        print(self.marca)
        print(self.primeira_parte_texto)
        
        #abre o arquivo para salvar
        with open('marcas.txt','a') as lee:
            print(str(self.marca)+'='+str(self.primeira_parte_texto), file=lee)
            print("Salvei")  
         
        #insere na lista e no listbox
        self.solenoide_serial0.append(self.primeira_parte_texto) 
        self.lbox.insert(len(self.solenoide_serial0),self.marca)
        
    #Função para enviar os dados    
    def Enviar(self):
        #retorna o valor escolhido do listbox
        escolhido = self.lbox.curselection()
        print (escolhido)
        if len(escolhido) >= 1:
            #retorna o id da marca do escolhido            
            id_escolhido= int(escolhido[0])
            #recupera a string
            texto = str(self.solenoide_serial0[id_escolhido])
            #divide a string em duas partes
            primeira_parte = texto[:42]
            segunda_parte = texto[42:]
            #envia a string via serial
            try:
                self.ser.write(primeira_parte.encode())
                print(primeira_parte) 
                time.sleep(3.1)    
                self.ser.write(segunda_parte.encode())
                print(segunda_parte)
                print("enviado")
            except:
                print("erro")
                pass
            
           
            
    
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    root.title("CAMBIO")
    menu(root)
    root.mainloop()


