from tkinter import *
from tkinter import ttk

RELEASE_VERSION = '1.0'

class myApp():
    def __init__(self):
        self.root = Tk()
        self.root.title( "PySample " + RELEASE_VERSION )
        self.root.option_add( '*tearOff', False) # Don't allow tear-off menus
        self.root.bind('<KeyPress>', self.keypressCallback )
        style = ttk.Style()
        allThemes = style.theme_names()
        print( 'Themes: ' + ','.join(allThemes) )   #  vista, clam, winnative, alt, default, classic, xpnative
        currentTheme = style.theme_use()
        print( 'Current Theme: ' + currentTheme )
        style.theme_use('vista')
        style.configure( 'TButton', foreground = 'blue' )

    def constructMenu(self):
        self.menubar = Menu(self.root)
        self.root.config( menu = self.menubar)
        self.m_file = Menu(self.menubar)
        self.menubar.add_cascade(menu= self.m_file , label = 'File')
        self.m_file.add_command( label='Exit', command = lambda: exit() )
        self.m_file.entryconfig('Exit', accelerator = 'Ctrl + Z')

    def constructWindows(self):
        self.constructMenu()
        self.button1 = ttk.Button(self.root, text ='Click Me', command = lambda: self.buttonCallback('ClickMe'))
        self.button1.pack()

    def run(self):
        self.root.mainloop()

    def buttonCallback(self, name):
        print("you pressed the button " + name)

    def keypressCallback(self, event):
        print('you pressed a key')
        print( 'type:{}'.format(event.type))
        print( 'widget:{}'.format(event.widget))
        print( 'char: {}'.format(event.char))
        print( 'keysym: {}'.format(event.keysym))
        print( 'keycode: {}'.format(event.keycode))

def main():
    """

    :rtype: object
    """
    app = myApp()
    app.constructWindows()
    app.run()

if __name__ == "__main__":
    main()
