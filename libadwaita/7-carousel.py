import sys
import gi
gi.require_version (
  'Gtk',
  '4.0'
)
gi.require_version (
  'Adw',
  '1'
)
from gi.repository import Gtk, Adw, GLib

class MainWindow (Adw.Window):
  def __init__ (self, *args, **kwargs):
    super ().__init__ (
      *args,
      **kwargs
    )
    GLib.set_prgname (
      'Adwaita Examples by Afacanc38'
    )
    GLib.set_application_name (
      'Adwaita Carousel'
    )
    self.set_default_size (650, 500)
    self.set_size_request (400, 400)

    self.box_main = Gtk.Box (
      orientation = Gtk.Orientation.VERTICAL,
      valign = Gtk.Align.FILL,
      vexpand = True
    )
    self.set_content (
      self.box_main
    )

    self.hb = Gtk.HeaderBar ()
    self.box_main.append (
      self.hb
    )

    # Carousel
    self.carousel = Adw.Carousel (
      hexpand = True,
      vexpand = True,
      allow_scroll_wheel = True,
      allow_long_swipes = False
    )
    self.box_main.append (
      self.carousel
    )

    # Indicator
    self.stk_indicator = Gtk.Stack (
      transition_type = Gtk.StackTransitionType.CROSSFADE
    )
    self.box_main.append (
      self.stk_indicator
    )
    self.carousel_dots = Adw.CarouselIndicatorDots (
      carousel = self.carousel
    )
    self.stk_indicator.add_titled (
      self.carousel_dots,
      'page0',
      'page0'
    )
    self.carousel_lines = Adw.CarouselIndicatorLines (
      carousel = self.carousel
    )
    self.stk_indicator.add_titled (
      self.carousel_lines,
      'page1',
      'page1'
    )

    # Page 1
    self.page1 = Adw.StatusPage (
      title = 'Carousel',
      description = 'A widget for paginated scrolling.',
      icon_name = 'go-next-symbolic',
      hexpand = True,
      vexpand = True,
    )
    self.carousel.append (
      self.page1
    )
    # Page 2
    self.page2 = Gtk.Box (
      hexpand = True,
      vexpand = True,
      halign = Gtk.Align.CENTER,
      valign = Gtk.Align.CENTER
    )
    self.carousel.append (
      self.page2
    )

    self.clamp = Adw.Clamp ()
    self.page2.append (
      self.clamp
    )

    self.listbox = Gtk.ListBox (
      selection_mode = Gtk.SelectionMode.NONE
    )
    self.listbox.get_style_context ().add_class (
      'boxed-list'
    )
    self.clamp.set_child (
      self.listbox
    )

    self.setting1 = Adw.ComboRow (
      title = 'Indicator Style'
    )
    self.strlist1 = Gtk.StringList ()
    self.strlist1.append (
      'Dots'
    )
    self.strlist1.append (
      'Lines'
    )
    self.setting1.set_model (
      self.strlist1
    )
    self.setting1.connect (
      'notify::selected-item',
      self.on_setting1_set
    )
    self.listbox.append (
      self.setting1
    )

    self.setting2 = Adw.ActionRow (
      title = 'Long swipes'
    )
    self.sw_long_swipe = Gtk.Switch (
      valign = Gtk.Align.CENTER
    )
    self.sw_long_swipe.connect (
      'notify::active',
      self.on_long_swipe_set
    )
    self.setting2.add_suffix (
      self.sw_long_swipe
    )
    self.listbox.append (
      self.setting2
    )

    self.setting3 = Adw.ActionRow (
      title = 'Scroll with mouse wheel'
    )
    self.sw_scroll_wheel = Gtk.Switch (
      valign = Gtk.Align.CENTER
    )
    self.sw_scroll_wheel.set_active (True)
    self.sw_scroll_wheel.connect (
      'notify::active',
      self.on_scroll_wheel_set
    )
    self.setting3.add_suffix (
      self.sw_scroll_wheel
    )
    self.listbox.append (
      self.setting3
    )
    for x in range(4):
      self.carousel.append (
        Adw.StatusPage (
          title = f'Page {x}',
          hexpand = True,
          vexpand = True,
        )
      )

    self.page4 = Gtk.Box (
      orientation = Gtk.Orientation.VERTICAL,
      hexpand = True,
      vexpand = True,
      halign = Gtk.Align.CENTER,
      valign = Gtk.Align.CENTER
    )
    self.carousel.append (
      self.page4
    )

    self.page4_status = Adw.StatusPage (
      title = 'Page 4',
    )
    self.page4.append (
      self.page4_status
    )

    self.btn_go_first_page = Gtk.Button (
      label = 'Return to the first page'
    )
    self.btn_go_first_page.get_style_context ().add_class (
      'pill'
    )
    self.btn_go_first_page.connect (
      'clicked',
      self.go_first_page
    )
    self.btn_go_first_page.get_style_context ().add_class (
      'suggested-action'
    )
    self.page4.append (
      self.btn_go_first_page
    )


  def on_setting1_set (self, widget, event):
    if "Dots" in self.setting1.get_selected_item ().get_string ():
      self.stk_indicator.set_visible_child (self.carousel_dots)
    if "Lines" in self.setting1.get_selected_item ().get_string ():
      self.stk_indicator.set_visible_child (self.carousel_lines)

  def on_long_swipe_set (self, widget, event):
    if self.sw_long_swipe.get_active ():
      self.carousel.set_allow_long_swipes (True)
    else:
      self.carousel.set_allow_long_swipes (False)

  def on_scroll_wheel_set (self, widget, event):
    if self.sw_scroll_wheel.get_active ():
      self.carousel.set_allow_scroll_wheel (True)
    else:
      self.carousel.set_allow_scroll_wheel (False)

  def go_first_page (self, widget):
    self.carousel.scroll_to (self.page1, True)

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

app = MyApp (
  application_id = 'io.github.afacanc38.adw-viewswitcher'
)
app.run (sys.argv)