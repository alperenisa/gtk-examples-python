import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib

class MainWindow (Adw.ApplicationWindow):
  def __init__ (self, *args, **kwargs):
    super ().__init__ (
      *args,
      **kwargs
    )
    # Set application name
    GLib.set_prgname (
      'Adwaita Examples by Afacanc38'
    )
    GLib.set_application_name (
      'Adwaita Clamp'
    )

    self.box_main = Gtk.Box (
      orientation = Gtk.Orientation.VERTICAL
    )
    self.set_content (
      self.box_main
    )

    # Headerbar
    self.hb = Gtk.HeaderBar ()
    self.box_main.append (
      self.hb
    )

    # Clamp widget
    self.clamp = Adw.Clamp ()
    self.box_main.append (
      self.clamp
    )

    # Wrapper inside Adw.Clamp
    self.box_wrapper = Gtk.Box (
      spacing = 10,
      margin_start = 20,
      margin_end = 20,
      margin_top = 20,
      margin_bottom = 20,
      orientation = Gtk.Orientation.VERTICAL
    )
    self.clamp.set_child (
      self.box_wrapper
    )

    # Label
    self.lbl1 = Gtk.Label (
      label = 'This widget is inside the Clamp.',
      halign = Gtk.Align.CENTER
    )
    self.lbl1.get_style_context ().add_class (
      'title-1'
    )
    self.lbl1.set_wrap (
      True
    )
    self.box_wrapper.append (
      self.lbl1
    )

    # Sample box
    self.box_sample = Gtk.Box ()
    self.box_sample.get_style_context ().add_class (
      'card'
    )
    self.box_wrapper.append (
      self.box_sample
    )

    # Label inside sample box
    self.lbl2 = Gtk.Label (
      label = "I am a box",
      margin_start = 10,
      margin_end = 10,
      margin_top = 10,
      margin_bottom = 10,
    )
    self.box_sample.append (
      self.lbl2
    )

class MyApp (Adw.Application):
  def __init__ (self, **kwargs):
    super ().__init__ (
      **kwargs
    )

    self.connect (
      'activate',
      self.on_activate
    )

  def on_activate (self, app):
    self.win = MainWindow (
      application = app
    )
    self.win.present ()

app = MyApp (
  application_id = 'io.github.afacanc38.adw-clamp'
)
app.run (sys.argv)