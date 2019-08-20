## Requirements

Python 3.6+

## Installing

1. Install `git`, `wget` and `openvpn` from your package manager
2. Clone this repository into a folder of your choice: `git clone https://github.com/ijustlovemath/nord-python.git your_folder_here`

## Using

    python nord.py > a.bash; bash a.bash

To connect automatically with TCP:

    python nord.py --tcp > a.bash; bash a.bash

To connect automatically with UDP:

    python nord.py --udp > a.bash; bash a.bash

## FAQ

Q. Why save the script output to a file and run that, why not just pipe into bash?

A. Firstly, so that you can read the script before executing it. You can pipe to bash/fish/zsh if you like, however.
