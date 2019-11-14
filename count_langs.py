import pandas as pd


lang = 'zh_cn'


def count_langs(lang):
    df = pd.read_csv(f'langs2/{lang}_imdb_tags.tsv', sep='\t')
    df['first language'] = df['languages'].apply(lambda x: str(x).split(',')[0])
    df_counts = df['first language'].value_counts()
    print(df_counts)
    df_counts.to_csv(f'langs/{lang}_imdb_tags.lang_counts.tsv', sep='\t')


count_langs(lang)
