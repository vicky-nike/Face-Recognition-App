import tkinter as tk
from tkinter import ttk
from tkinter import *

key = tk.Tk()

key.title('On Screen Keyboard')

key.geometry('600x200')  # Window size
#key.maxsize(width=700, height=240)
#key.minsize(width=700, height=240)

style = ttk.Style()
#style.theme_use("clam")
key.configure(background='gray27')
style.map("C.TButton", foreground=[('!active', 'white'), ('active', 'white')], background=[ ('!active','grey21'), ('active', 'black')])
#cursor = ttk.Cursor()
#cursor.config

theme = "light"

# entry box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key, state='readonly', textvariable=equation)
Dis_entry.grid(rowspan=1, columnspan=100, ipadx=600, ipady=10)

exp = " "
is_shift = False

def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)


def Backspace():
    global exp
    exp = exp[:-1]
    equation.set(exp)


def Shift():
    global is_shift
    is_shift = not is_shift
    display()


def Clear():
    global exp
    exp = " "
    equation.set(exp)


def Theme():
    global theme
    if theme == "dark":
        key.configure(bg='gray27')
        style.map("C.TButton", foreground=[('!active', 'white'), ('active', 'white')], background=[('!active','gray21'), ('active', 'black')])
        theme = "light"
    elif theme == "light":
        key.configure(bg='gray99')
        style.map("C.TButton", foreground=[('!active', 'black'), ('active', 'black')], background=[('!active','azure'), ('active', 'grey')])
        theme = "dark"

