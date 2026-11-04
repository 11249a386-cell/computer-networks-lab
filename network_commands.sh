#!/bin/bash
# Run on Linux. Commands requiring unavailable utilities are skipped.
run_cmd() { echo -e "\\n$ $*"; if command -v "$1" >/dev/null 2>&1; then "$@"; else echo "$1 is not installed"; fi; }
run_cmd hostname
run_cmd ip addr
run_cmd ip route
run_cmd netstat -an
run_cmd nslookup google.com
run_cmd ping -c 4 google.com
run_cmd traceroute google.com
run_cmd arp -n
run_cmd tcpdump -D
