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
    super ().__init__ (*args, **kwargs)
    GLib.set_application_name ('Adwaita Buttons')
    GLib.set_prgname ('Adwaita Examples by Afacanc38')

    self.set_default_size (500, 600)

    css_provider = Gtk.CssProvider()
    css_provider.load_from_file(Gio.File.new_for_path(f'{os.path.dirname(os.path.realpath(__file__))}/resources/2-buttons.css'))
    Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    self.hb = Gtk.HeaderBar ()
    self.set_titlebar (self.hb)

    self.scroll = Gtk.ScrolledWindow ()
    self.scroll.set_policy (Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
    self.set_child (self.scroll)

    self.main_box = Gtk.Box (
      spacing = 10,
      orientation = Gtk.Orientation.VERTICAL
    )
    self.main_box.set_margin_top (20)
    self.main_box.set_margin_bottom (20)
    self.main_box.set_margin_start (20)
    self.main_box.set_margin_end (20)
    self.scroll.set_child(self.main_box)

    self.box_normal_buttons_group = Gtk.Box (
      spacing = 6,
      orientation = Gtk.Orientation.VERTICAL,
      halign = Gtk.Align.START,
      valign = Gtk.Align.CENTER
    )
    self.main_box.append (self.box_normal_buttons_group)

    self.lbl_normal_buttons_title = Gtk.Label (
      label = 'Normal Buttons',
      halign = Gtk.Align.START
    )
    self.lbl_normal_buttons_title.get_style_context().add_class ('title-1')
    self.box_normal_buttons_group.append (self.lbl_normal_buttons_title)

    self.box_normal_buttons = Gtk.Box (
      spacing = 6
    )
    self.box_normal_buttons_group.append (self.box_normal_buttons)

    self.normal_button_regular = Gtk.Button (
      label = 'Regular'
    )
    self.box_normal_buttons.append (self.normal_button_regular)

    self.normal_button_flat = Gtk.Button (
      label = 'Flat'
    )
    self.normal_button_flat.get_style_context().add_class ('flat')
    self.box_normal_buttons.append (self.normal_button_flat)

    self.normal_button_suggested = Gtk.Button (
      label = 'Suggested'
    )
    self.normal_button_suggested.get_style_context ().add_class ('suggested-action')
    self.box_normal_buttons.append (self.normal_button_suggested)
    
    self.normal_button_destructive = Gtk.Button (
      label = 'Destructive'
    )
    self.normal_button_destructive.get_style_context ().add_class ('destructive-action')
    self.box_normal_buttons.append (self.normal_button_destructive)

    self.box_custom_buttons = Gtk.Box (
      spacing = 6
    )
    self.box_normal_buttons_group.append (self.box_custom_buttons)

    self.custom_button_green = Gtk.Button (
      label = 'Custom'
    )
    self.custom_button_green.get_style_context ().add_class ('green')
    self.box_custom_buttons.append (self.custom_button_green)

    self.custom_button_purple = Gtk.Button (
      label = 'Custom'
    )
    self.custom_button_purple.get_style_context ().add_class ('purple')
    self.box_custom_buttons.append (self.custom_button_purple)

    self.custom_button_yellow = Gtk.Button (
      label = 'Custom'
    )
    self.custom_button_yellow.get_style_context ().add_class ('yellow')
    self.box_custom_buttons.append (self.custom_button_yellow)

    self.custom_button_orange = Gtk.Button (
      label = 'Custom'
    )
    self.custom_button_orange.get_style_context ().add_class ('orange')
    self.box_custom_buttons.append (self.custom_button_orange)

    self.box_other_buttons_group = Gtk.Box (
      spacing = 6,
      orientation = Gtk.Orientation.VERTICAL,
      halign = Gtk.Align.START,
      valign = Gtk.Align.CENTER
    )
    self.main_box.append (self.box_other_buttons_group)

    self.lbl_ohter_buttons_title = Gtk.Label (
      label = 'Other Buttons',
      halign = Gtk.Align.START
    )
    self.lbl_ohter_buttons_title.get_style_context ().add_class ('title-1')
    self.box_other_buttons_group.append (self.lbl_ohter_buttons_title)
    
    self.box_other_buttons = Gtk.Box (
      spacing = 6
    )
    self.box_other_buttons_group.append (self.box_other_buttons)

    self.circular_button_1 = Gtk.Button.new_from_icon_name ('go-home-symbolic')
    self.circular_button_1.get_style_context().add_class ('circular')
    self.box_other_buttons.append (self.circular_button_1)

    self.circular_button_2 = Gtk.Button.new_from_icon_name ('document-save-symbolic')
    self.circular_button_2.get_style_context().add_class ('circular')
    self.box_other_buttons.append (self.circular_button_2)

    self.circular_button_3 = Gtk.Button.new_from_icon_name ('document-properties-symbolic')
    self.circular_button_3.get_style_context().add_class ('circular')
    self.box_other_buttons.append (self.circular_button_3)

    self.box_other_buttons_2 = Gtk.Box (
      spacing = 6
    )
    self.box_other_buttons_group.append (self.box_other_buttons_2)

    self.pill_button = Gtk.Button (
      label = 'Pill Button'
    )
    self.pill_button.get_style_context ().add_class ('pill')
    self.box_other_buttons_2.append (self.pill_button)
class MyApp (Adw.Application):
  def __init__ (self, **kwargs):
    super ().__init__ (**kwargs)
    self.connect (
      'activate',
      self.on_activate
    )

  def on_activate (self, app):
    self.win = MainWindow (
      application = app
    )
    self.win.present ()

app = MyApp(
  application_id = 'io.github.afacanc38.adw-buttons'
)
app.run(sys.argv)