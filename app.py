import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    csv_path = os.path.join(current_dir, 'clubs_data.csv')
    print(f"\n[SYSTEM] Searching for database at: {csv_path}")

    try:
        df = pd.read_csv(csv_path)
        print("[SYSTEM] Database loaded successfully!\n")
        return df
    except FileNotFoundError:
        print(f"\n[ERROR] Could not find 'clubs_data.csv' at: {csv_path}")
        print("Tip: Make sure the CSV file is in the same folder as this script.")
        return None

def recommend_club():
    df = load_data()
    if df is None:
        return

    # User Interface
    print("="*40)
    print("   College Club Recommender  ")
    print("="*40)
    user_input = input("\nDescribe your interests (e.g., 'I like coding in Java and gaming'): ")

    if not user_input.strip():
        print("Please enter some interests to get a recommendation!")
        return

    tfidf = TfidfVectorizer(ngram_range=(1, 2))
    
    all_content = list(df['Description']) + [user_input]
    tfidf_matrix = tfidf.fit_transform(all_content)

    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    df['Match_Score'] = cosine_sim[0]
    
    recommendations = df.sort_values(by='Match_Score', ascending=False).head(3)

    print("\n" + "*"*30)
    print("TOP RECOMMENDATIONS FOR YOU:")
    print("*"*30)
    
    for i, (index, row) in enumerate(recommendations.iterrows(), 1):
        score_pct = round(row['Match_Score'] * 100, 2)
        print(f"{i}. {row['Club Name']} ({score_pct}% Match)")
    
    print("\nExplore these clubs on the college portal!")

if __name__ == "__main__":
    run_choice = "y"
    while run_choice.lower() == "y":
        recommend_club()
        run_choice = input("\nWould you like to search again? (y/n): ")
    print("\nGood luck with your club applications!")