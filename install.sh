#!/bin/bash
sudo cp vpn-killswitch.service /etc/systemd/system/
sudo cp kill-if-disconnected.sh /usr/local/bin/
sudo systemctl enable vpn-killswitch.service --now
sudo cp nord.py /usr/local/bin
sudo cp nord-connect /usr/local/bin
sudo cp vpn-connected /usr/local/bin
