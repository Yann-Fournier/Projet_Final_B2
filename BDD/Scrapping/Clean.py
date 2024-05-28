import pandas as pd
import glob


def concat_csv(file):
    fichiers_csv = glob.glob('CSV/Save/' + file)

    dataframes = [pd.read_csv(fichier) for fichier in fichiers_csv]
    dataframe_combine = pd.concat(dataframes, ignore_index=True)
    # dataframe_combine = dataframe_combine.drop_duplicates()
    dataframe_combine = dataframe_combine.drop_duplicates(subset=['Nom'])

    # dataframe_combine.to_csv('CSV/Save/Shōnen_combined.csv', index=True)
    dataframe_combine.to_csv('CSV/Save/Auteurs_combined.csv', index=False)

# concat_csv("Sh*.csv")
concat_csv("Auteurs.csv")
