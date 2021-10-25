#!/bin/bash
targets="$@"

function vpn_connected () {
    while read -r line
    do
        if [[ "$line" == "0.0.0.0/1"*"dev tun"* ]]; then
            true
            return
        fi
    done < <(ip route)
    false
    return
}

echo -n "At startup, VPN is"
if vpn_connected; then
     echo "connected";
else
    echo "not connected";
fi

# dependencies:
# ip, pkill
# optional dependencies:
# notify-send

# Daemon mode: 
# 1. Look for falling edge of vpn connection
# 2. On falling edge, kill all targets passed as argument
# 3. To kill:
#  - pkill
polling_interval=1

# Initial setup
vpn_connected
previously_connected_status=$?
sleep $polling_interval

echo "Entering main service loop"
# Main dameon loop
while true; do
    if ! vpn_connected; then
        while IFS=" " read -r target; do
            # To keep the logs quiet, don't try and kill if it's not running 
            if ! pgrep $target >/dev/null 2>&1; then
                continue
            fi
            echo -n "Killing '$target'..."
            if pkill $target; then
                echo Success
            else
                echo Failed
                notify-send "Unable to VPN auto kill $target, you should close it!"
            fi
        done < <(echo $targets)
    fi
    sleep $polling_interval
done
