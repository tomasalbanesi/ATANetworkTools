import psutil

def network_info():

    net_if_addrs = psutil.net_if_addrs()
    for interface, addresses in net_if_addrs.items():
        for address in addresses:
            print(f"Interfaz: {interface}")
            print(f"  Dirección: {address.address}")
            print(f"  Familia: {address.family}")
            print(f"  Máscara de red: {address.netmask}")
            print(f"  Dirección de transmisión: {address.broadcast}")