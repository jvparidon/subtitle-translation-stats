import os
import pandas as pd


def count_token_estimates(folder):
    counts_files = sorted(os.listdir(folder))
    dfs = []
    for counts_file in counts_files:
        df = pd.read_csv(os.path.join(folder, counts_file), sep='\t', names=['original lang', 'unique count']).dropna()
        df['subtitle lang'] = counts_file.replace('_lang_counts.tsv', '')
        df['estimated word count'] = df['unique count']
        dfs.append(df)
    df = pd.concat(dfs)
    df = df.sort_values('unique count', ascending=False)
    df['estimated word count'] = (df['unique count'] / 200).astype(str) + 'M'
    df.to_csv('translation_word_count_estimates.tsv', sep='\t', index=False)


count_token_estimates('counts_tables')
