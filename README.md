# Pcap Explorer

A collection of Python utilities for network packet analysis and custom packet crafting using [Scapy](https://scapy.net/).

## Tools

### `packet_spoofer.py`

Craft and send a spoofed UDP packet with a custom source IP, destination IP, port, and payload.

Useful for testing firewall rules, studying packet routing behavior, and understanding how source IP fields are treated at different network layers.

## Requirements

- Python 3.8+
- Scapy
- Root / Administrator privileges (required for raw socket access)

```bash
pip install -r requirements.txt
```

## Usage

### Packet Spoofer

```bash
sudo python packet_spoofer.py \
    --src 192.168.1.50 \
    --dst 10.0.0.1 \
    --port 9999 \
    --payload "hello"
```

| Flag | Description |
|------|-------------|
| `--src` | Spoofed source IP address |
| `--dst` | Destination IP address |
| `--port` | Destination UDP port |
| `--payload` | Payload string (max 150 bytes) |

### Analyzing PCAPs

Use the tools below alongside Scapy's built-in PCAP reading for traffic analysis:

```python
from scapy.all import rdpcap, IP, UDP, DNS

packets = rdpcap("capture.pcap")
for pkt in packets:
    if IP in pkt:
        print(pkt[IP].src, "->", pkt[IP].dst)
```

## Notes

- Raw socket operations require elevated privileges on most operating systems.
- Use only on networks you own or have explicit permission to test.
- Spoofed packets will not receive responses unless you control the routing path.

## License

MIT
