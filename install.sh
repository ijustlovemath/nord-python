#!/bin/bash
sudo cp vpn-killswitch.service /etc/systemd/system/
sudo cp kill-if-disconnected.sh /usr/local/bin/
sudo systemctl enable vpn-killswitch.service --now
