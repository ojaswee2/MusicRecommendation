#Recommendations and Feedback

# Example user liked songs
liked_songs = ['save your tears', 'levitating']

# Normalize user feedback
liked_songs_nor = [s.lower().strip() for s in liked_songs]

# Get corresponding song_key 
liked_song_keys = merged_df[merged_df['track_name'].str.lower().str.strip().isin(liked_songs_nor)]['song_key'].tolist()

# Check if any liked songs were found in dataset
if not liked_song_keys:
    print("No liked songs in dataset")
else:
    print(f"Retraining model on {len(liked_song_keys)} liked songs...")

    # Retrain Word2Vec with liked songs 
    model.build_vocab([liked_song_keys], update=True)
    model.train([liked_song_keys], total_examples=1, epochs=5)

    print("Model updated with user feedback.")