import sys
import tkinter as tk
import os

class Main(tk.Frame):

    def __init__(self, top, *args, **kwargs):
     
        tk.Frame.__init__(self, top, *args, **kwargs)
        self.parent = top

        top.geometry("705x405+257+97")
        top.minsize(120, 1)
        top.maxsize(3290, 1061)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Graphics = tk.Canvas(top)
        self.Graphics.place(relx=0.43, rely=0, height=400, width=400)
        self.Graphics.configure(background="#d9d9d9")
        self.Graphics.configure(borderwidth="2")
        self.Graphics.configure(highlightbackground="#d9d9d9")
        self.Graphics.configure(highlightcolor="black")
        self.Graphics.configure(insertbackground="black")
        self.Graphics.configure(relief="ridge")
        self.Graphics.configure(selectbackground="blue")
        self.Graphics.configure(selectforeground="white")
        self.Graphics.create_line(0, 200, 400, 200,width=2)
        self.Graphics.create_line(200, 0, 200, 400, width=2)
        for i in range(0,400,50):
            self.Graphics.create_line(0, i, 400, i, width=1)
            self.Graphics.create_line(i, 0, i, 400, width=1)

        xgra = ygra = 0
        textbruh = -200
        self.id = False
        for i in range(7):
            xgra += 50
            ygra += 50
            textbruh += 50
            self.Graphics.create_oval(xgra-1, 199,xgra+1,201,fill = 'purple', width = 3)

            if textbruh==0 or textbruh==400:
                self.Graphics.create_text(xgra+15, 200-10, text=str(''), fill="purple", font=("-family {Sitka Text} -size 10"))
                self.Graphics.create_text(200+15, ygra-10, text=str(''), fill="purple", font=("-family {Sitka Text} -size 10"))
            else:
                self.Graphics.create_text(xgra+15, 200-10, text=str(textbruh), fill="purple",font=("-family {Sitka Text} -size 10"))
                self.Graphics.create_text(200+15, ygra-10, text=str(-textbruh), fill="purple",font=("-family {Sitka Text} -size 10"))
            self.Graphics.create_oval(199, ygra-1,201,ygra+1,fill = 'purple',width = 3)


        self.Text = tk.Label(top)
        self.Text.place(relx=0, rely=0, height=61, width=305)
        self.Text.configure(activebackground="#f9f9f9")
        self.Text.configure(activeforeground="black")
        self.Text.configure(background="#d9d9d9")
        self.Text.configure(disabledforeground="#a3a3a3")
        self.Text.configure(font="-family {Sitka Text} -size 20")
        self.Text.configure(foreground="#000000")
        self.Text.configure(highlightbackground="#d9d9d9")
        self.Text.configure(highlightcolor="black")
        self.Text.configure(relief="groove")
        self.Text.configure(text='''Введите коеффиценты''')

        self.inputA = tk.Entry(top)
        self.inputA.place(relx=0.028, rely=0.198, height=50, relwidth=0.077)
        self.inputA.configure(background="white")
        self.inputA.configure(disabledforeground="#a3a3a3")
        self.inputA.configure(font="-family {Courier New} -size 20")
        self.inputA.configure(foreground="#000000")
        self.inputA.configure(highlightbackground="#d9d9d9")
        self.inputA.configure(highlightcolor="black")
        self.inputA.configure(insertbackground="black")
        self.inputA.configure(selectbackground="blue")
        self.inputA.configure(selectforeground="white")

        self.axText = tk.Label(top)
        self.axText.place(relx=0.113, rely=0.198, height=51, width=43)
        self.axText.configure(activebackground="#f9f9f9")
        self.axText.configure(activeforeground="black")
        self.axText.configure(background="#d9d9d9")
        self.axText.configure(disabledforeground="#a3a3a3")
        self.axText.configure(font="-family {Segoe UI} -size 20")
        self.axText.configure(foreground="#000000")
        self.axText.configure(highlightbackground="#d9d9d9")
        self.axText.configure(highlightcolor="black")
        self.axText.configure(text='''X +''')

        self.inputB = tk.Entry(top)
        self.inputB.place(relx=0.184, rely=0.198, height=50, relwidth=0.077)
        self.inputB.configure(background="white")
        self.inputB.configure(disabledforeground="#a3a3a3")
        self.inputB.configure(font="-family {Courier New} -size 20")
        self.inputB.configure(foreground="#000000")
        self.inputB.configure(highlightbackground="#d9d9d9")
        self.inputB.configure(highlightcolor="black")
        self.inputB.configure(insertbackground="black")
        self.inputB.configure(selectbackground="blue")
        self.inputB.configure(selectforeground="white")

        self.byText = tk.Label(top)
        self.byText.place(relx=0.27, rely=0.198, height=51, width=43)
        self.byText.configure(activebackground="#f9f9f9")
        self.byText.configure(activeforeground="black")
        self.byText.configure(background="#d9d9d9")
        self.byText.configure(disabledforeground="#a3a3a3")
        self.byText.configure(font="-family {Segoe UI} -size 20")
        self.byText.configure(foreground="#000000")
        self.byText.configure(highlightbackground="#d9d9d9")
        self.byText.configure(highlightcolor="black")
        self.byText.configure(text='''Y =''')

        self.inputC = tk.Entry(top)
        self.inputC.place(relx=0.34, rely=0.198, height=50, relwidth=0.077)
        self.inputC.configure(background="white")
        self.inputC.configure(disabledforeground="#a3a3a3")
        self.inputC.configure(font="-family {Courier New} -size 20")
        self.inputC.configure(foreground="#000000")
        self.inputC.configure(highlightbackground="#d9d9d9")
        self.inputC.configure(highlightcolor="black")
        self.inputC.configure(insertbackground="black")
        self.inputC.configure(selectbackground="blue")
        self.inputC.configure(selectforeground="white")

        self.MainX = tk.Label(top)
        self.MainX.place(relx=0.03, rely=0.33, height=51, width=250)
        self.MainX.configure(activebackground="#f9f9f9")
        self.MainX.configure(activeforeground="black")
        self.MainX.configure(background="#d9d9d9")
        self.MainX.configure(disabledforeground="#a3a3a3")
        self.MainX.configure(font="-family {Segoe UI} -size 18")
        self.MainX.configure(foreground="#000000")
        self.MainX.configure(highlightbackground="#d9d9d9")
        self.MainX.configure(highlightcolor="black")
        self.MainX.configure(text='''X = X0 + Bk''')

        self.MainY = tk.Label(top)
        self.MainY.place(relx=0.03, rely=0.46, height=51, width=250)
        self.MainY.configure(activebackground="#f9f9f9")
        self.MainY.configure(activeforeground="black")
        self.MainY.configure(background="#d9d9d9")
        self.MainY.configure(disabledforeground="#a3a3a3")
        self.MainY.configure(font="-family {Segoe UI} -size 18")
        self.MainY.configure(foreground="#000000")
        self.MainY.configure(highlightbackground="#d9d9d9")
        self.MainY.configure(highlightcolor="black")
        self.MainY.configure(text='''Y = Y0 + Ak''')

        self.kText = tk.Label(top)
        self.kText.place(relx=0.043, rely=0.593, height=31, width=33)
        self.kText.configure(activebackground="#f9f9f9")
        self.kText.configure(activeforeground="black")
        self.kText.configure(background="#d9d9d9")
        self.kText.configure(disabledforeground="#a3a3a3")
        self.kText.configure(font="-family {Segoe UI} -size 18")
        self.kText.configure(foreground="#000000")
        self.kText.configure(highlightbackground="#d9d9d9")
        self.kText.configure(highlightcolor="black")
        self.kText.configure(relief="groove")
        self.kText.configure(text='''K''')

        self.spinboxK = tk.Spinbox(top, from_=-100.0, to=100.0)
        self.spinboxK.place(relx=0.099, rely=0.59, relheight=0.08, relwidth=0.332)
        self.spinboxK.configure(activebackground="#f9f9f9")
        self.spinboxK.configure(background="white")
        self.spinboxK.configure(buttonbackground="#d9d9d9")
        self.spinboxK.configure(disabledforeground="#a3a3a3")
        self.spinboxK.configure(font="TkDefaultFont")
        self.spinboxK.configure(foreground="black")
        self.spinboxK.configure(highlightbackground="black")
        self.spinboxK.configure(highlightcolor="black")
        self.spinboxK.configure(insertbackground="black")
        self.spinboxK.configure(selectbackground="blue")
        self.spinboxK.configure(selectforeground="white")
        self.spinboxK.configure(value = 0)

        self.xLabel = tk.Label(top)
        self.xLabel.place(relx=0.043, rely=0.691, height=51, width=53)
        self.xLabel.configure(activebackground="#f9f9f9")
        self.xLabel.configure(activeforeground="black")
        self.xLabel.configure(background="#d9d9d9")
        self.xLabel.configure(disabledforeground="#a3a3a3")
        self.xLabel.configure(font="-family {Segoe UI} -size 20")
        self.xLabel.configure(foreground="#000000")
        self.xLabel.configure(highlightbackground="#d9d9d9")
        self.xLabel.configure(highlightcolor="black")
        self.xLabel.configure(text='''X =''')

        self.yLabel = tk.Label(top)
        self.yLabel.place(relx=0.043, rely=0.815, height=51, width=53)
        self.yLabel.configure(activebackground="#f9f9f9")
        self.yLabel.configure(activeforeground="black")
        self.yLabel.configure(background="#d9d9d9")
        self.yLabel.configure(disabledforeground="#a3a3a3")
        self.yLabel.configure(font="-family {Segoe UI} -size 20")
        self.yLabel.configure(foreground="#000000")
        self.yLabel.configure(highlightbackground="#d9d9d9")
        self.yLabel.configure(highlightcolor="black")
        self.yLabel.configure(text='''Y =''')

        self.outputX = tk.Label(top)
        self.outputX.place(relx=0.113, rely=0.691, height=51, width=222)
        self.outputX.configure(activebackground="#f9f9f9")
        self.outputX.configure(activeforeground="black")
        self.outputX.configure(background="#d9d9d9")
        self.outputX.configure(disabledforeground="#a3a3a3")
        self.outputX.configure(font="-family {Segoe UI} -size 20")
        self.outputX.configure(foreground="#000000")
        self.outputX.configure(highlightbackground="#d9d9d9")
        self.outputX.configure(highlightcolor="black")
        self.outputX.configure(justify='left')
        self.outputX.configure(text='''X0 + Bk''')

        self.outputY = tk.Label(top)
        self.outputY.place(relx=0.113, rely=0.815, height=51, width=222)
        self.outputY.configure(activebackground="#f9f9f9")
        self.outputY.configure(activeforeground="black")
        self.outputY.configure(background="#d9d9d9")
        self.outputY.configure(disabledforeground="#a3a3a3")
        self.outputY.configure(font="-family {Segoe UI} -size 20")
        self.outputY.configure(foreground="#000000")
        self.outputY.configure(highlightbackground="#d9d9d9")
        self.outputY.configure(highlightcolor="black")
        self.outputY.configure(justify='left')
        self.outputY.configure(text='''Y0 + Ak''')

        self.ConfirmB = tk.Button(top, command = self.start1)
        self.ConfirmB.place(relx=0.37, rely=0.395, height=64, width=40)
        self.ConfirmB.configure(activebackground="#ececec")
        self.ConfirmB.configure(activeforeground="#000000")
        self.ConfirmB.configure(background="#d9d9d9")
        self.ConfirmB.configure(disabledforeground="#a3a3a3")
        self.ConfirmB.configure(font="-family {Segoe UI} -size 12")
        self.ConfirmB.configure(foreground="#000000")
        self.ConfirmB.configure(highlightbackground="#d9d9d9")
        self.ConfirmB.configure(highlightcolor="black")
        self.ConfirmB.configure(pady="0")
        self.ConfirmB.configure(text='''Счёт''')

        self.id = False

    def sign(self,a):
        if a<0:
            return '-'
        else:
            return '+'

    def gcd(self,a,b): # обычный алгоритм
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        self.g = (a + b)
        pass

    def cases(self,a, b, c, k): # проверка на особые случаи
        self.check_for_zeros = False
        self.gcd(abs(a),abs(b))
        if a == b == 0:
            if c == 0: #0x + 0y = 0
                x = 'x - любое число'
                xr = 'любое число'
                y = 'y - любое число'
                yr = 'любое число'
                self.check_for_zeros = True
                print('ок...', x, y)
            else: # 0x + 0y = x; x!=0
                print('x,y - принадлежит пустое множество')
                xr = 'пустое множество'
                x = "y - пустое множество"
                yr = 'пустое множество'
                y = "y - пустое множество"
        elif a == 0: # By = C
            x = 'x - любое число'
            y = 'y = ' + str(c/b)
            xr = 0
            yr = c/b
            print('y =',y)
        elif b == 0: # Ax = C
            x = 'x = ' + str(c/a)
            y = 'y - любое число'
            xr = c/a
            yr = 0
            print('x =',x)
        elif c==0: # Ax + By = 0
            xr = 0 + b*k
            yr = 0 - a*k
            x = 'x = 0'+self.sign(b)+str(abs(b))+'*k'
            y = 'y = 0'+self.sign(-a)+str(abs(a))+'*k'
            print('x = 0',self.sign(b), abs(b),'*k\ny= 0',self.sign(-a), abs(a),'*k')
        elif c % self.g == 0: # Евклид
            self.main(a,b,c)
            x = 'x = '+str(self.x0) + self.sign(self.b) + str(abs(self.b)) + '*k;'
            y = 'y = '+str(self.y0) + self.sign(-self.a) + str(abs(self.a)) + '*k'
            xr = self.x0 + b*k
            yr = self.y0 - a*k
        else: # алгебраический метод
            print('Алгебраический метод')
            x = '1 + ' + str(b) + '*' + str(k)
            y = str(c-a) + ' + ' + str(b) + '*' + str(k)
            xr = 1+b*k
            yr = (c-a)/b-a*k
            print('x = 1',self.sign(b), abs(a) ,'*k\ny = ',(c-a),'/',b,self.sign(-a),abs(a),'*k', sep='')
        self.x, self.y, self.xr, self.yr = x, y, xr, yr
        pass

    def main(self, a,b,c): # расширенный алгоритм Евклида
        print('Расширенный алгоритм Евклида:')
        x0, xr0, y0, yr0 = 1, 0, 0, 1
        at, bt = a, b
        while bt:
            q = at//bt
            at, bt=bt, at%bt
            x0, xr0 = xr0, x0 - xr0*q
            y0, yr0 = yr0, y0 - yr0*q
        self.x0, self.y0, self.a, self.b = x0*(c/self.g), y0*(c/self.g), a/self.g, b/self.g
        print('x=', x0, self.sign(b), abs(b) ,'*k;')
        print('y=', y0, self.sign(-a), abs(a) ,'*k')
        pass

    def start1(self):
        try:
            a = int(self.inputA.get())
            b = int(self.inputB.get())
            c = int(self.inputC.get())
            k = int(self.spinboxK.get())
            self.cases(a, b, c, k)
            self.MainX.configure(text=self.x)
            self.MainY.configure(text=self.y)
            if not self.check_for_zeros:
                self.outputX.configure(text=self.xr)
                self.outputY.configure(text=self.yr)
            else:
                self.outputX.configure(text=self.xr)
                self.outputY.configure(text=self.yr)
            self.Graphics.delete(self.id)
            print(self.xr, self.yr)
            self.cases(a, b, c, 1000)
            x1, y1 = self.xr, self.yr
            self.cases(a, b, c, -1000)
            if not self.check_for_zeros:
                if x1 == self.xr and y1 == self.yr:
                    if not self.xr != 0:
                        self.id = self.Graphics.create_line(0, self.yr+200, 400, self.yr+200, width=1, fill='red')
                    else:
                        self.id = self.Graphics.create_line(self.xr+200, 0, self.xr+200, 400, width=1, fill='red')
                else:
                    self.id = self.Graphics.create_line(x1+200, y1+200, self.xr+200, self.yr+200, width=1, fill='red')
        except ValueError:
            print('ээээ. давай только цифры')


if __name__ == "__main__":
    top = tk.Tk()
    Main(top).pack()
    top.mainloop()
