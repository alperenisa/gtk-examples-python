selamun = "aleyküm"

import gi, os
gi.require_version("Gtk", "3.0")
gi.require_version("Handy", "1")
from gi.repository import Gtk, Handy, GLib

Handy.init()

class MyWindow(Handy.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        GLib.set_application_name("Hello World")
        GLib.set_prgname('Hello World')
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
        self.hb.props.title = "HeaderBar Example"
        self.winbox.pack_start(self.hb, False, True, 0)

        # Label
        self.lbl = Gtk.Label()
        self.lbl.set_text("Hebele hübele")
        self.lbl.set_justify(Gtk.Justification.CENTER)
        self.winbox.pack_start(self.lbl, True, True, 0)

        # Headerbar button 1
        self.button = Gtk.Button()
        self.button = Gtk.Button.new_from_icon_name("pan-start-symbolic", Gtk.IconSize.MENU)
        self.hb.pack_start(self.button)

        # Headerbar button 2
        self.button2 = Gtk.Button()
        self.button2 = Gtk.Button.new_from_icon_name("pan-end-symbolic", Gtk.IconSize.MENU)
        self.hb.pack_start(self.button2)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
