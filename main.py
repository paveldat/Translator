"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░

▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

from tkinter import *
from art import tprint
from PIL import Image, ImageTk
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def interface_configure():
    class SetCombobox():
        def __init__(self):
            self.combobox = ttk.Combobox(root, values=languageV,
                                         font='Roboto 14', state='r')
            self.label = Label()
            self.frame = Frame(root, bg='Black', bd=5)
            self.text = Text(self.frame, font='Robote 20', bg='white',
                             relief=GROOVE, wrap=WORD)
            self.scrollbar = Scrollbar(self.frame)
            self.scrollbar.pack(side='right', fill='y')

        def get(self):
            return self.combobox.get()

        def set_place(self, x, y):
            self.combobox.place(x=x, y=y)
            self.combobox.set('ENGLISH')

        def set_label(self, width, x, y):
            self.label = Label(root, text='ENGLISH', font='segoe 30 bold',
                               bg='white',
                               width=width, bd=5, relief=GROOVE)
            self.label.place(x=x, y=y)

        def set_frame(self, x, y, width, heigth):
            self.frame.place(x=x, y=y, width=width, height=heigth)

        def set_text(self, x, y, width, heigth):
            self.text.place(x=x, y=y, width=width, height=heigth)

        def configure(self):
            self.scrollbar.configure(command=self.text.yview)
            self.text.configure(yscrollcommand=self.scrollbar.set)

    def set_icon():
        """
        Sets icon in UI
        """

        icon = PhotoImage(file='icon/logo.png')
        root.iconphoto(False, icon)

    def get_available_languages() -> tuple:
        """
        Returns all available to use languages
        """

        languages = LANGUAGES
        languageV = [language.capitalize() for language in languages.values()]
        return languageV

    def configure_comboboxes():
        """
        Comboboxes configure
        """

        # 1
        combobox1 = SetCombobox()
        combobox1.set_place(110, 20)
        combobox1.set_label(18, 10, 50)
        combobox1.set_text(0, 0, 430, 200)
        combobox1.set_frame(10, 118, 440, 210)
        combobox1.configure()

        # 2
        combobox2 = SetCombobox()
        combobox2.set_place(730, 20)
        combobox2.set_label(18, 620, 50)
        combobox2.set_text(0, 0, 430, 200)
        combobox2.set_frame(620, 118, 440, 210)
        combobox2.configure()

        return combobox1, combobox2

    def add_translate_button():
        translate = Button(root, text='Translate',
                           font='Robboto 15 bold italic',
                           activebackground='purple', cursor='hand2', bd=5,
                           bg='red', fg='white', command=translate_now)
        translate.place(x=480, y=250)

    def label_change():
        language1 = combobox1.get()
        language2 = combobox2.get()
        combobox1.label.configure(text=language1)
        combobox2.label.configure(text=language2)
        root.after(1000, label_change)

    def translate_now():
        text = combobox1.text.get(1.0, END)
        translator = Translator()
        translated_text = translator.translate(text, src=combobox1.get(),
                                               dest=combobox2.get())
        translated_text = translated_text.text

        combobox2.text.delete(1.0, END)
        combobox2.text.insert(END, translated_text)

    def set_assign():
        sign = Label(root, text='Made by paveldat', bg='white',
                     font='Robboto 15 bold italic')
        sign.place(x=800, y=360)

    root = Tk()
    root.title('Transaltor')
    root.geometry('1080x400')
    set_icon()
    languageV = get_available_languages()
    combobox1, combobox2 = configure_comboboxes()
    add_translate_button()
    label_change()
    set_assign()
    root.configure(bg='white')
    root.mainloop()


def main():
    tprint('Translator')
    tprint('Made by paveldat')
    interface_configure()


if __name__ == '__main__':
    main()
