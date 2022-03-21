import tkinter as tk
from tkinter import ttk
root = tk.Tk()

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        
    def init_main(self):
        toolbar = tk.Frame(bg = 'white', bd = 2)
        toolbar.pack(side = tk.TOP, fill = tk.X)
        self.add_img = tk.PhotoImage(file = 'add.gif')
        btn_open_dialog = tk.Button(
                                    toolbar, 
                                    text = 'Добавить новую птицу', 
                                    command = self.open_dialog,
                                    bg = 'black', bd = 0,
                                    compound = tk.TOP, image = self.add_img)
        btn_open_dialog.pack(side = tk.LEFT)
        self.tree = ttk.Treeview(self, columns = ('ID', 'Пол', 'Порода'), 
                                 height = 15, show = 'headings')
        self.tree.column('ID', width = 30, anchor = tk.CENTER)        
        self.tree.column('Пол', width = 30, anchor = tk.CENTER)
        self.tree.column('Порода', width = 30, anchor = tk.CENTER)
        
        self.tree.heading('ID', text = 'ID')
        self.tree.heading('Пол', text = 'Пол')
        self.tree.heading('Порода', text = 'Порода')
        self.tree.pack()
        
    def open_dialog(self):
        Child()
        
class Child1(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child1()

    def init_child1(self):
        self.title('Новая птица')
        self.geometry('400x220+400+300')
        self.resizable(False, False)
        
        label_ID = ttk.Label(self, text = 'ID')
        label_ID.place(x = 200, y = 40 )
        
        label_s = ttk.Label(self, text = 'Пол')
        label_s.place(x = 200, y = 60 )
        
        label_k = ttk.Label(self, text = 'Порода')
        label_k.place(x = 200, y = 90 )
        
        self.entry_ID = ttk.Entry(self)
        self.entry_ID.place(x = 200, y = 50)
        
        self.combox_s = ttk.Combobox(self, values = [u'Самка', u'Самец'])
        self.combox_s.current(0)
        self.combox_s.place(x = 200, y = 70)
        
        self.combox_k = ttk.Combobox(self, values = [u'сизый', 
                                                     u'бельгийский почтовый', 
                                                     u'английский карьер'])
        self.combox_k.current(0)
        self.combox_k.place(x = 200, y = 100)
        
        btn_pass = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        btn_pass.place(x = 200, y = 150)
        
        btn_ok = ttk.Button(self, text = 'Добавить')
        btn_ok.place(x = 250, y = 150)
        btn_ok.bind('<Button-1>')
        
        self.grab_set()
        self.focus_set()

        
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Прилетная доска")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()        