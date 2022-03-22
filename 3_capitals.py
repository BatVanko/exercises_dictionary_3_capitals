country_names = input().split(", ")
capitals = input().split(", ")
country_capital = zip(country_names,capitals)
for country, capital in country_capital:
    print(f"{country} -> {capital}")