import re

# product codes
data = """
ABC123, XYZ456, PQR789,
LMN456, DEF789, GHI123,
JKL789, STU123, VWX456,
YZA123, BCD456, EFG789,
HIJ123, OPQ456, RST789,
UVW123, XYZ456, ABC789,
LMN123, GHI456, DEF789,
JKL123, STU456, VWX789,
YZA456, BCD123, EFG456,
HIJ789, OPQ123, RST456,
UVW789, XYZ123, ABC456,
LMN789, GHI123, DEF456,
JKL789, STU123, VWX456,
YZA789, BCD123, EFG456,
HIJ789, OPQ123, RST456,
"""

# Regular expression pattern
pattern = r'([A-Z]+)(\d+)'

# Extract product codes
matches = re.findall(pattern, data)

# Print the extracted product codes
for match in matches:
    letters = match[0]
    digits = match[1]
    print(f"Product Code: {letters}{digits}")
