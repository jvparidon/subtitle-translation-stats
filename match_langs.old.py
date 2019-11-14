import pandas as pd
import os
import zipfile
import imdb
import time


lang = 'bn'
ia = imdb.IMDb()

'''
df_imdb = pd.read_csv('title.akas.tsv', sep='\t', low_memory=False)
df_imdb['titleId'] = df_imdb['titleId'].str.replace('tt', '')

df_langs = df_imdb[df_imdb['language'] != '\\N']
#print(df_langs.tail())
#print(len(df_langs))

#df_lang_ww = df_langs[df_langs['region'] == 'XWW']
#print(df_lang_ww.tail())
#print(len(df_lang_ww))

df_originals = df_imdb[df_imdb['isOriginalTitle'] == '1']
df_originals = df_imdb[df_imdb['types'] == 'original']
#print(df_originals.tail())
#print(len(df_originals))

df_originals = df_originals.merge(df_langs, on='titleId')
#print(df_originals.tail())
#print(len(df_originals))
'''

# load subtitle foldernames from archive into df
print('reading zip archive')
read_zip = zipfile.ZipFile(f'../data/OpenSubtitles/raw/{lang}/{lang}.zip', 'r')
dirpath = 'OpenSubtitles/raw'
imdb_keys = []
subs_names = []
subs_years = []
for filepath in read_zip.namelist():
    if filepath.endswith('xml') and filepath.startswith(os.path.join(dirpath, lang)):
        #if len(filepath.split('/')[4]) > 7:
        #    print(filepath)
        imdb_keys.append(filepath.split('/')[4].zfill(7))
        subs_names.append(filepath.split('/')[5])
        subs_years.append(filepath.split('/')[3])

imdb_keys = sorted(list(set(imdb_keys)))
print('retrieving languages\n')
with open(f'{lang}_imdb_web_langs.tsv', 'w') as langfile:
    for imdb_key in imdb_keys:
        movie = ia.get_movie(imdb_key)
        languages = movie.get('languages', '')
        title = movie.get('title', '')
        line = f'{imdb_key}\t{title}\t{",".join(languages)}'
        print(line)
        langfile.write(f'{line}\n')
        #time.sleep(.4)

'''
#imdb_keys = list(set(imdb_keys))  # remove duplicates for testing
#df_subs = pd.DataFrame({'imdb key': imdb_keys, 'subs name': subs_names, 'subs year': subs_years})
df_subs = pd.DataFrame({'imdb key': list(set(imdb_keys))})

# merge with df_langs
print(f'number of subtitle files: {len(df_subs)}')
df_merged = df_subs.merge(df_imdb, left_on='imdb key', right_on='titleId')
df_merged = df_merged.sort_values(['titleId', 'ordering'])
print(f'number of files matched: {len(list(df_merged["titleId"].unique()))}')
print(df_merged[df_merged['titleId'] == '0457430'])
#print(df_merged.tail(3000).head(30))
df_merged.to_csv(f'{lang}_imdb_langs.tsv', sep='\t')
df_merged.tail(2000).to_csv(f'{lang}_imdb_langs.sample.tsv', sep='\t')
'''
