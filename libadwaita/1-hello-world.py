import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib, Gio


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(300, 400)
        self.set_title("Merhaba dünya!")
        GLib.set_application_name("Merhaba Dünya!")
        GLib.set_prgname('Merhaba Dünya!')

        self.main_box = Gtk.Box(
            orientation = Gtk.Orientation.VERTICAL,
            spacing = 6, # Öğeler arasında boşluk
            halign = Gtk.Align.CENTER,
            valign = Gtk.Align.CENTER # Öğeleri ortaya sabitledik
        )
        self.set_child(self.main_box)

        self.lbl_hello = Gtk.Label(
            label = "Merhaba dünya"
        )
        self.main_box.append(self.lbl_hello)

        self.btn_hello = Gtk.Button(
            label = "Bana tıkla"
        )
        self.btn_hello.connect(
            "clicked",
            self.btn_hello_clicked
        )
        self.main_box.append(self.btn_hello)

        self.hb = Gtk.HeaderBar()
        self.set_titlebar(self.hb)

        self.btn_open = Gtk.Button(
            label = "Aç"
        )
        self.btn_open.set_icon_name("document-open-symbolic")
        self.hb.pack_start(self.btn_open)

        self.dyl_open = Gtk.FileChooserNative.new(
            title = "Bir dosya seçin",
            parent = self,
            action = Gtk.FileChooserAction.OPEN
        )
        self.dyl_open.connect("response", self.open_response)
        self.btn_open.connect("clicked", self.show_open_dialog)

        self.lbl_filepath = Gtk.Label()

        menuAction = Gio.SimpleAction.new("birseyler", None)
        menuAction.connect("activate", self.print_something)
        self.add_action(menuAction)

        menu = Gio.Menu.new()
        menu.append("Bir şeyler yap!", "win.birseyler")

        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)

        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")

        self.hb.pack_end(self.hamburger)

        app = self.get_application()
        sm = app.get_style_manager()
        sm.set_color_scheme(Adw.ColorScheme.PREFER_DARK)

        self.main_box.set_margin_top(10)
        self.main_box.set_margin_bottom(10)
        self.main_box.set_margin_start(10)
        self.main_box.set_margin_end(10)

    def print_something(self, action, param):
        print("Bir şeyler!")

    def open_response(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            filename = file.get_path()
            self.lbl_filepath.set_label(filename)
            self.main_box.append(self.lbl_filepath)

    def show_open_dialog(self, button):
        self.dyl_open.show()
            
    def btn_hello_clicked(self, button):
        print("Merhaba dünya!")

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="net.teteos.example")
app.run(sys.argv)