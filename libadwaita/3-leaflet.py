import sys
import gi
import os
gi.require_version (
  'Gtk', '4.0'
)
gi.require_version (
  'Adw', '1'
)
from gi.repository import Gtk, Adw, GLib, Gio, Gdk

class MainWindow (Gtk.ApplicationWindow):
  def __init__ (self, *args, **kwargs):
    super ().__init__ (
      *args,
      **kwargs
    )

    GLib.set_application_name (
      'Adwaita Leaflet'
    )
    GLib.set_prgname (
      'Adwaita Examples by Afacanc38'
    )

    self.set_default_size (300, 300)
    
    self.hb = Gtk.HeaderBar ()
    self.set_titlebar (self.hb)

    self.lf_main = Adw.Leaflet (
      halign = Gtk.Align.FILL,
      valign = Gtk.Align.FILL
    )
    self.lf_main.set_can_unfold (False)
    self.set_child (
      self.lf_main
    )

    # Home Page

    self.pg_home = Gtk.Box (
      spacing = 6,
      halign = Gtk.Align.FILL,
      valign = Gtk.Align.FILL,
      hexpand = True,
      vexpand = True,
      orientation = Gtk.Orientation.VERTICAL
    )
    self.pg_home.set_margin_top (20)
    self.pg_home.set_margin_bottom (20)
    self.pg_home.set_margin_start (20)
    self.pg_home.set_margin_end (20)
    
    self.lf_main.append (
      self.pg_home
    )

    self.btn_go_second = Gtk.Button (
      label = "Go to second page"
    )
    self.btn_go_second.connect (
      'clicked',
      self.on_btn_go_second
    )
    self.btn_go_second.get_style_context ().add_class ('pill')
    self.pg_home.append (
      self.btn_go_second
    )
    self.sw_box_set_can_unfold = Gtk.Box (
      spacing = 6,
      orientation = Gtk.Orientation.HORIZONTAL
    )
    self.pg_home.append (
      self.sw_box_set_can_unfold
    )
    self.sw_set_can_unfold = Gtk.Switch ()
    self.sw_set_can_unfold.set_active (True)
    self.sw_set_can_unfold.connect (
      'notify::active',
      self.on_set_can_unfold
    )
    self.sw_box_set_can_unfold.append (
      self.sw_set_can_unfold
    )

    self.sw_lbl_set_can_unfold = Gtk.Label (
      label = 'Can unfold'
    )
    self.sw_box_set_can_unfold.append (
      self.sw_lbl_set_can_unfold
    )

    # Second page

    self.pg_second = Gtk.Box (
      spacing = 6,
      halign = Gtk.Align.FILL,
      valign = Gtk.Align.FILL,
      hexpand = True,
      vexpand = True,
      orientation = Gtk.Orientation.VERTICAL
    )

    self.pg_second.set_margin_top (20)
    self.pg_second.set_margin_bottom (20)
    self.pg_second.set_margin_start (20)
    self.pg_second.set_margin_end (20)
    
    self.lf_main.append (
      self.pg_second
    )

    self.lbl_pg2 = Gtk.Label (
      label = 'Second Page'
    )
    self.pg_second.append (
      self.lbl_pg2
    )

    self.btn_go_home = Gtk.Button (
      label = "Retrun to home"
    )
    self.btn_go_home.get_style_context ().add_class ('pill')
    self.pg_second.append (
      self.btn_go_home
    )
    self.btn_go_home.connect (
      'clicked',
      self.on_btn_go_home
    )


  def on_set_can_unfold (self, switch, gparam):
    if self.sw_set_can_unfold.get_active() == False:
      self.lf_main.set_can_unfold (True)
    else:
      self.lf_main.set_can_unfold (False)

  def on_btn_go_second (self, widget):
    self.lf_main.set_visible_child (self.pg_second)

  def on_btn_go_home (self, widget):
    self.lf_main.set_visible_child (self.pg_home)

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
  application_id = 'io.github.afacanc38.adw-leaflet'
)
app.run (sys.argv)