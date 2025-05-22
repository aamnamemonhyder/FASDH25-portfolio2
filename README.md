# FASDH25-portfolio2

## Objective of the Project & Data Sources  
The objective of this project is to identify toponyms using two methods:
1. **Regex-based matching** with a published gazetteer focused on the region of Gaza\
2. **Named Entity Recognition (NER)** using Python's Stanza library for a global detection

Both methods were applied to subsets of *Al-Jazeera English* articles, sourced from *Kaggle*


## directories

**gazetteer** - a list of toponyms in Gaza, including geographic coordinates, geoname IDs, and multilingual variants. The gazetteer is sourced from the *GeoNames* website\
**articles** - text files of *Al Jazeera English* articles (primarily from 2021 to 2024)\
**scripts** -
- **regex_script_aamna_2A.py** uses the gazetteer to find and count the toponym mentions in the articles\
- **regex_png.py** - a static PNG map\
- **regex_html.py** - an interactive HTML map\
- **2A_aamna.tsv** - stores regex-based frequency counts\
- **2B & 3_aamna.ipynb** - colab notebook containing scripts for the NER workflow\
- **ner_counts_aamna.tsv** - output of the NER script showing frequency of detected toponyms\
- **ner_gazetteer_aamna.tsv** - geographic coordinates of NER-detected toponyms

### advantages of using gazetteer

- suitable for focused research in a defined geographic region\
- ensures high precision, especially for multilingual variants of toponyms included in the gazetteer

### disadvantages of using gazetteer
- limited scope - only detects places listed in the gazetteer

### advantages of using NER
- suitable for broad geographic coverage, inclusing global place names.
- useful for exploratory research

### disadvantages of using NER 

- false negatives and positives
- context blindness
- low recall in historical texts
- post- processing required

#### misrecognized entities (2024 articles)
Stanza misclassified the following non-place entities as locations. They were supposed to be filtered out during post-processing:
corrections= {
    'Hezbollah’s': 'NORP',
    'X.\nSpain': 'MISC',
    'Al Jazeera’s': 'MISC',
    '@TomWhiteGaza':'PER',
    '#October7': 'DATE',
    '@MirandaCleland':'PER',
    '@carogennez':'PER',
    '@zarahsultana':'PER',
    'Abudaqa':'PER',
    'Nairoukh':'PER',
    'Motaz':'PER',
    '@azaizamotaz9':'PER',
    'Netanyahu’s':'PER',
    '@adoniaayebare':'PER',
    '@RepJayapal':'PER',
    '@RepCori':'PER',
    '@BasedMikelee':'PER',
    'Rawaa’s':'PER',
    'Thameen Darby':'PER',
    '@NaksBilal':'PER',
    '@Benarasiyaa':'PER',
    '@majedalansari':'PER',
    'Ahmadiyyah Zawiya':'PER',
    'Houthis’': 'NORP',
    'Ansarallah': 'NORP',
    'Houthi': 'NORP',
    'Jama’a Islamiya': 'NORP',
    'Hebrew': 'MISC',
    'taalbaya':'MISC',
    'rmeish':'MISC',
    'margaliot':'MISC',
    'zar’it':'MISC',
    'qffd':'MISC',
    'pashias':'MISC',
    '@palestine_un':'ORG',
    'africa4palestine':'ORG',
    'the\xa0Gaza Strip':'MISC',
    'jawwal':'ORG'
}

#### missing coordinates
The GeoNames function missed a couple of valid toponyms, therefore there coordinates were manually added to the NER gazetteer
1. Dahiyeh\
2. Philadelphi *(with tupo "Philadelphi" in original)*

Many of the coordinates fetched from GeoNames were are incorrect, for instance, the Gaza Strip, US, Sarit and many other places are marked incorrectly. These inaccuracies affect the NER-based map quality.

## Loophole in NER processing
Due to long processing times in Google Colab, only a subset of January 2024 articles was used for the NER experiment. The corrections dictionary shared above is based on an initial run over all January files but only a smaller dictionary relevant to the mini-dataset was used in the final NER workflow
