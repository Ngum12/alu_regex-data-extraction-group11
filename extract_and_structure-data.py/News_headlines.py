import re

# Sample API response containing news headlines
api_response = """
Here are some news headlines:
1. Breaking News: COVID-19 Cases Surge Again
2. Technology Update: New iPhone Launch Date Announced
3. Sports News: Team Wins Championship Game
"""

# Regular expression pattern to extract news headlines
pattern = r'Headline:\s*(.*?)(?=\n|$)'

# Find all matches in the API response
matches = re.findall(pattern, api_response, re.IGNORECASE)

# Extracted news headlines
news_headlines = [match.strip() for match in matches]

# Print the extracted news headlines
for i, headline in enumerate(news_headlines, start=1):
    print(f"{i}. {headline}")
