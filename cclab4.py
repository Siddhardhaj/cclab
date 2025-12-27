def travel_budget(travel_guide):
  total_cost = 0
  for state,cost in travel_guide.items():
    total_cost += cost
    print(f"{state}:{cost}")
  return total_cost

travel_guide = {"Chennai":12000, "Mumbai":13000, "Delhi":14000}

travel_budget(travel_guide)

print(f"Total Cost : {total_cost}")
