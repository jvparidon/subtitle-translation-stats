import pandas as pd
import os
import zipfile
import imdb
import time


ia = imdb.IMDb()
def imdb_lookup(lang):
    #print(f'reading {lang} zip archive')
    read_zip = zipfile.ZipFile(f'../data/OpenSubtitles/raw/{lang}/{lang}.zip', 'r')
    dirpath = 'OpenSubtitles/raw'
    imdb_keys = []
    subs_names = []
    subs_years = []
    for filepath in read_zip.namelist():
        if filepath.endswith('xml') and filepath.startswith(os.path.join(dirpath, lang)):
            imdb_keys.append(filepath.split('/')[4].zfill(7))
            subs_names.append(filepath.split('/')[5])
            subs_years.append(filepath.split('/')[3])

    unique_imdb_keys = sorted(list(set(imdb_keys)))
    #print('retrieving imdb data\n')
    tags = sorted([
        #'cast',
        'genres',
        'runtimes',
        'countries',
        'country codes',
        'language codes',
        #'color info',
        #'aspect ratio',
        #'sound mix',
        #'box office',
        #'certificates',
        #'original air date',
        'rating',
        'votes',
        #'cover url',
        #'plot outline',
        'languages',
        'title',
        'year',
        'kind',
        #'directors',
        #'writers',
        #'producers',
        #'composers',
        #'cinematographers',
        #'editors',
    ])
    with open(f'langs2/{lang}_imdb_tags.tsv', 'w') as langfile:
        langfile.write('imdb key\t' + '\t'.join(tags) + '\n')
        for imdb_key in unique_imdb_keys:
            movie = ia.get_movie(imdb_key)
            entries = [movie.get(tag) for tag in tags]
            entries = [entry if entry is not None else '' for entry in entries]
            #for i, entry in enumerate(entries):
            #    if type(entry) is list:
            #        entry = [subentry.get('name') if hasattr(subentry, 'get') else subentry for subentry in entry]
            #        entries[i] = [subentry if subentry is not None else '' for subentry in entry]
            entries = [','.join(entry) if type(entry) is list else str(entry) for entry in entries]
            line = imdb_key + '\t' + '\t'.join(entries)
            print(line)
            langfile.write(line + '\n')


if __name__ == '__main__':
    langs = reversed(sorted(os.listdir('../data/OpenSubtitles/raw')))
    for lang in langs:
        imdb_lookup(lang)
