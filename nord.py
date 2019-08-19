import sys
import argparse

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https:/nordvpn.com/servers/tools")

server = driver.find_element_by_class_name("mb-3").text

driver.quit()

protocols = ["tcp", "udp"]

port_lookup = {
        "tcp" : "443"
        , "udp" : "1194"
}

for protocol in protocols:
    port = port_lookup[protocol]
    config_file = f"{server}.{protocol}{port}.ovpn"
    config_file_url = ("https://downloads.nordcdn.com/configs/files/" 
            + f"ovpn_legacy/servers/{config_file}"
    )

    print(f"wget {config_file_url} > /dev/null")
    print(f"sudo mv {config_file} /etc/openvpn/ovpn_{protocol}/"
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

base_config_path = "/etc/openvpn/ovpn_"

for protocol in protocols:
    locals()[f"{protocol}_connect_cmd"] = f"sudo openvpn {base_config_path}{protocol}/{server}.{protocol}.ovpn"

if options.tcp or options.udp:
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
