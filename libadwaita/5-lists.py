import sys
import gi
import os
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib, Gio, Gdk

class MainWindow (Gtk.Window):
  def __init__ (self, *args, **kwargs):
    super ().__init__ (*args, **kwargs)

    GLib.set_prgname (
      'Adwaita Examples by Afacanc38'
    )
    GLib.set_application_name (
      'Adwaita ListBox'
    )

    self.set_default_size (650, 500)
    self.set_size_request (400, 400)

    self.scroll = Gtk.ScrolledWindow ()
    self.scroll.set_policy (Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
    self.set_child (self.scroll)

    self.box_main = Gtk.Box (
      orientation = Gtk.Orientation.VERTICAL
    )
    self.scroll.set_child (
      self.box_main
    )

    # HeaderBar
    self.hb = Gtk.HeaderBar ()
    self.set_titlebar (
      self.hb
    )

    # Clamp
    self.clamp = Adw.Clamp ()
    self.box_main.append (
      self.clamp
    )

    # Wrapper
    self.box_wrapper = Gtk.Box (
      orientation = Gtk.Orientation.VERTICAL,
      margin_top = 20,
      margin_bottom = 20,
      margin_start = 20,
      margin_end = 20
    )
    self.clamp.set_child (
      self.box_wrapper
    )

    # Header
    self.box_header = Gtk.Box (
      orientation = Gtk.Orientation.VERTICAL,
      margin_bottom = 10
    )
    self.box_wrapper.append (
      self.box_header
    )

    # Title
    self.lbl_title = Gtk.Label (
      label = "Lists",
      halign = Gtk.Align.CENTER,
      wrap = True
    )
    self.lbl_title.get_style_context ().add_class ('title-1')
    self.box_header.append (
      self.lbl_title
    )

    self.box_listbox_wrapper = Gtk.Box (
      spacing = 20,
      orientation = Gtk.Orientation.VERTICAL
    )
    self.box_wrapper.append (
      self.box_listbox_wrapper
    )

    # ListBox
    self.listbox1 = Gtk.ListBox (
      selection_mode = Gtk.SelectionMode.NONE
    )
    self.listbox1.get_style_context ().add_class ('boxed-list')
    self.box_listbox_wrapper.append (
      self.listbox1
    )

    # Row 1
    self.row_listbox1_1 = Adw.ActionRow (
      title = 'ActionRow',
      subtitle = 'This ActionRow has subtitle and icon',
      icon_name = 'emblem-system-symbolic'
    )
    self.listbox1.append (
      self.row_listbox1_1
    )

    # Row 2
    self.row_listbox1_2 = Adw.ActionRow (
      title = 'ActionRow can have suffix widgets',
      icon_name = 'go-home-symbolic',
      subtitle = 'This listbox has subtitle, suffix widget and icon'
    )

    self.btn_listbox1_2_suffix = Gtk.Button (
      label = 'Button',
      halign = Gtk.Align.CENTER,
      valign = Gtk.Align.CENTER,
    )
    self.row_listbox1_2.add_suffix (
      self.btn_listbox1_2_suffix
    )

    self.listbox1.append (
      self.row_listbox1_2
    )

    # ListBox 2
    self.listbox2 = Gtk.ListBox (
      selection_mode = Gtk.SelectionMode.NONE
    )
    self.listbox2.get_style_context ().add_class ('boxed-list')
    self.box_listbox_wrapper.append (
      self.listbox2
    )

    # Row 1
    self.row_listbox2_1 = Adw.ActionRow (
      title = 'ActionRow can have prefix widgets',
      activatable = True
    )
    
    self.rd_listbox2_1_prefix = Gtk.CheckButton ()
    self.row_listbox2_1.add_prefix (
      self.rd_listbox2_1_prefix
    )
    self.row_listbox2_1.set_activatable_widget (
      self.rd_listbox2_1_prefix
    )

    self.listbox2.append (
      self.row_listbox2_1
    )

    # Row 2
    self.row_listbox2_2 = Adw.ActionRow (
      title = 'ActionRow can have prefix widgets',
      activatable = True
    )
    
    self.rd_listbox2_2_prefix = Gtk.CheckButton ()
    self.row_listbox2_2.add_prefix (
      self.rd_listbox2_2_prefix
    )
    self.rd_listbox2_2_prefix.set_group (
      self.rd_listbox2_1_prefix
    )
    self.row_listbox2_2.set_activatable_widget (
      self.rd_listbox2_2_prefix
    )

    self.listbox2.append (
      self.row_listbox2_2
    )

    # ListBox 3
    self.prfgr_listbox3 = Adw.PreferencesGroup (
      title = 'Expander Rows',
      margin_top = 10
    )
    self.box_wrapper.append (
      self.prfgr_listbox3
    )
    
    self.listbox3 = Gtk.ListBox (
      selection_mode = Gtk.SelectionMode.NONE
    )
    self.listbox3.get_style_context ().add_class ('boxed-list')
    self.prfgr_listbox3.add (
      self.listbox3
    )

    # ExpanderRow 1
    self.row_listbox3_1 = Adw.ExpanderRow (
      title = 'ExpanderRow',
      subtitle = 'This ActionRow has subtitle and icon',
      icon_name = 'emblem-system-symbolic'
    )
    self.listbox3.append (
      self.row_listbox3_1
    )

    for x in range(3):
      self.row_listbox3_1.add_row (
        Adw.ActionRow (
          title = 'Nested row',
        )
      )
    # ExpanderRow 2
    self.row_listbox3_2 = Adw.ExpanderRow (
      title = 'ExpanderRow',
      subtitle = 'With an action',
      icon_name = 'emblem-system-symbolic'
    )
    self.btn_listbox3_2_action = Gtk.Button.new_from_icon_name (
      'edit-copy-symbolic',
    )
    self.btn_listbox3_2_action.set_halign (Gtk.Align.CENTER)
    self.btn_listbox3_2_action.set_valign (Gtk.Align.CENTER)
    self.row_listbox3_2.add_action (
      self.btn_listbox3_2_action
    )
    self.listbox3.append (
      self.row_listbox3_2
    )

    for x in range(3):
      self.row_listbox3_2.add_row (
        Adw.ActionRow (
          title = 'Nested row',
        )
      )

    # ListBox 4
    self.prfgr_listbox4 = Adw.PreferencesGroup (
      title = 'Preferences Group has a suffix',
      margin_top = 10
    )
    
    self.btn_prfgr_listbox4_suffix = Gtk.Button ()
    self.btn_prfgr_listbox4_suffix.get_style_context ().add_class (
      'image-text-button'
    )
    self.btn_prfgr_listbox4_suffix.get_style_context ().add_class (
      'flat'
    )

    self.btn_prfgr_listbox4_suffix_content = Adw.ButtonContent (
      label = 'Button',
      icon_name = 'view-pin-symbolic'
    )
    self.btn_prfgr_listbox4_suffix.set_child (
      self.btn_prfgr_listbox4_suffix_content
    )

    self.prfgr_listbox4.set_header_suffix (
      self.btn_prfgr_listbox4_suffix
    )

    self.box_wrapper.append (
      self.prfgr_listbox4
    )
    
    self.listbox4 = Gtk.ListBox (
      selection_mode = Gtk.SelectionMode.NONE
    )
    self.listbox4.get_style_context ().add_class ('boxed-list')
    self.prfgr_listbox4.add (
      self.listbox4
    )

    # ExpanderRow 1
    self.row_listbox4_1 = Adw.ExpanderRow (
      title = 'ExpanderRow',
      subtitle = 'This ActionRow has subtitle and icon',
      icon_name = 'emblem-system-symbolic'
    )
    self.listbox4.append (
      self.row_listbox4_1
    )

    for x in range(3):
      self.row_listbox4_1.add_row (
        Adw.ActionRow (
          title = 'Nested row',
        )
      )

    # ExpanderRow 2
    self.row_listbox4_2 = Adw.ExpanderRow (
      title = 'ExpanderRow',
      subtitle = 'This ActionRow has subtitle and icon',
      icon_name = 'emblem-system-symbolic',
      show_enable_switch = True
    )
    self.listbox4.append (
      self.row_listbox4_2
    )

    for x in range(3):
      self.row_listbox4_2.add_row (
        Adw.ActionRow (
          title = 'Nested row',
        )
      )
    
    # ListBox 5
    self.prfgr_listbox5 = Adw.PreferencesGroup (
      title = 'Combo Rows',
      margin_top = 10
    )
    self.box_wrapper.append (
      self.prfgr_listbox5
    )

    self.listbox5 = Gtk.ListBox (
      selection_mode = Gtk.SelectionMode.NONE
    )
    self.listbox5.get_style_context ().add_class ('boxed-list')
    self.prfgr_listbox5.add (
      self.listbox5
    )

    self.strlist_listbox5_1 = Gtk.StringList ()
    self.strlist_listbox5_1.append ('Foo')
    self.strlist_listbox5_1.append ('Bar')
    self.strlist_listbox5_1.append ('Baz')
    # Row 1
    self.row_listbox5_1 = Adw.ComboRow (
      title = 'This a combo row'
    )
    self.row_listbox5_1.connect (
      'notify::selected-item',
      self.on_row_listbox5_1_select
    )
    self.row_listbox5_1.set_model (
      self.strlist_listbox5_1
    )
    self.listbox5.append (
      self.row_listbox5_1
    )
  def on_row_listbox5_1_select (self, widget, event):
    print (f'"{self.row_listbox5_1.get_selected_item ().get_string ()}" is selected.')

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
  application_id = 'io.github.afacanc38.adw-listbox'
)
app.run (sys.argv)