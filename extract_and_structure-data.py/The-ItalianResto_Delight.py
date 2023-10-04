

import re

# data for the Italian Delight restauran
restaurant_data = """
Restaurant: Italian Delight - Italian
Ingredients: pasta, tomatoes, cheese, basil
Color: rgb(255, 0, 0)
Social Media: @italiandelight123
Product Code: ABC123
News Headline: Food Critic's Review: Italian Delight Impresses Again
Event: Grand Opening - Sep 15, 2023 - 06:00 PM
"""

# Regular expression patterns
restaurant_name_pattern = r'Restaurant: (.*)'
ingredients_pattern = r'Ingredients: (.*)'
color_pattern = r'Color: rgb\((\d+), (\d+), (\d+)\)'
social_media_pattern = r'Social Media: (@[\w\d]+)'
product_code_pattern = r'Product Code: ([A-Z]+\d+)'
news_headline_pattern = r'News Headline: (.*)'
event_pattern = r'Event: (.*) - (\w{3} \d{2}, \d{4} - \d{2}:\d{2} [APM]+)'

# Extract data for the restaurant
restaurant_name_match = re.search(restaurant_name_pattern, restaurant_data)
ingredients_match = re.search(ingredients_pattern, restaurant_data)
color_match = re.search(color_pattern, restaurant_data)
social_media_match = re.search(social_media_pattern, restaurant_data)
product_code_match = re.search(product_code_pattern, restaurant_data)
news_headline_match = re.search(news_headline_pattern, restaurant_data)
event_match = re.search(event_pattern, restaurant_data)

# Combine and print the extracted data
if restaurant_name_match:
    restaurant_name = restaurant_name_match.group(1)
    print(f"Restaurant Name: {restaurant_name}")

if ingredients_match:
    ingredients = ingredients_match.group(1).split(', ')
    print("Ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

if color_match:
    red = color_match.group(1)
    green = color_match.group(2)
    blue = color_match.group(3)
    print(f"Color: RGB({red}, {green}, {blue})")

if social_media_match:
    social_media_username = social_media_match.group(1)
    print(f"Social Media Username: {social_media_username}")

if product_code_match:
    product_code = product_code_match.group(1)
    print(f"Product Code: {product_code}")

if news_headline_match:
    news_headline = news_headline_match.group(1)
    print(f"News Headline: {news_headline}")

if event_match:
    event_details = event_match.group(1)
    event_datetime = event_match.group(2)
    print(f"Event Details: {event_details}")
    print(f"Event Date and Time: {event_datetime}")

