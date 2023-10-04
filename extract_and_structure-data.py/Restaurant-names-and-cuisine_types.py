#!/usr/bin/python3
import re

# Sample data containing 150 restaurant entries
data = """
Italian Delight - Italian, Spice Fusion - Indian, Sushi Heaven - Japanese,
Taste of India - Indian, French Bistro - French, Thai Spice - Thai,
Mamma Mia - Italian, Szechuan Palace - Chinese, Tex-Mex Grill - Mexican,
Greek Oasis - Greek, Red Curry House - Thai, BBQ Shack - American,
Casa de Tacos - Mexican, Sushi Express - Japanese, The Burger Joint - American,
Peking Garden - Chinese, Veggie Delight - Vegetarian, Pho Noodle House - Vietnamese,
"""

# Regular expression pattern
pattern = r'([\w\s]+) - ([\w\s]+)'

# Extract restaurant names and cuisine types
matches = re.findall(pattern, data)

# Organize the extracted data into a list of dictionaries
restaurants_data = []
for match in matches:
    restaurant_name = match[0]
    cuisine_type = match[1]
    restaurants_data.append({"Restaurant Name": restaurant_name, "Cuisine Type": cuisine_type})

# Print the extracted data for all 150 restaurants
for idx, restaurant in enumerate(restaurants_data, start=1):
    print(f"Restaurant {idx}:")
    print(f"Name: {restaurant['Restaurant Name']}")
    print(f"Cuisine: {restaurant['Cuisine Type']}")
    print()
