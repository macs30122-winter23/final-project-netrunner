# MACS30122 Final Project - Netrunners
## *Portrait of Economic Academia: Evidence from Top 20 Economics Journals from 2012 to 2022*
### Research Questions and Relevance
 * We form a whole picture of the current Economic academia by 
    1. identifying its collaboration patterns on Top Econ Journals through SNA
    2. research topics evolvement across time and institutions through dynamic TM.
 * We ask the following research questions:
    1. SNA: 
        - What are the network features and collaboration patterns at the institutional and tier level? Density, centrality, cross-rank freedom?
    2. TM:
        - How research topics vary and evolve across time and institutions? 
        - For each topic, who are the most important contributors?
    3. SNA & TM:
        - Do centralities in the network research the same topics?
        - For a centrality, who are parallel peers, who are distinct peers?
 * We have the following interesting findings:
    1. SNA: 
        - Top tier institutions are more likely to collaborate with institutions of similar levels; but for lower tier institutions, they often collaborate with those from very different tiers. In other words, an institution’s cross-rank/tier collaboration likelihood decreases as its tier/rank gets higher.
    2. TM:
        - Topics are stable in trends across time with some fluctuations but can vary a lot across different institutions.
    3. SNA & TM:
        - Centralities of university-institutions are relatively similar in what they research, but World Bank shows a large discrepancy against university-institutions.

### Data Sources
1. [Econpapers](https://econpapers.repec.org/)
2. [AEA](https://www.aeaweb.org/)
3. [IDEAS](https://ideas.repec.org/)
4. [Google Scholar](https://scholar.google.com/)

### Required Packages (can also see the requirements.txt)
1. bertopic==0.14.0
2. pandas==1.5.1
3. plotly==5.11.0
4. selenium==4.4.3
5. umap-learn==0.5.3
6. nltk==3.7
7. numpy==1.21.6
8. networkx==2.7.1
9. bs4==4.11.1

### Structure of Repo
* codes folder:
    1. [*ipynb*](https://github.com/macs30122-winter23/final-project-netrunner/tree/main/codes/ipynb): contains the Jupyter Notebook for data collection and analysis
    2. [*py*](https://github.com/macs30122-winter23/final-project-netrunner/tree/main/codes/py): contains scripts to scrape author/articles
    3. [*sql*](https://github.com/macs30122-winter23/final-project-netrunner/tree/main/codes/sql): contains the file to create database
    4. [*all_in_one_codes.ipynb*](https://github.com/macs30122-winter23/final-project-netrunner/blob/main/codes/all_in_one_codes.ipynb): main codes collected from the above 3 folders
* data folder:
    1. [*authors*](https://github.com/macs30122-winter23/final-project-netrunner/tree/main/data/authors): contains html files for Google Scholars profiles
    2. [*csv*](https://github.com/macs30122-winter23/final-project-netrunner/tree/main/data/csv): contains csv files used for database construction
    3. [*gephifiles*](https://github.com/macs30122-winter23/final-project-netrunner/tree/main/data/gephifiles): contains the gexf and Gephi Project files that uses for network visualization
    4. [*journals*](https://github.com/macs30122-winter23/final-project-netrunner/tree/main/data/journals): contains the raw data for Top 20 Economic Journals
* present folder:
    1. [*graph*](https://github.com/macs30122-winter23/final-project-netrunner/tree/main/present/graph): contains all the graphs we produce for visualizations
    2. [*ppt*](https://github.com/macs30122-winter23/final-project-netrunner/tree/main/present/ppt): contain both the presented version slides and an updated version

### Contributions:
1. **Data Scraping and Cleaning**:
    - Journal Top 1-6: Jerry Cheng
    - Journal Top 7-9: Yicheng Zhang
    - Journal Top 10-20: Hongzhang Xie
    - Author_Article Database: Jerry Cheng
    - Affiliation Database: Jerry Cheng
    - Author Database: Jerry Cheng, Yicheng Zhang
    - Affiliation Ranking Match: Yicheng Zhang
    - Missing Abstracts Matching: Yicheng Zhang
2. **Data Analysis and Visualization**:
    - Social Network Analysis: Jerry Cheng, Yicheng Zhang
    - Topic Modeling: Jerry Cheng
3. **Proposal, Slides, Progress Report, Final Report**:
    - Evenly distributed
4. **Codes Cleaning**:
    - Jerry Cheng, Hongzhang Xie
5. **Video Recording**:
    - Yicheng Zhang

### In-class Presentation Sildes
- [Presented Version](https://github.com/macs30122-winter23/final-project-netrunner/blob/main/present/ppt/Netrunner%20-%20MACS30122%20Final%20Project%20-%20Presented.pdf)
- [Updated Version](https://github.com/macs30122-winter23/final-project-netrunner/blob/main/present/ppt/Netrunners%20-%20MACS30122%20Final%20Project%20-%20Updated.pdf)

### Demonstration Video
- [Video Link](https://uchicagoedu-my.sharepoint.com/:v:/g/personal/zycheng_uchicago_edu/EZff7QMXKZNGhE3CpekBDm0B-z03txsei8BCRWwLLoYkFw?e=Ua32pa)


Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg