# nord-python: A simple CLI for connecting to NordVPN

## Features

- Easily connect using the provided `nord-connect` command
- Simple script, easy to read and audit the whole connection sequence
- Killswitch systemd service for ending programs after a disconnect (defaults to qbittorrent)
- Check if you're connected using the provided `vpn-connected` command. Use it silently in scripts as well:

```
vpn-connected -q && echo "vpn online" || echo "vpn offline"
``` 

## Requirements

Python 3.6+

## Installation

1. Install `git`, `wget` and `openvpn` from your package manager
2. Clone this repository into a folder of your choice: `git clone https://github.com/ijustlovemath/nord-python.git your_folder_here`
3. Run `install.sh`

## Usage

The included `nord-connect` script can be used to connect automagically. You'll need to save your login details in `/etc/openvpn/auth.txt`, that looks like this:

```
username
password
```

The username and password should be taken from here: https://my.nordaccount.com/dashboard/nordvpn/ , under "Advanced Configuration"

## Manual Usage

    python nord.py > a.bash; bash a.bash

To connect automatically with TCP:

    python nord.py --tcp > a.bash; bash a.bash

To connect automatically with UDP:

    python nord.py --udp > a.bash; bash a.bash

To have configuration files installed to `/etc/openvpn/client`, as is done in OpenVPN2.4+, pass in `--openvpn24`:

    python nord.py --openvpn24 > a.bash; bash a.bash


## FAQ

Q. Why save the script output to a file and run that, why not just pipe into bash?

A. Firstly, so that you can read the script before executing it. You can pipe to bash/fish/zsh if you like, however. You'll need OpenVPN configured to read your username and password from a configuration file, however.

Q. I'm getting this error:

ERROR: Cannot open TUN/TAP dev /dev/net/tun: No such device (errno=19)

What gives?

A. This happens when your kernel has been upgraded and you haven't rebooted. You'll have to reboot like a filthy Windows user to make the VPN work again.

Q. Where do scripts get saved when running `nord-connect`?

A. `mktemp` is used, so they'll be located in `/tmp/nord-python.XXXXXXX` for your review as needed.

Q. How do I configure the killswitch service?

A. For now, you have to add programs using the service file, which you can edit here and deploy using `install.sh`
