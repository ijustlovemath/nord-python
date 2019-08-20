import sys
import argparse
import urllib.request
import json

protocols = ["tcp", "udp"]

port_lookup = {
        "tcp" : "443"
        , "udp" : "1194"
}

base_config_path = "/etc/openvpn/ovpn_"

options = lambda:0
options.openvpn24 = False

def recommended_server():
    url = "https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations"
    request = urllib.request.Request(url=url, headers={"User-Agent":"Mozilla/5.0"})
    raw_json = urllib.request.urlopen(request).read()
    recommendations = json.loads(raw_json)
    return recommendations[0]["hostname"]

def install_dir(protocol):
    if options.openvpn24:
        return "/etc/openvpn/client"
    return f"{base_config_path}{protocol}"

def main(args):
    global options

    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("--openvpn24"
        , action="store_true"
        , help="install VPN configurations to /etc/openvpn/client instead of /etc/openvpn/ovpn_{tcp,udp}"
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

    options = parser.parse_args(args)

    server = recommended_server()

    print(f"echo Recommended server identified: {server}")

    # Download and install
    for protocol in protocols:
        port = port_lookup[protocol]
        config_file = f"{server}.{protocol}{port}.ovpn"
        config_file_url = ("https://downloads.nordcdn.com/configs/files/" 
                + f"ovpn_legacy/servers/{config_file}"
        )

        print(f"echo Downloading VPN configuration for {protocol.upper()}")
        print(f"wget -nv {config_file_url}")
        print(f"echo \"Installing VPN configuration for {protocol.upper()} (requires sudo)\"")
        print(f"sudo mv {config_file} {install_dir(protocol)}/"
            + f"{server}.{protocol}.ovpn"
        )

    for protocol in protocols:
        locals()[f"{protocol}_connect_cmd"] = f"sudo openvpn {install_dir(protocol)}/{server}.{protocol}.ovpn"

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

if __name__ == '__main__':
    main(sys.argv[1:])
