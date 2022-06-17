import sys
import gi
gi.require_version (
  "Gtk",
  "4.0"
)
gi.require_version(
  "Adw",
  "1"
)
from gi.repository import Gtk, Adw, GLib

class MainWindow (Adw.ApplicationWindow):
  def __init__ (self, *args, **kwargs):
    super ().__init__ (
      *args,
      **kwargs
    )
    GLib.set_prgname (
      'Adwaita Examples by Afacanc38'
    )
    GLib.set_application_name (
      'Adwaita ViewSwitcher'
    )

    self.set_name (
      'ViewSwitcherDemo'
    )
    self.set_default_size (600, 300)

    self.box_main = Gtk.Box (
      orientation = Gtk.Orientation.VERTICAL,
      halign = Gtk.Align.FILL,
      valign = Gtk.Align.FILL,
      hexpand = True,
      vexpand = True
    )
    self.set_content (
      self.box_main
    )

    self.hb = Adw.HeaderBar ()
    self.box_main.append (self.hb)

    self.stack = Adw.ViewStack ()
    self.box_main.append (
      self.stack
    )

    # Squieezer
    self.sq_viewswitcher = Adw.Squeezer ()
    self.sq_viewswitcher.set_switch_threshold_policy (
      Adw.FoldThresholdPolicy.NATURAL
    )
    self.sq_viewswitcher.set_transition_type (
      Adw.SqueezerTransitionType.CROSSFADE
    )
    self.sq_viewswitcher.set_xalign (1)
    self.sq_viewswitcher.set_homogeneous (True)
    self.hb.set_title_widget (
      self.sq_viewswitcher
    )

    # ViewSwitcher (wide)
    self.viewswitcher_wide = Adw.ViewSwitcher ()
    self.viewswitcher_wide.set_policy(
      Adw.ViewSwitcherPolicy.WIDE
    )
    self.viewswitcher_wide.set_stack (
      self.stack
    )
    self.sq_viewswitcher.add (
      self.viewswitcher_wide
    )

    # ViewSwitcher (narrow)
    self.viewswitcher_narrow = Adw.ViewSwitcher ()
    self.viewswitcher_narrow.set_policy(
      Adw.ViewSwitcherPolicy.NARROW
    )
    self.viewswitcher_narrow.set_stack (
      self.stack
    )
    self.sq_viewswitcher.add (
      self.viewswitcher_narrow
    )

    # ViewSwitcherBar (bottom viewswitcher)
    self.viewswitcherbar = Adw.ViewSwitcherBar (
      vexpand = True,
      valign = Gtk.Align.END
    )
    self.viewswitcherbar.set_stack (
      self.stack
    )
    self.viewswitcherbar.set_reveal (False)
    self.box_main.append (
      self.viewswitcherbar
    )

    # Window Title
    self.wintitle = Adw.WindowTitle (
      title = 'Adwaita ViewSwitcher'
    )
    self.sq_viewswitcher.add (self.wintitle)
    
    # Connect signals
    self.sq_viewswitcher.connect (
      'notify::visible-child',
      self.on_sq_get_visible_child
    )

    # Page 1 
    self.page1 = Adw.StatusPage (
      title = 'Apps',
      icon_name = 'view-grid-symbolic',
      valign = Gtk.Align.CENTER,
      vexpand = True
    )
    self.stack.add_titled (
      self.page1,
      'page0',
      'Apps'
    )
    self.stack.get_page (self.page1).set_icon_name (
      'view-grid-symbolic'
    )

    # Page 2
    self.page2 = Adw.StatusPage (
      title = 'Installed',
      icon_name = 'system-software-install-symbolic',
      valign = Gtk.Align.CENTER,
      vexpand = True
    )
    self.stack.add_titled (
      self.page2,
      'page1',
      'Installed'
    )
    self.stack.get_page (self.page2).set_icon_name (
      'system-software-install-symbolic'
    )

    # Page 3
    self.page3 = Adw.StatusPage (
      title = 'Updates',
      icon_name = 'view-refresh-symbolic',
      valign = Gtk.Align.CENTER,
      vexpand = True
    )
    self.stack.add_titled (
      self.page3,
      'page2',
      'Updates'
    )
    self.stack.get_page (self.page3).set_icon_name (
      'view-refresh-symbolic'
    )

  def on_sq_get_visible_child (self, widget, event):
    if self.sq_viewswitcher.get_visible_child() == self.wintitle:
      self.viewswitcherbar.set_reveal (True)
    else:
      self.viewswitcherbar.set_reveal (False)

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