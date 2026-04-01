def run():
    print("=== AI Recommendation System ===\n")

    category = input("Choose a category (ai, marketing, programming, business): ")

    from recommender import recommend
    results = recommend(category)

    if not results:
        print("\nNo recommendations found.")
        return

    print("\nRecommended items:\n")

    for item in results:
        print(f"- {item['title']}")

if __name__ == "__main__":
    run()
