import re
data = """
flour, sugar, eggs, milk, butter,
salt, pepper, garlic, onion, tomatoes,
cheese, pasta, rice, chicken, beef,
pork, spinach, broccoli, carrots, potatoes,
beans, peas, mushrooms, bell peppers, cilantro,
cumin, paprika, oregano, thyme, basil,
rosemary, lemon, lime, orange, ginger,
cinnamon, nutmeg, vanilla, honey, olive oil,
vinegar, soy sauce, mustard, ketchup, mayonnaise,
kale, arugula, quinoa, cheddar cheese, salmon
"""

# Regular expression pattern
pattern = r'([^,]+)'

# Extract ingredients
ingredients = re.findall(pattern, data)

# Print the extracted ingredients
for ingredient in ingredients:
    print(f"Ingredient: {ingredient.strip()}")
