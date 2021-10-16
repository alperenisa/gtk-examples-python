selamun = "aleyküm"

import gi, os
gi.require_version("Gtk", "3.0")
gi.require_version("Handy", "1")
from gi.repository import Gtk, Handy

Handy.init()

class MyWindow(Handy.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self.set_default_size(500, 300)

        # WindowHandle
        self.handle = Handy.WindowHandle()
        self.add(self.handle)

        # Box
        self.winbox = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        self.handle.add(self.winbox)

        # Headerbar
        self.hb = Handy.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.props.title = "Stack Example"
        self.winbox.pack_start(self.hb, False, True, 0)

        # Stack
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.winbox.pack_start(self.stack, True, True, 0)

        # Labels
        self.label = Gtk.Label(label="Page 1")
        self.stack.add_titled(self.label, "page0", "Label")

        self.label = Gtk.Label(label="Page 2")
        self.stack.add_titled(self.label, "page1", "Label")

        self.label = Gtk.Label(label="Page 3")
        self.stack.add_titled(self.label, "page2", "Label")
        
        self.label = Gtk.Label(label="Page 4")
        self.stack.add_titled(self.label, "page3", "Label")

        self.label = Gtk.Label(label="Page 5")
        self.stack.add_titled(self.label, "page4", "Label")

        # Headerbar button 1
        self.button = Gtk.Button()
        self.button = Gtk.Button.new_from_icon_name("pan-start-symbolic", Gtk.IconSize.MENU)
        self.hb.pack_start(self.button)
        self.button.connect('clicked', self.on_button1_clicked)

        # Headerbar button 2
        self.button2 = Gtk.Button()
        self.button2 = Gtk.Button.new_from_icon_name("pan-end-symbolic", Gtk.IconSize.MENU)
        self.hb.pack_start(self.button2)
        self.button2.connect("clicked", self.on_button2_clicked)

    def on_button1_clicked(self, widget):
        pages = self.stack.get_children()
        cur_page = self.stack.get_visible_child()
        i = pages.index(cur_page)
        if i == 0: return
        self.stack.set_visible_child(pages[i-1])

    def on_button2_clicked(self, widget):
        pages = self.stack.get_children()
        cur_page = self.stack.get_visible_child()
        i = pages.index(cur_page)
        if i == len(pages) - 1: return
        self.stack.set_visible_child(pages[i+1])

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()