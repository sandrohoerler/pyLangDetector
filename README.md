# pyLangDetector
super simple language detector written in python using https://pypi.org/project/langdetect/. 
* counting of *.txt files per language
* printing out filename with language comma separated to easly use as csv
* supports 55 languages

### Supported languages
```af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw```
```
## Executiuon
count file per language in a folder


```buildoutcfg
python2 detectLanguage.py count {directory}
en : 171
de : 12
fr : 19
```

count file per language in a folder and print out language, filename tuple

```buildoutcfg
python2 detectLanguage.py print {directory}
en : 171
en,7 August 2003_0_0.txt
en,20 January 2016_0_0.txt
en,1 August 2002_0_0.txt
en,7 February 1998_0_0.txt
en,15 June 1998_0_0.txt
en,21 November 2015_0_0.txt
en,24 April 2000_0_0.txt
en,18 March 2001_0_0.txt
en,19 July 2004_0_0.txt
en,21 March 2011_0_0.txt
en,23 July 2012_0_0.txt
en,19 June 2018_0_0.txt
en,25 April 2002_0_0.txt
en,26 May 2012_0_0.txt
en,9 August 2013_0_0.txt
en,1 February 2011_0_0.txt
...
```
