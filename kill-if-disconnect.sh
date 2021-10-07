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

if vpn_connected; then
     echo "connected";
else
    echo "not connected";
fi

# dependencies:
# ip, pkill

# Daemon mode: 
# 1. Look for falling edge of vpn connection
# 2. On falling edge, kill all targets passed as argument
# 3. To kill:
#  - pkill
polling_interval=1
vpn_connected
previously_connected_status=$?
sleep $polling_interval

while true; do
    vpn_connected
    current_status=$?
    if [[ ! $current_status -eq 0 && $previously_connected_status -eq 0 ]]; then
        echo "killing targets"
        while IFS=" " read -r target; do
        
            echo "would have killed '$target'"
        done < <(echo $targets)
    else
        echo "no change in connection status"
    fi
    previously_connected_status=$current_status
    sleep $polling_interval
done

sleep 1
