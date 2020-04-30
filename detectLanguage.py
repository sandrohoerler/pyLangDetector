# from langdetect import detect
import os
from os import walk
from langdetect import detect

filepath = "/home/sandro/data/projects/03_integrity/Korpus/trainingset_latest/integrity/negative"
mode, filepath = raw_input("Enter mode, directory with .txt files \n e.g. [count, print] [directory]: ").split()

f = []
def count_files_with_language(filepath):
    for (dirpath, dirname, filenames) in walk(filepath):
        f.extend(filenames)
        documentLangCount = dict({})
        for (file) in filenames:
            with open(os.path.join(dirpath, file), "r") as content:
                text = content.read()
                # ignores conversion errors
                text = text.decode('utf-8', errors='ignore')
                lang = detect(text)
                if lang in documentLangCount:
                    langCount = documentLangCount.get(lang)
                    langCount = langCount + 1;
                    documentLangCount.update({lang : langCount})
                else:
                    entry = {lang : 1}
                    documentLangCount.update(entry)
    for key in documentLangCount:
        print(key + " : " +  str(documentLangCount.get(key)))
    return documentLangCount

def print_files_and_languages(filepath, language):
    for (dirpath, dirname, filenames) in walk(filepath):
        f.extend(filenames)
        for (file) in filenames:
            with open(os.path.join(dirpath, file), "r") as content:
                text = content.read()
                # ignores conversion errors
                text = text.decode('utf-8', errors='ignore')
                lang = detect(text)
                if lang in language:
                    print(lang + "," + file)

if mode == "count":
    languages = count_files_with_language(filepath)
    for key in languages:
        print_files_and_languages(filepath, key)

#  print(filenames)
    #
    # if mode == "print":
    #     for (dirpath, dirname, filenames) in walk(filepath):
    #         f.extend(filenames)
    #         for (file) in filenames:
    #             with open(os.path.join(dirpath, file), "r") as content:
    #                 text = content.read()
    #                 # ignores conversion errors
    #                 text = text.decode('utf-8', errors='ignore')
    #                 lang = detect(text)
    #                 if lang in language:
    #                     print(file)
    #     #  print(filenames)
    # elif mode == "count":
    #     for (dirpath, dirname, filenames) in walk(filepath):
    #         f.extend(filenames)
    #         documentLangCount = dict({})
    #         documentIdPerLanguage = dict({})
    #         for (file) in filenames:
    #             with open(os.path.join(dirpath, file), "r") as content:
    #                 text = content.read()
    #                 # ignores conversion errors
    #                 text = text.decode('utf-8', errors='ignore')
    #                 lang = detect(text)
    #                 if lang in documentLangCount:
    #                     langCount = documentLangCount.get(lang)
    #                     langCount = langCount + 1;
    #                     documentLangCount.update({lang: langCount})
    #                 else:
    #                     entry = {lang: 1}
    #                     documentLangCount.update(entry)
    #     for key in documentLangCount:
    #         print(key + " : " + documentLangCount.get(key))
