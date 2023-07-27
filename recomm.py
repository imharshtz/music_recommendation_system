import pandas as pd
import numpy as np

song_df = pd.read_csv("C:\Project\jupyter_notebook\music_recommendation_system\song_df.csv")
simm = np.load("C:\Project\jupyter_notebook\music_recommendation_system\cos_sim.npy")

def get_recommendations(idx, cosine_sim):
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    sim_scores.sort()
    song_index = [i[0] for i in sim_scores]
    song_index = song_index
    return song_index

def UseMe(song_input):
    song_index = song_df[song_df.eq(song_input).any(axis=1)].index
    song_index = song_index[0]
    rec_c = get_recommendations(song_index, simm)
    for i in rec_c:
        recomm = song_df.loc[song_df["id"] == i]
        recom = recomm[['name','artists']]
        print(recom)

lock = 1
while(lock!=0):
    song_input = input("Enter song you want to get recommendations for: ")
    UseMe(song_input)
    lock = int(input("Enter 0 to escape or 1 to continue"))