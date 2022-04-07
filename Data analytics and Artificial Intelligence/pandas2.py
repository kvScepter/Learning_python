import pandas as pd
import numpy as np

#Read the first 10 rows from the gamedata.json file into the DataFrame. Then read the last five rows from the same file into another DataFrame. 
#Combine these two into one DataFrame
game = pd.read_json("gamedata.json")
game_head = game.head(10)
game_tail = game.tail(5)
game_combine = pd.concat([game_head,game_tail])

#Set steamRatingPercent to NaN for all rows having steamRatingCount below 1000
game.loc[game["steamRatingCount"] < 1000, "steamRatingPercent"] = np.nan

#Fill all NaN values in steamRatingPercent column by increasing the metacriticScore from the same row with 7 %
game["steamRatingPercent"].fillna(game.metacriticScore * 1.07)

#Group the data by steamRatingText column so that averages of the following columns will be calculated for each text value: 
#steamRatingPercent, metacriticScore, normalPrice and salePrice. Do not show any other columns in the resulting DataFrame
game1 = game[["steamRatingText", "steamRatingPercent", "metacriticScore", "normalPrice", "salePrice"]]
game1.groupby("steamRatingText").mean()

#Load the original game_data.json file content into a new DataFrame and then filter the data with the same manner as in previous task. 
#Combine these two DataFrames together and change the column names of the original to contain text ORIGINAL
game_original = pd.read_json("gamedata.json")
game_original.rename(columns={"steamRatingText":"ORIGINAL_SRText","steamRatingPercent":"ORIGINAL_SRPercent","metacriticScore":"ORIGINAL_Meta","normalPrice":"ORIGINAL_Normal","salePrice":"ORIGINAL_Sale" },inplace=True)
game_original1 = game_original[["ORIGINAL_SRText", "ORIGINAL_SRPercent", "ORIGINAL_Meta", "ORIGINAL_Normal", "ORIGINAL_Sale"]]
game2 = pd.concat([game1, game_original1])
