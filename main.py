from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showerror, showinfo
import pyqrcode
from PIL import Image
from os import path

# funções do programa


def makeqrcode():
    """
    -> Função que gera qrcode;
    A função não possui parâmetros, pois acessa a url por meio do método get;
    Após gerar o qrcode, é atribuído à varíavel 'imagem' o arquivo convertido para exibição;
    No final, defini-se o atributo 'image' para o label de exibição do código.
    """
    global image
    if (not url.get().isspace()) and (url.get() != ''):
        pyqrcode.create(url.get()).png('qrcode.png', scale=3)
        image = PhotoImage(file="qrcode.png")
        qrCode['image'] = image
    else:
        errorMessage = showerror('Erro: Campo vazio',
                                 'Você precisa digitar uma URL para gerar o QR Code')


def saveimage():
    """
    -> Função que salva a imagem no desktop do usuário;
    A função não possui parâmetros, pois faz acesso da imagem gerada pela função makeqrcode();
    Ao clicar em salvar, uma messagebox abre pedindo para o usuário digitar o nome que quer
        salvar a imagem;
    A imagem é salva automaticamente no desktop do usuário.
    """
    fileName = askstring('Salvar', 'Escolha um nome para a imagem').strip()
    if (fileName != None) and (fileName != ''):
        imageSave = Image.open('qrcode.png')
        imageSave.save(path.expanduser(f'~/Desktop/{fileName}.png'), 'PNG')
        successMessage = showinfo(
            'Sucesso', 'O QR Code foi salvo com sucesso na sua área de trabalho.')
    else:
        errorMessage = showerror(
            'Erro: Arquivo sem nome', 'Você precisa definir um nome para o arquivo antes de salvar.')


# definições da janela
root = Tk()

root.title('QR Code')
root.geometry('300x350+600+230')
root.resizable(0, 0)

# definições dos elementos
Label(root,
      text='Digite uma URL válida',
      font='Arial 15',
      height=2).pack()

url = Entry(root, width=30)
url.pack()

qrCode = Label(root,
               width=130,
               height=130)

btn = Button(root,
             text='GERAR QR CODE',
             font='Arial 10',
             height=2,
             command=makeqrcode)
btn.pack(pady=20)

qrCode.pack()

btnSave = Button(root,
                 text='SALVAR',
                 font='Arial 10',
                 height=2,
                 command=saveimage)
btnSave.pack(pady=10)

# loop da janela
root.mainloop()
