from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp

# 定义本地IP和网管IP
ip_address = ''
router = ''

# 创建ARP请求数据包
arp = ARP()
ether = Ether()
packet = ether / arp

# 发送ARP请求并获取响应
result = srp(packet, timeout=3)
