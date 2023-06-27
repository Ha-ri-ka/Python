travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country, visits, list_of_cities):
    dict_to_add={
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    }
    travel_log.append(dict_to_add)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
