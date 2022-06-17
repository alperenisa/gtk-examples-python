import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Handy", "1")
from gi.repository import Gtk, Handy

Handy.init()

class MyWindow(Handy.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self.set_default_size(900, 300)
        self.handle = Handy.WindowHandle()
        self.add(self.handle)

        # Window box
        self.winbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.handle.add(self.winbox)
        ## Headerbar
        self.hb = Handy.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.props.title = "Style Classes Example"
        self.winbox.pack_start(self.hb, False, True, 0)

        # MainBox
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, halign=Gtk.Align.CENTER, valign=Gtk.Align.CENTER)
        self.winbox.pack_start(self.mainbox, True, True, 0)
        ## Button box
        self.btn_box = Gtk.ButtonBox(halign=Gtk.Align.CENTER, valign=Gtk.Align.CENTER, spacing=6)
        self.mainbox.pack_start(self.btn_box, True, True, 0)
        ### Normal button
        self.btn = Gtk.Button(label="Normal")
        self.btn_box.pack_start(self.btn, False, False, 0)
        ### Suggested button
        self.btn_suggested = Gtk.Button(label="Suggested")
        self.btn_suggested.get_style_context().add_class("suggested-action")
        self.btn_box.pack_start(self.btn_suggested, False, False, 0)
        ### Destructive button
        self.btn_destructive = Gtk.Button(label="Destructive")
        self.btn_destructive.get_style_context().add_class("destructive-action")
        self.btn_box.pack_start(self.btn_destructive, False, False, 0)

        ## Flat button box
        self.btn_box2 = Gtk.ButtonBox(halign=Gtk.Align.CENTER, valign=Gtk.Align.CENTER, spacing=6)
        self.mainbox.pack_start(self.btn_box2, True, True, 0)
        ### Normal button
        self.btn_flat = Gtk.Button(label="Flat")
        self.btn_flat.get_style_context().add_class("flat")
        self.btn_box.pack_start(self.btn_flat, False, False, 0)
        ### Suggested button
        self.btn_suggested_flat = Gtk.Button(label="Suggested Flat")
        self.btn_suggested_flat.get_style_context().add_class("suggested-action")
        self.btn_suggested_flat.get_style_context().add_class("flat")
        self.btn_box.pack_start(self.btn_suggested_flat, False, False, 0)
        ### Destructive button
        self.btn_destructive_flat = Gtk.Button(label="Destructive Flat")
        self.btn_destructive_flat.get_style_context().add_class("destructive-action")
        self.btn_destructive_flat.get_style_context().add_class("flat")
        self.btn_box.pack_start(self.btn_destructive_flat, False, False, 0)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
