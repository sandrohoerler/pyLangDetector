#!/usr/bin/env python

"""Scans directory with text files and determines their languages"""

__author__      = "Sandro Hoerler"
__copyright__   = "Copyright 2020, fhgr.ch"

import os
from os import walk
from langdetect import detect

f = []
def count_files_with_language(filepath):
    for (dirpath, dirname, filenames) in walk(filepath):
        f.extend(filenames)
        documentLangCount = dict({})
        for (file) in filenames:
            with open(os.path.join(dirpath, file), "r") as content:
                if content.name.endswith(".txt"):
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
        for (file) in filenames:
            with open(os.path.join(dirpath, file), "r") as content:
                if content.name.endswith(".txt"):
                    text = content.read()
                   # ignores conversion errors
                    text = text.decode('utf-8', errors='ignore')
                    lang = detect(text)
                    if lang in language:
                        print(lang + "," + file)

def main():
    verbosity, filepath = raw_input("verbosity [print, count] and directory with .txt files to determine languages from: ").split()
    languages = count_files_with_language(filepath)
    if verbosity == "print":
       for key in languages:
          print_files_and_languages(filepath, key)

if __name__ == "__main__":
    main()