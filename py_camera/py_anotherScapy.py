def ip_mac_scanner_sim(hosts: str, local_mac: str):
    """
    网段IP&Mac ARP协议扫描器
    :param hosts: 网段 e.g.‘*.*.*.*/*’
    :param local_mac: 本地MAC地址，e.g.‘**-**-**-**-**-**’
    :return: dict { IP: MAC, .... }
    """
    from scapy.layers.l2 import Ether, ARP
    from scapy.sendrecv import srp

    packet = Ether(dst="ff:ff:ff:ff:ff:ff", src=local_mac) / ARP(pdst=hosts)
    _Answer, _unAnswer = srp(packet, timeout=2, verbose=0)

    result = {}

    for Send, Receive in _Answer:
        result[Receive[ARP].psrc] = Receive[ARP].hwsrc
    return result


if __name__ == '__main__':
    all_ip_dic = ip_mac_scanner_sim('192.168.105.185', '6c:7e:67:d0:e3:da')
    print(all_ip_dic)
