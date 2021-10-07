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

function slow_kill () {
    pkill $targets
}

watch -n 5 -x bash -c slow_kill & 

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
    vpn_connected
    current_status=$?
    if [[ ! $current_status -eq 0 && $previously_connected_status -eq 0 ]]; then
        echo "VPN disconnected, killing targets"
        while IFS=" " read -r target; do
            echo -n "Killing '$target'..."
            if pkill $target; then
                echo Success
            else
                echo Failed
                notify-send "Unable to VPN auto kill $target, you should close it!"
            fi
        done < <(echo $targets)
    fi
    previously_connected_status=$current_status
    sleep $polling_interval
done