def display():
    if (is_shift):
        # Adding keys line wise
        # First Line Button
        tilda = ttk.Button(key, text='~', command=lambda: press('~'))
        tilda.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.005, rely=0.29)

        num1 = ttk.Button(key, text='!', command=lambda: press('!'))
        num1.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.07, rely=0.29)
        
        num2 = ttk.Button(key, text='@', command=lambda: press('@'))
        num2.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.135, rely=0.29)

        num3 = ttk.Button(key, text='#', command=lambda: press('#'))
        num3.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.2, rely=0.29)

        num4 = ttk.Button(key, text='$', command=lambda: press('$'))
        num4.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.265, rely=0.29)

        num5 = ttk.Button(key, text='%', command=lambda: press('%'))
        num5.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.33, rely=0.29)

        num6 = ttk.Button(key, text='^', command=lambda: press('^'))
        num6.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.395, rely=0.29)

        num7 = ttk.Button(key, text='&', command=lambda: press('&'))
        num7.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.46, rely=0.29)

        num8 = ttk.Button(key, text='*', command=lambda: press('*'))
        num8.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.525, rely=0.29)

        num9 = ttk.Button(key, text='(', command=lambda: press('('))
        num9.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.59, rely=0.29)

        num0 = ttk.Button(key, text=')', command=lambda: press(')'))
        num0.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.655, rely=0.29)

        under = ttk.Button(key, text='_', command=lambda: press('_'))
        under.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.72, rely=0.29)

        equal = ttk.Button(key, text='=', command=lambda: press('='))
        equal.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.785, rely=0.29)

        backspace = ttk.Button(key, text='Backspace', command=Backspace)
        backspace.place(anchor=tk.W, relheight=0.13, relwidth=0.141, relx=0.85, rely=0.29)

        # Second Line Buttons

        tab_button = ttk.Button(key, text='Tab', command=lambda: press('\t'))
        tab_button.place(anchor=tk.W, relheight=0.13, relwidth=0.09, relx=0.005, rely=0.45)

        Q = ttk.Button(key, text='Q', command=lambda: press('Q'))
        Q.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.1, rely=0.45)

        W = ttk.Button(key, text='W', command=lambda: press('W'))
        W.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.165, rely=0.45)

        E = ttk.Button(key, text='E', command=lambda: press('E'))
        E.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.23, rely=0.45)

        R = ttk.Button(key, text='R', command=lambda: press('R'))
        R.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.295, rely=0.45)

        T = ttk.Button(key, text='T', command=lambda: press('T'))
        T.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.36, rely=0.45)

        Y = ttk.Button(key, text='Y', command=lambda: press('Y'))
        Y.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.425, rely=0.45)

        U = ttk.Button(key, text='U', command=lambda: press('U'))
        U.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.49, rely=0.45)

        I = ttk.Button(key, text='I', command=lambda: press('I'))
        I.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.555, rely=0.45)

        O = ttk.Button(key, text='O', command=lambda: press('O'))
        O.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.62, rely=0.45)

        P = ttk.Button(key, text='P', command=lambda: press('P'))
        P.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.685, rely=0.45)

        curly_l = ttk.Button(key, text='{', command=lambda: press('{'))
        curly_l.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.75, rely=0.45)

        curly_r = ttk.Button(key, text='}', command=lambda: press('}'))
        curly_r.place(anchor=tk.W, relheight=0.13, relwidth=0.11, relx=0.88, rely=0.45)

        # Third Line Buttons

        caps = ttk.Button(key, text='Caps', command=Shift)
        caps.place(anchor=tk.W, relheight=0.13, relwidth=0.12, relx=0.005, rely=0.61)
        
        A = ttk.Button(key, text='A', command=lambda: press('A'))
        A.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.13, rely=0.61)

        S = ttk.Button(key, text='S', command=lambda: press('S'))
        S.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.195, rely=0.61)

        D = ttk.Button(key, text='D', command=lambda: press('D'))
        D.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.26, rely=0.61)

        F = ttk.Button(key, text='F', command=lambda: press('F'))
        F.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.325, rely=0.61)

        G = ttk.Button(key, text='G', command=lambda: press('G'))
        G.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.39, rely=0.61)

        H = ttk.Button(key, text='H', command=lambda: press('H'))
        H.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.455, rely=0.61)

        J = ttk.Button(key, text='J', command=lambda: press('J'))
        J.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.52, rely=0.61)

        K = ttk.Button(key, text='K', command=lambda: press('K'))
        K.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.585, rely=0.61)

        L = ttk.Button(key, text='L', command=lambda: press('L'))
        L.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.65, rely=0.61)

        colon = ttk.Button(key, text=':', command=lambda: press(':'))
        colon.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.715, rely=0.61)

        quotation = ttk.Button(key, text='"', command=lambda: press('"'))
        quotation.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.78, rely=0.61)

        enter = ttk.Button(key, text='Enter', command=lambda: press('\n'))
        enter.place(anchor=tk.W, relheight=0.429, relwidth=0.112, relx=0.88, rely=0.759)

        # Fourth line Buttons

        shift = ttk.Button(key, text='Shift', command=Shift)
        shift.place(anchor=tk.W, relheight=0.13, relwidth=0.15, relx=0.005, rely=0.758)

        Z = ttk.Button(key, text='Z', command=lambda: press('Z'))
        Z.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.16, rely=0.758)

        X = ttk.Button(key, text='X', command=lambda: press('X'))
        X.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.225, rely=0.758)

        C = ttk.Button(key, text='C', command=lambda: press('C'))
        C.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.29, rely=0.758)

        V = ttk.Button(key, text='V', command=lambda: press('V'))
        V.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.355, rely=0.758)

        B = ttk.Button(key, text='B', command=lambda: press('B'))
        B.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.42, rely=0.758)

        N = ttk.Button(key, text='N', command=lambda: press('N'))
        N.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.485, rely=0.758)

        M = ttk.Button(key, text='M', command=lambda: press('M'))
        M.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.55, rely=0.758)

        ang_l = ttk.Button(key, text='<', command=lambda: press('<'))
        ang_l.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.615, rely=0.758)

        ang_r = ttk.Button(key, text='>', command=lambda: press('>'))
        ang_r.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.68, rely=0.758)

        question = ttk.Button(key, text='?', command=lambda: press('?'))
        question.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.745, rely=0.758)

        plus = ttk.Button(key, text='+', command=lambda: press('+'))
        plus.place(anchor=tk.W, relheight=0.13, relwidth=0.065, relx=0.81, rely=0.758)

        # Fifth Line Buttons

        close = ttk.Button(key, text='Close', command=key.destroy)
        close.place(anchor=tk.W, relheight=0.13, relwidth=0.09, relx=0.005, rely=0.91)
        
        theme = ttk.Button(key, text='Theme', command=Theme)
        theme.place(anchor=tk.W, relheight=0.13, relwidth=0.1, relx=0.1, rely=0.91)
        
        space = ttk.Button(key, text='Space', command=lambda: press(' '))
        space.place(anchor=tk.W, relheight=0.13, relwidth=0.515, relx=0.205, rely=0.91)

        clear = ttk.Button(key, text='Clear', command=Clear)
        clear.place(anchor=tk.W, relheight=0.13, relwidth=0.15, relx=0.725, rely=0.91)

        
        key.mainloop()
        
    else:
        # Adding keys line wise
        # First Line Button
        tick = ttk.Button(key, text='`', command=lambda: press('`'))
        tick.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.005, rely=0.29)

        num1 = ttk.Button(key, text='1', command=lambda: press('1'))
        num1.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.07, rely=0.29)

        num2 = ttk.Button(key, text='2', command=lambda: press('2'))
        num2.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.135, rely=0.29)

        num3 = ttk.Button(key, text='3', command=lambda: press('3'))
        num3.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.2, rely=0.29)
        
        num4 = ttk.Button(key, text='4', command=lambda: press('4'))
        num4.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.265, rely=0.29)

        num5 = ttk.Button(key, text='5', command=lambda: press('5'))
        num5.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.33, rely=0.29)

        num6 = ttk.Button(key, text='6', command=lambda: press('6'))
        num6.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.395, rely=0.29)

        num7 = ttk.Button(key, text='7', command=lambda: press('7'))
        num7.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.46, rely=0.29)

        num8 = ttk.Button(key, text='8', command=lambda: press('8'))
        num8.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.525, rely=0.29)

        num9 = ttk.Button(key, text='9', command=lambda: press('9'))
        num9.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.59, rely=0.29)

        num0 = ttk.Button(key, text='0', command=lambda: press('0'))
        num0.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.655, rely=0.29)
        
        minus = ttk.Button(key, text='-', command=lambda: press('-'))
        minus.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.72, rely=0.29)

        equal = ttk.Button(key, text='=', command=lambda: press('='))
        equal.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.785, rely=0.29)

        backspace = ttk.Button(key, text='Backspace', command=Backspace)
        backspace.place(anchor=tk.W, relheight=0.13, relwidth=0.141, relx=0.85, rely=0.29)
        
        # Second Line Buttons ###########################################################

        tab_button = ttk.Button(key, text='Tab', command=lambda: press('\t'))
        tab_button.place(anchor=tk.W, relheight=0.13, relwidth=0.09, relx=0.005, rely=0.45)

        Q = ttk.Button(key, text='q', command=lambda: press('q'))
        Q.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.1, rely=0.45)
        
        W = ttk.Button(key, text='w', command=lambda: press('w'))
        W.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.165, rely=0.45)

        E = ttk.Button(key, text='e', command=lambda: press('e'))
        E.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.23, rely=0.45)

        R = ttk.Button(key, text='r', command=lambda: press('r'))
        R.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.295, rely=0.45)

        T = ttk.Button(key, text='t', command=lambda: press('t'))
        T.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.36, rely=0.45)

        Y = ttk.Button(key, text='y', command=lambda: press('y'))
        Y.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.425, rely=0.45)

        U = ttk.Button(key, text='u', command=lambda: press('u'))
        U.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.49, rely=0.45)

        I = ttk.Button(key, text='i', command=lambda: press('i'))
        I.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.555, rely=0.45)

        O = ttk.Button(key, text='o', command=lambda: press('o'))
        O.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.62, rely=0.45)

        P = ttk.Button(key, text='p', command=lambda: press('p'))
        P.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.685, rely=0.45)
        
        sq_l = ttk.Button(key, text='[', command=lambda: press('['))
        sq_l.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.75, rely=0.45)

        sq_r = ttk.Button(key, text=']', command=lambda: press(']'))
        sq_r.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.815, rely=0.45)

        back_slash = ttk.Button(key, text='\\', command=lambda: press('\\'))
        back_slash.place(anchor=tk.W, relheight=0.13, relwidth=0.11, relx=0.88, rely=0.45)
        
        # Third Line Buttons ###########################################################
        
        caps = ttk.Button(key, text='Caps', command=Shift)
        caps.place(anchor=tk.W, relheight=0.13, relwidth=0.12, relx=0.005, rely=0.61)
        
        A = ttk.Button(key, text='a', command=lambda: press('a'))
        A.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.13, rely=0.61)
        
        S = ttk.Button(key, text='s', command=lambda: press('s'))
        S.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.195, rely=0.61)

        D = ttk.Button(key, text='d', command=lambda: press('d'))
        D.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.26, rely=0.61)

        F = ttk.Button(key, text='f', command=lambda: press('f'))
        F.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.325, rely=0.61)

        G = ttk.Button(key, text='g', command=lambda: press('g'))
        G.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.39, rely=0.61)

        H = ttk.Button(key, text='h', command=lambda: press('h'))
        H.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.455, rely=0.61)

        J = ttk.Button(key, text='j', command=lambda: press('j'))
        J.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.52, rely=0.61)

        K = ttk.Button(key, text='k', command=lambda: press('k'))
        K.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.585, rely=0.61)

        L = ttk.Button(key, text='l', command=lambda: press('l'))
        L.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.65, rely=0.61)
        
        semi_co = ttk.Button(key, text=';', command=lambda: press(';'))
        semi_co.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.715, rely=0.61)

        quotation = ttk.Button(key, text="'", command=lambda: press('"'))
        quotation.place(anchor=tk.W, relheight=0.13, relwidth=0.095, relx=0.78, rely=0.61)

        enter = ttk.Button(key, text='Enter', command=lambda: press('\n'))
        enter.place(anchor=tk.W, relheight=0.429, relwidth=0.112, relx=0.88, rely=0.759)
        
        # Fourth line Buttons ######################################################

        shift = ttk.Button(key, text='Shift', width=6, command=Shift)
        shift.place(anchor=tk.W, relheight=0.13, relwidth=0.15, relx=0.005, rely=0.758)
        
        Z = ttk.Button(key, text='z', command=lambda: press('z'))
        Z.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.16, rely=0.758)
        
        X = ttk.Button(key, text='x', command=lambda: press('x'))
        X.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.225, rely=0.758)

        C = ttk.Button(key, text='c', command=lambda: press('c'))
        C.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.29, rely=0.758)

        V = ttk.Button(key, text='v', command=lambda: press('v'))
        V.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.355, rely=0.758)

        B = ttk.Button(key, text='b', command=lambda: press('b'))
        B.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.42, rely=0.758)

        N = ttk.Button(key, text='n', command=lambda: press('n'))
        N.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.485, rely=0.758)

        M = ttk.Button(key, text='m', command=lambda: press('m'))
        M.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.55, rely=0.758)

        comma = ttk.Button(key, text=',', command=lambda: press(','))
        comma.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.615, rely=0.758)

        dot = ttk.Button(key, text='.', command=lambda: press('.'))
        dot.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.68, rely=0.758)

        slash = ttk.Button(key, text='/', command=lambda: press('/'))
        slash.place(anchor=tk.W, relheight=0.13, relwidth=0.06, relx=0.745, rely=0.758)

        plus = ttk.Button(key, text='+', command=lambda: press('+'))
        plus.place(anchor=tk.W, relheight=0.13, relwidth=0.065, relx=0.81, rely=0.758)


        # Fifth Line Buttons

        close = ttk.Button(key, text='Close', command=key.destroy)
        close.place(anchor=tk.W, relheight=0.13, relwidth=0.09, relx=0.005, rely=0.91)
        
        theme = ttk.Button(key, text='Theme', command=Theme)
        theme.place(anchor=tk.W, relheight=0.13, relwidth=0.1, relx=0.1, rely=0.91)
        
        space = ttk.Button(key, text='Space', command=lambda: press(' '))
        space.place(anchor=tk.W, relheight=0.13, relwidth=0.515, relx=0.205, rely=0.91)

        clear = ttk.Button(key, text='Clear', command=Clear)
        clear.place(anchor=tk.W, relheight=0.13, relwidth=0.15, relx=0.725, rely=0.91)

        key.mainloop()

display()