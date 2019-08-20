## Requirements

Python 3.6+

## Installation

1. Install `git`, `wget` and `openvpn` from your package manager
2. Clone this repository into a folder of your choice: `git clone https://github.com/ijustlovemath/nord-python.git your_folder_here`

## Usage

    python nord.py > a.bash; bash a.bash

To connect automatically with TCP:

    python nord.py --tcp > a.bash; bash a.bash

To connect automatically with UDP:

    python nord.py --udp > a.bash; bash a.bash

To have configuration files installed to `/etc/openvpn/client`, as is done in OpenVPN2.4+, pass in `--openvpn24`:

    python nord.py --openvpn24 > a.bash; bash a.bash

## FAQ

Q. Why save the script output to a file and run that, why not just pipe into bash?

A. Firstly, so that you can read the script before executing it. You can pipe to bash/fish/zsh if you like, however.
