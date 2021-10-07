#!/bin/bash
targets="$@"

function vpn_connected () {
    while read -r line
    do
        if [[ "$line" == "0.0.0.0/1"*"dev tun0" ]]; then
            true
            return
        fi
    done < <(ip route)
    false
    return
}

if vpn_connected; then
     echo "connected";
else
    echo "not connected";
fi

sleep 1
