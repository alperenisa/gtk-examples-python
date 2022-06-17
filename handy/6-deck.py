import gi
gi.require_version ('Gtk', '3.0')
gi.require_version ('Handy', '1')
from gi.repository import Gtk, Handy

Handy.init ()

class MyWindow (Handy.Window):
    def __init__ (self):
        super() .__init__(
            title = 'Hello World'
        )
        self.set_default_size (900, 300)

        # WindowHandle
        self.hdl = Handy.WindowHandle ()
        self.add (self.hdl)

        # Deck
        self.deck = Handy.Deck ()
        self.deck.set_can_swipe_back (True)
        self.hdl.add (self.deck)

        # Main Page
        self.mainpage = Gtk.Box(
            spacing = 6,
            orientation = Gtk.Orientation.VERTICAL
        )
        
        self.hb = Handy.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.props.title = "Handy Deck Example"
        self.mainpage.pack_start(
            self.hb,
            False,
            True,
            0
        )
        self.deck.add (self.mainpage)

        # Page 1
        self.page1 = Gtk.Box(
            spacing = 6,
            orientation = Gtk.Orientation.VERTICAL,
            halign = Gtk.Align.CENTER,
            valign = Gtk.Align.CENTER
        )
        self.lbl_page1 = Gtk.Label (
            label = 'Page 1',
        )
        self.btn_prev1 = Gtk.Button (
            label = 'Previous',
            halign = Gtk.Align.CENTER,
            valign = Gtk.Align.CENTER
        )
        self.btn_prev1.connect(
            'clicked', self.on_prev_clicked
        )
        self.page1.pack_start(
            self.lbl_page1,
            True,
            True,
            0
        )
        self.page1.pack_start(
            self.btn_prev1,
            True,
            True,
            0
        )
        
        self.deck.add (self.page1)

        # Page 2
        self.page2 = Gtk.Box(
            spacing = 6,
            orientation = Gtk.Orientation.VERTICAL,
            halign = Gtk.Align.CENTER,
            valign = Gtk.Align.CENTER
        )
        self.lbl_page2 = Gtk.Label (
            label = 'Page 2'
        )
        self.btn_prev2 = Gtk.Button (
            label = 'Previous',
            halign = Gtk.Align.CENTER,
            valign = Gtk.Align.CENTER
        )
        self.btn_prev2.connect(
            'clicked', self.on_prev_clicked
        )
        self.page2.pack_start(
            self.lbl_page2,
            True,
            True,
            0
        )
        self.page2.pack_start(
            self.btn_prev2,
            True,
            True,
            0
        )

        self.deck.add (self.page2)

        # Page 3
        self.page3 = Gtk.Box(
            spacing = 6,
            orientation = Gtk.Orientation.VERTICAL,
            halign = Gtk.Align.CENTER,
            valign = Gtk.Align.CENTER
        )
        self.btn_prev3 = Gtk.Button (
            label = 'Previous',
            halign = Gtk.Align.CENTER,
            valign = Gtk.Align.CENTER
        )
        self.btn_prev3.connect(
            'clicked', self.on_prev_clicked
        )
        self.lbl_page3 = Gtk.Label (
            label = 'Page 3'
        )
        self.page3.pack_start(
            self.lbl_page3,
            True,
            True,
            0
        )
        self.page3.pack_start(
            self.btn_prev3,
            True,
            True,
            0
        )

        self.deck.add (self.page3)

        # Main page
        self.btn_box = Gtk.ButtonBox (
            spacing = 6,
            halign = Gtk.Align.CENTER,
            valign = Gtk.Align.CENTER
        )

        self.btn_page1 = Gtk.Button (
            label = 'Page 1',
        )
        self.btn_box.add (self.btn_page1)
        self.btn_page1.connect(
            'clicked',
            self.on_btn_page1_clicked
        )

        self.btn_page2 = Gtk.Button (
            label = 'Page 2',
        )
        self.btn_page2.connect(
            'clicked', self.on_btn_page2_clicked
        )

        self.btn_box.add (self.btn_page2)

        self.btn_page3 = Gtk.Button (
            label = 'Page 3'
        )

        self.btn_page3.connect(
            'clicked',
            self.on_btn_page3_clicked
        )

        self.btn_box.add (self.btn_page3)
        self.mainpage.pack_start(
            self.btn_box,
            True,
            True,
            0
        )

    def on_btn_page1_clicked (self, widget):
        self.deck.set_visible_child (self.page1)
    def on_btn_page2_clicked (self, widget):
        self.deck.set_visible_child (self.page2)
    def on_btn_page3_clicked (self, widget):
        self.deck.set_visible_child (self.page3)
    def on_prev_clicked (self, widget):
        self.deck.set_visible_child (self.mainpage)

win = MyWindow ()
win.connect ('destroy', Gtk.main_quit)
win.show_all ()
Gtk.main ()
