import re
data = """
flour, rice, chicken, beef,
pork, spinach, broccoli, carrots, potatoes,
beans, peas, mushrooms, bell peppers, cilantro,sugar, eggs, milk, butter,
salt, pepper, garlic, onion, tomatoes,
cheese, pasta, cumin, paprika, oregano, thyme, basil,
rosemary, lemon, lime, orange, ginger,
cinnamon, nutmeg, vanilla, honey, olive oil,
kale, arugula, quinoa, cheddar cheese, salmon,
vinegar, soy sauce, mustard, ketchup, mayonnaise,
"""

# Regular expression pattern
pattern = r'([^,]+)'

# Extract ingredients
ingredients = re.findall(pattern, data)

# Print the extracted ingredients
for ingredient in ingredients:
    print(f"Ingredient: {ingredient.strip()}")

