def find_famous_cat(cats):
  famous_stats = {
    "famous_cats": [],
    "max_followers": 0
  }
  
  for cat in cats:
    total_followers = 0
    for num in cat["followers"]:
      total_followers += num
      
    if total_followers > famous_stats["max_followers"]:
      famous_stats["max_followers"] = total_followers
      famous_stats["famous_cats"] = []
      famous_stats["famous_cats"].append(cat["name"])
    elif total_followers == famous_stats["max_followers"]:
      famous_stats["famous_cats"].append(cat["name"])
  
  return famous_stats["famous_cats"]
                                
response = find_famous_cat([
  {
    "name": "Luna",
		"followers": [500, 200, 300]
   },
   {
		"name": "Michi",
		"followers": [100, 500]
   }
])

print(response)

#codigo propio desafio


def find_famous_cat(cat_list):
    max_followers = 0
    famous_cats = []

    for cat in cat_list:
        followers = max(cat["followers"])
        if followers > max_followers:
            max_followers = followers
            famous_cats = [cat["name"]]
        elif followers == max_followers:
            famous_cats.append(cat["name"])

    return famous_cats

cats = [
    {
        "name": "Luna",
        "followers": [500, 200, 300]
    },
    {
        "name": "Michi",
        "followers": [100, 300]
    }
]

result = find_famous_cat(cats)
print(result)  # Salida: ["Luna"]

cats = [
    {
        "name": "Luna",
        "followers": [500, 200, 300]
    },
    {
        "name": "Michi",
        "followers": [100, 300]
    }
]

result = find_famous_cat(cats)
print(result)  # Salida: ["Luna", "Michi"]
