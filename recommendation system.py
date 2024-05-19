# Sample user-item ratings matrix (user_id: [ratings])
user_ratings = {
    'User1': {'Item1': 4, 'Item2': 5, 'Item3': 3, 'Item4': 2},
    'User2': {'Item1': 5, 'Item2': 4, 'Item3': 2, 'Item4': 3},
    'User3': {'Item1': 2, 'Item2': 3, 'Item3': 4, 'Item4': 5},
    'User4': {'Item1': 3, 'Item2': 2, 'Item3': 5, 'Item4': 4},
    'User5': {'Item1': 5, 'Item2': 2, 'Item3': 4, 'Item4': 3}
}

# Function to calculate similarity between two users using cosine similarity
def cosine_similarity(user1, user2):
    common_items = set(user1.keys()) & set(user2.keys())
    numerator = sum(user1[item] * user2[item] for item in common_items)
    denominator = (sum(user1[item] ** 2 for item in user1) ** 0.5) * (sum(user2[item] ** 2 for item in user2) ** 0.5)
    if denominator == 0:
        return 0
    return numerator / denominator

# Function to recommend items to a user based on collaborative filtering
def recommend_items(user_id, user_ratings):
    similarities = {}
    for other_user in user_ratings:
        if other_user != user_id:
            similarity = cosine_similarity(user_ratings[user_id], user_ratings[other_user])
            similarities[other_user] = similarity

    # Sort users by similarity in descending order
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    recommended_items = {}
    for item in user_ratings[user_id]:
        if user_ratings[user_id][item] == 0:
            weighted_sum = 0
            similarity_sum = 0
            for other_user, similarity in sorted_similarities:
                if item in user_ratings[other_user]:
                    weighted_sum += user_ratings[other_user][item] * similarity
                    similarity_sum += similarity
            if similarity_sum != 0:
                recommended_items[item] = weighted_sum / similarity_sum

    # Sort recommended items by rating in descending order
    sorted_recommendations = sorted(recommended_items.items(), key=lambda x: x[1], reverse=True)

    return sorted_recommendations

# Main function to test the recommendation system
def main():
    user_id = 'User1'
    recommendations = recommend_items(user_id, user_ratings)
    print(f"Recommendations for {user_id}:")
    for item, rating in recommendations:
        print(f"{item}: {rating}")

if __name__ == "__main__":
    main()
