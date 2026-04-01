from data import items

def recommend(category):
    results = [item for item in items if item["category"] == category]
    return results
