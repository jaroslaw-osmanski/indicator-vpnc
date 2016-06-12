#!/bin/sh

mkdir -p ~/.config/autostart/
mkdir -p ~/.local/bin
mkdir -p ~/.local/share/icons

cp indicator-vpnc.desktop ~/.config/autostart/
sed -i 's|HOME|'$HOME'|g' ~/.config/autostart/indicator-vpnc.desktop
 
cp indicator-vpnc.py ~/.local/bin 
cp vpn_alarming.svg  ~/.local/share/icons
cp vpn_off.svg  ~/.local/share/icons
cp vpn_on.svg ~/.local/share/icons
