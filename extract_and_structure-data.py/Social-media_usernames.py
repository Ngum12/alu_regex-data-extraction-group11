import re

# social medis usernames for the restaurant
data = """
@italian_delight, @spice_fusion, @sushi_heaven,
@taste_of_india, @french_bistro, @thai_spice,
@mamma_mia, @szechuan_palace, @tex_mex_grill,
@greek_oasis, @red_curry_house, @bbq_shack,
@casa_de_tacos, @sushi_express, @the_burger_joint,
@peking_garden, @veggie_delight, @pho_noodle_house,
@pizza_paradise, @mexican_grill, @indian_spices,
@healthy_eats, @italian_cuisine, @seafood_delight,
@vegan_cafe, @taco_truck, @pasta_place,
@korean_bbq, @juicy_burgers, @sweet_treats,
@mediterranean_feast, @soul_food, @farm_to_table,
@hometown_diner, @breakfast_corner, @coffee_culture,
@sandwich_shop, @foodie_paradise, @food_truck,
@ice_cream_shop, @dessert_haven, @noodle_house,
@steakhouse, @chop_suey, @sushi_bar,
@brewery_pub, @wine_cellar, @craft_cocktails,
@juice_bar, @vegetarian_eats, @bbq_smokehouse,
@seafood_market, @asian_fusion, @gourmet_pizza,
"""

# Regular expression pattern
pattern = r'@([\w\d_]+)'

# Extract social media usernames
usernames = re.findall(pattern, data)

# Print the extracted usernames
for username in usernames:
    print(f"Username: {username}")

