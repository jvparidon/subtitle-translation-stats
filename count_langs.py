import pandas as pd
import os


def count_langs(lang):
    df = pd.read_csv(f'movie_tables/{lang}_imdb_tags.tsv', sep='\t')
    df['first language'] = df['languages'].apply(lambda x: str(x).split(',')[0])
    df_counts = df['first language'].value_counts()
    print(df_counts)
    df_counts.to_csv(f'counts_tables/{lang}_lang_counts.tsv', sep='\t')


langs = sorted(os.listdir('movie_tables'))
langs = [lang.replace('_imdb_tags.tsv', '') for lang in langs]
for lang in langs:
    count_langs(lang)
