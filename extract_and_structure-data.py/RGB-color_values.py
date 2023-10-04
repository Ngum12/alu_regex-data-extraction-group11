#!/usr/bin/python3

import re

data = """
rgb(255, 0, 0), rgb(0, 255, 0), rgb(0, 0, 255),
rgb(255, 255, 0), rgb(255, 0, 255), rgb(0, 255, 255),
rgb(128, 128, 0), rgb(128, 0, 128), rgb(0, 128, 128),
rgb(192, 192, 0), rgb(192, 0, 192), rgb(0, 192, 192),
rgb(128, 0, 0), rgb(0, 128, 0), rgb(0, 0, 128),
rgb(255, 128, 0), rgb(255, 0, 128), rgb(128, 255, 0),
rgb(0, 255, 128), rgb(128, 0, 255), rgb(0, 128, 255),
rgb(64, 64, 0), rgb(64, 0, 64), rgb(0, 64, 64),
rgb(192, 192, 192), rgb(128, 128, 128), rgb(64, 64, 64),
rgb(255, 128, 128), rgb(128, 255, 128), rgb(128, 128, 255),
rgb(255, 255, 128), rgb(128, 255, 255), rgb(255, 128, 255),
rgb(192, 0, 0), rgb(0, 192, 0), rgb(0, 0, 192),
rgb(255, 192, 0), rgb(255, 0, 192), rgb(192, 255, 0),
rgb(0, 255, 192), rgb(192, 0, 255), rgb(0, 192, 255),
rgb(255, 64, 0), rgb(255, 0, 64), rgb(64, 255, 0),
rgb(0, 255, 64), rgb(64, 0, 255), rgb(0, 64, 255),
"""

# Regular expression pattern
pattern = r'rgb\((\d+), (\d+), (\d+)\)'

# Extract RGB color values
matches = re.findall(pattern, data)

# Print the extracted color values
for match in matches:
    red = match[0]
    green = match[1]
    blue = match[2]
    print(f"RGB Color: ({red}, {green}, {blue})")
