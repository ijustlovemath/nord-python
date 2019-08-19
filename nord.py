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

    print(f"wget {config_file_url}")
    print(f"sudo mv {config_file} /etc/openvpn/ovpn_{protocol}/"
        + f"{server}.{protocol}.ovpn"
    )

