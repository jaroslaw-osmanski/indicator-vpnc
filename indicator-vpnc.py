 #!/usr/bin/env python

 
import gtk as Gtk
import appindicator as appindicator
import subprocess as subprocess 
 

VPN_ON = "vpn_on"
VPN_ALARMING = "vpn_alarming"
VPN_OFF = "vpn_off"
class VpnIndicator(object):
  def __init__(self):
    self.set_vpn_on_normal()
    self.ind = appindicator.Indicator(
                         "vpn-error",
                         "indicator-messages",
                         appindicator.CATEGORY_SYSTEM_SERVICES)
    self.ind.set_status (appindicator.STATUS_ACTIVE)
    self.ind.set_icon(VPN_OFF)
    self.current_icon = ""
    self.update_icon()
  def get_icon(self):
    if not VpnIndicator.is_running():
      return VPN_OFF
    return self.vpn_on_icon
  def update_icon(self):
    if self.get_icon() != self.current_icon:
      self.current_icon = self.get_icon()
      self.ind.set_icon(self.current_icon)
    return True
  
  def set_vpn_on_normal(self):
    self.vpn_on_icon = VPN_ON
  def set_vpn_on_alarming(self):
    self.vpn_on_icon  = VPN_ALARMING
  def change_vpn_on_icon(self, w):
    if not w.get_active ():
      self.set_vpn_on_normal()
    else:
      self.set_vpn_on_alarming()
  @staticmethod
  def is_running():
     output=subprocess.check_output("ps cax | grep vpnc | wc -l", shell=True)
     return output != '0\n'

if __name__ == "__main__":
   vpn_indicator = VpnIndicator()
   # create a menu
   menu = Gtk.Menu()
   Gtk.timeout_add(1000, vpn_indicator.update_icon)

   
   
   menu_check_box = Gtk.CheckMenuItem("VPN on should be alarming")
   menu.append(menu_check_box)
   menu_check_box.connect("toggled", vpn_indicator.change_vpn_on_icon)
   menu_check_box.show()

   menu_item = Gtk.MenuItem("Quit")
   menu_item.connect("activate", lambda w: Gtk.mainquit())
   menu.append(menu_item)
   menu_item.show()

   vpn_indicator.ind.set_menu(menu) 
   Gtk.main()
