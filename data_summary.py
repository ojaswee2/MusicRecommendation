import pandas as pd

def print_data_summary(data):
    print("Data Summary:")
    print("Shape of data: ", data.shape)
    print("Columns: ", data.columns)
    print("Number of missing values: ", data.isnull().sum().sum())
    print("Number of duplicate rows: ", data.duplicated().sum())

spotify_df = pd.read_csv('spotify_dataset.csv', on_bad_lines='skip')
attributes_df = pd.read_csv('Spotify_Song_Attributes.csv')

print("== Spotify Playlist Dataset ==")
print_data_summary(spotify_df)

print("\n== Spotify Song Attributes Dataset ==")
print_data_summary(attributes_df)