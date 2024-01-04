#!/usr/bin/env python3

import subprocess
import sys
import json

#print(sys.argv)

if sys.argv[1] == "Get":
    if sys.argv[3] == "On":
        result = subprocess.run(["tailscale", "funnel", "status","--json"], stdout=subprocess.PIPE, text=True)
 #       print(result)
        result =json.loads(result.stdout)
        if "AllowFunnel" in result:
            print(1)
        else:
            print(0)
    sys.exit(0)

if sys.argv[1] == "Set":
    if sys.argv[3] == "On":
        if sys.argv[4] == "1":
            subprocess.run(["sudo", "tailscale", "serve", "-bg", "--https=443","off"])
            subprocess.run(["sudo", "tailscale", "funnel", "-bg", "--https=443","80"])
            sys.exit(0)
        else:
            subprocess.run(["sudo", "tailscale", "funnel", "-bg", "--https=443","off"])
            subprocess.run(["sudo", "tailscale", "serve", "-bg", "--https=443","80"])
            sys.exit(0)
