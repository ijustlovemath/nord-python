import sys
import argparse
import urllib.request
import json

url = "https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations"
request = urllib.request.Request(url=url, headers={"User-Agent":"Mozilla/5.0"})
raw_json = urllib.request.urlopen(request).read()
recommendations = json.loads(raw_json)
server = recommendations[0]["hostname"]

protocols = ["tcp", "udp"]

port_lookup = {
        "tcp" : "443"
        , "udp" : "1194"
}

base_config_path = "/etc/openvpn/ovpn_"

print(f"echo Recommended server identified: {server}")

for protocol in protocols:
    port = port_lookup[protocol]
    config_file = f"{server}.{protocol}{port}.ovpn"
    config_file_url = ("https://downloads.nordcdn.com/configs/files/" 
            + f"ovpn_legacy/servers/{config_file}"
    )

    print(f"echo Downloading VPN configuration for {protocol.upper()}")
    print(f"wget {config_file_url} >/dev/null 2>&1")
    print(f"echo \"Installing VPN configuration for {protocol.upper()} (requires sudo)\"")
    print(f"sudo mv {config_file} {base_config_path}{protocol}/"
        + f"{server}.{protocol}.ovpn"
    )

parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

group = parser.add_mutually_exclusive_group()

group.add_argument("--tcp"
        , action="store_true"
        , help="automatically connect to the server using TCP"
)

group.add_argument("--udp"
        , action="store_true"
        , help="automatically connect to the server using UDP"
)

options = parser.parse_args(sys.argv[1:])

for protocol in protocols:
    locals()[f"{protocol}_connect_cmd"] = f"sudo openvpn {base_config_path}{protocol}/{server}.{protocol}.ovpn"

if options.tcp or options.udp:
    print("echo Connecting automatically...")
    if options.tcp:
        print(tcp_connect_cmd)

    if options.udp:
        print(udp_connect_cmd)

else:
    for protocol in protocols:
        print("echo To connect with {upper}: {command}".format(
                upper=protocol.upper()
                , command=locals()[protocol + "_connect_cmd"]
            )
        )
