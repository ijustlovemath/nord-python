## Requirements

Python 3.6+

## Installing

1. Install `geckodriver`, `wget`, `openvpn` and `firefox` from your package manager
2. Create a virtual environment:

        virtualenv venv --distribute
        source venv/bin/activate
        pip install -r requirements.txt

## Using

    python nord.py > a.bash; bash a.bash

To connect automatically with TCP:

    python nord.py --tcp > a.bash; bash a.bash

To connect automatically with UDP:

    python nord.py --udp > a.bash; bash a.bash

## FAQ

Q. Why save the script output to a file and run that, why not just pipe into bash?

A. Firstly, so that you can read the script before executing it, but more importantly, because if you don't, the Selenium driver will not have enough time to load the recommended server.

Q. A web browser pops up and then closes! Why is that?

A. That's Selenium doing its work. You can see what it's doing by reading the script.
