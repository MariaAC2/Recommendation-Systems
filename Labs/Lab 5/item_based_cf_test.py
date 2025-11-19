import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------
# 1. Load users (people.csv) and items (nike_data_2022_09.csv)
# ---------------------------------------------------------

# IMPORTANT:
# Replace 'user_id' below with the correct column from people.csv (e.g., 'id', 'name', etc.)
people_df = pd.read_csv("people.csv")
nike_df = pd.read_csv("nike_data_2022_09.csv")

# Select the first 10 users and first 15 items
num_users = 10
num_items = 15

users_df = people_df.head(num_users).copy()
items_df = nike_df.head(num_items).copy()

# Extract user identifiers (assuming first column uniquely identifies users)
user_ids = users_df["sp_id"].values
user_names = users_df["sales_person"].values

# Extract item identifiers and names (useful for printing recommendations)
item_ids = items_df["id"].values if "id" in items_df.columns else np.arange(num_items)
item_names = items_df["name"].values if "name" in items_df.columns else item_ids

# ---------------------------------------------------------
# 2. Build User–Item Matrix (ratings 1–5)
# ---------------------------------------------------------
# We generate synthetic ratings:
#   - 0 = no rating
#   - 1 to 5 = actual rating

np.random.seed(42)  # reproducibility

user_item_matrix = np.zeros((num_users, num_items), dtype=int)

rating_probability = 0.4  # 40% of entries will have a rating

for u in range(num_users):
    for i in range(num_items):
        if np.random.rand() < rating_probability:
            user_item_matrix[u, i] = np.random.randint(1, 6)  # rating 1–5

print("User–Item matrix (shape =", user_item_matrix.shape, "):")
print(user_item_matrix)

# ---------------------------------------------------------
# 3. Compute Item–Item Similarity (Cosine Similarity)
# ---------------------------------------------------------
# cosine_similarity expects shape (n_items, n_users)
# so we transpose the matrix

item_similarity = cosine_similarity(user_item_matrix.T)

print("\nItem–Item Similarity Matrix (shape =", item_similarity.shape, "):")
print(item_similarity)

# ---------------------------------------------------------
# 4. Item-Based Recommendation Function
# ---------------------------------------------------------

def recommend_items(user_index, user_item_matrix, item_similarity, top_k=3):
    """
    Computes item-based collaborative filtering recommendations.

    Parameters:
        user_index: index (0-based) of the target user in user_item_matrix
        user_item_matrix: matrix of user ratings
        item_similarity: cosine similarity between items
        top_k: number of recommended items to return

    Returns:
        - list of recommended item indices
        - array of predicted scores for all items
    """
    user_ratings = user_item_matrix[user_index]

    # Predicted score = weighted sum of similarities with items the user has rated
    predicted_scores = user_ratings @ item_similarity

    # Exclude items already rated by the user
    predicted_scores[user_ratings > 0] = -1e9

    # Get top_k highest scores
    recommended_indices = np.argsort(predicted_scores)[::-1][:top_k]

    return recommended_indices, predicted_scores

# ---------------------------------------------------------
# 5. Test Example: Recommend Items for a Selected User
# ---------------------------------------------------------

target_user_index = 4
target_user_label = user_names[target_user_index]

recommended_items, scores = recommend_items(
    user_index=target_user_index,
    user_item_matrix=user_item_matrix,
    item_similarity=item_similarity,
    top_k=5
)

print(f"\nRecommendations for user {target_user_label} (User number {target_user_index + 1}):")
for idx in recommended_items:
    print(
        f"- Item index {idx} | id={item_ids[idx]} "
        f"| name='{item_names[idx]}' | predicted_score={scores[idx]:.3f}"
    )

# Show original ratings for that user
print("\nOriginal ratings of selected user:")
print("Item index -> rating")
for i, r in enumerate(user_item_matrix[target_user_index]):
    if r > 0:
        print(f"  {i}: {r}")
