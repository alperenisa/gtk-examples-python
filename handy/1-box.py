import gi, os
gi.require_version("Gtk", "3.0")
gi.require_version("Handy", "1")
from gi.repository import Gtk, Handy

Handy.init()

class MyWindow(Handy.Window):
    def __init__(self):
        super().__init__(title="Hello World")

        # WindowHandle
        self.handle = Handy.WindowHandle()
        self.add(self.handle)

        # Box
        self.box = Gtk.Box(spacing=6)
        self.handle.add(self.box)

        # Button 1
        self.button1 = Gtk.Button(label="Merhaba")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        # Button 2
        self.button2 = Gtk.Button(label="Güle güle")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        # Button 3
        self.button3 = Gtk.Button(label="Hebele")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.button3, True, True, 0)

        # Button 4
        self.button4 = Gtk.Button(label="Temizle")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.box.pack_start(self.button4, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Merhaba")
    
    def on_button2_clicked(self, widget):
        print("Güle güle")

    def on_button3_clicked(self, widget):
        print("Hübele")
    
    def on_button4_clicked(self, widget):
        os.system("clear")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
