import customtkinter 
def logar():
    email_texto=email.get()
    senha_texto= senha.get()


    if not email_texto or not senha_texto:
        print('DIGITE SUA SENHA E/OU EMAIL')
    else:
        print('VOCÊ FOI LOGADO')



janela=customtkinter.CTk()
janela.geometry("300x200")

texto=customtkinter.CTkLabel(janela,text='TELA DE LOGIN')
texto.pack(padx=10,pady=10)

email=customtkinter.CTkEntry(janela,placeholder_text='SEU EMAIL')
email.pack(pady=10,padx=10)

senha=customtkinter.CTkEntry(janela,placeholder_text='SUA SENHA',show='*')
senha.pack(pady=10,padx=10)

botao=customtkinter.CTkButton(janela,text='logar',command=logar)
botao.pack(pady=10,padx=10)



janela.mainloop()