# FASDH25-portfolio2

## Objective of the Project & Sources of Data  
The objective of this project is to identify place names using two methods:
1. **Regex-based matching** with a published gazetteer focused on the region of Gaza.
2. **Named Entity Recognition (NER)** using Python's Stanza library for a global approach.

Both techniques were applied to subsets of Al-Jazeera's published news articles, which were taken from the *Kaggle*.

---

## Folder Structure
The portfolio repository contains the following folders:

1. **gazetteer/**
Contains a list of place names in Gaza, including geographic coordinates, geoname IDs, and alternate names in other languages. The gazetteer is sourced from the *GeoNames* website.
2. **articles/**
Contains the text of Al Jazeera English articles (mainly from 2021 to 2024).
3. **scripts/**
Conatins the following files:
    - **regex script:** Uses the gazetteer to find and count the place name mentions in the articles.
    - Two map visualizations of regex results:
      - A **static PNG map** ('regex png')
      - An **interactive HTML map** ('regex html')
    - A TSV file ('2A_aamna.tsv') that stores regex-based frequency counts.
    - A Colab notebook ('2B & 3_aamna.ipynb') containing scripts for the NER workflow.
    - Two additional TSV files:
      - 'ner_counts_aamna.tsv': Output of the NER script showing frequency of detected place names.
    - 'ner_gazetteer_aamna.tsv': Geographic coordinates of NER-detected place names.

    
---

## Advantages and Disadvantages of the Techniques

### Gazetteer + Regex

#### Advantages
- Suitable for focused research in a defined geographic region.
- Ensures high precision, especially for multilingual variants of place names included in the gazetteer.

#### Disadvantages
- Limited scope - only places listed in the gazetteer are detected.

### Stanza NER

#### Advantages
- Suitable for broad geographic coverage, inclusing global place names.
- Useful for exploratory research

#### Disadvantages


can misinterpret and leaves a valid placename behind. Reasons could be ? Another important drawback of Stanza NER model is that entities that are not placenames also get detected incorrectly. Our dataset of January 2024 had the following entitites misrecognized and had to be corrected in the code.

## Loophole in my project
Since the colab was taking very long to process the large data set of Jan 2024, I selected only a few articles from January to perform the NER exercise.  
Initially, when I started working on January 2024 files, I found the following entities with incorrect type assignments. However, this dictionary is not used in the project but a shorter dictionary relevant to my minidataset was created for errors.  

### Entities recognized incorrectly in Jan 2024 articles
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

### Missing coordinates

The coordinates function missed the values for the following places. They were added manually to the TSV of the gazetteer.
1. Dahiyeh
2. Philadelphi (with missing 'a')

Many of the coordinates fetched by the website 'geonames' are incorrect. the gaza Strip, US, Sarit and many other places are marked incorrectly in the ner map.

## Weaknesses of the project.
My data set for NER is very small.
