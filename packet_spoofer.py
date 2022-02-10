"""
packet_spoofer.py - Craft and send spoofed UDP packets using Scapy.

Usage:
    python packet_spoofer.py --src <src_ip> --dst <dst_ip> --port <dst_port> --payload <data>

Requirements:
    pip install scapy
"""

import sys
import argparse
from scapy.all import IP, UDP, send


def send_packet(src_ip: str, dst_ip: str, dst_port: int, payload: str):
    """Craft a spoofed IP/UDP packet and send it on the wire."""
    if len(payload) > 150:
        print("[!] Payload must be 150 bytes or fewer.")
        sys.exit(1)

    ip = IP(src=src_ip, dst=dst_ip)
    udp = UDP(sport=1234, dport=dst_port)
    packet = ip / udp / payload
    send(packet, verbose=False)
    print(f"[+] Sent packet: {src_ip} -> {dst_ip}:{dst_port} | payload={repr(payload)}")


def main():
    parser = argparse.ArgumentParser(
        description="Craft and send a spoofed UDP packet via Scapy."
    )
    parser.add_argument("--src", required=True, help="Spoofed source IP address")
    parser.add_argument("--dst", required=True, help="Destination IP address")
    parser.add_argument("--port", required=True, type=int, help="Destination UDP port")
    parser.add_argument("--payload", required=True, help="Payload string (max 150 bytes)")
    args = parser.parse_args()

    send_packet(
        src_ip=args.src,
        dst_ip=args.dst,
        dst_port=args.port,
        payload=args.payload,
    )


if __name__ == "__main__":
    main()
