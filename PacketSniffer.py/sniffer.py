from scapy.all import sniff, IP, TCP, UDP
import sqlite3
from datetime import datetime

def log_to_db(pkt):
    if IP in pkt:
        conn = sqlite3.connect("packets.db")
        cur = conn.cursor()
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        proto = {6: 'TCP', 17: 'UDP'}.get(pkt[IP].proto, str(pkt[IP].proto))
        length = len(pkt)
        src_port = dst_port = flags = None
        if TCP in pkt:
            src_port = pkt[TCP].sport
            dst_port = pkt[TCP].dport
            flags = str(pkt[TCP].flags)
        elif UDP in pkt:
            src_port = pkt[UDP].sport
            dst_port = pkt[UDP].dport
        cur.execute('''
            INSERT INTO packets (timestamp, src_ip, dst_ip, src_port, dst_port, protocol, length, flags)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (datetime.now().isoformat(timespec="seconds"), src_ip, dst_ip, src_port, dst_port, proto, length, flags))
        conn.commit()
        conn.close()

sniff(prn=log_to_db, store=0)
from collections import defaultdict, deque
import time

scan_window = 10
scan_threshold = 20
flood_threshold = 100
ports_by_src = defaultdict(lambda: deque())
packets_by_src = defaultdict(lambda: deque())

def detect_anomaly(pkt):
    now = time.time()
    if IP in pkt:
        src_ip = pkt[IP].src
        # Port scan detection
        if TCP in pkt:
            dport = pkt[TCP].dport
            ports_by_src[src_ip].append((now, dport))
            while ports_by_src[src_ip] and now - ports_by_src[src_ip][0][0] > scan_window:
                ports_by_src[src_ip].popleft()
            if len(set(x[1] for x in ports_by_src[src_ip])) > scan_threshold:
                print(f"ALERT: Port scan from {src_ip}")
        # Flooding detection
        packets_by_src[src_ip].append(now)
        while packets_by_src[src_ip] and now - packets_by_src[src_ip][0] > scan_window:
            packets_by_src[src_ip].popleft()
        if len(packets_by_src[src_ip]) > flood_threshold:
            print(f"ALERT: Flooding from {src_ip}")
