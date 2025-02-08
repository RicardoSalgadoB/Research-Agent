# Efficiency Project 1: Publications by sector in Mexico
*A project that I could live without, yet it makes life a lot easier*

For some optative research, I needed to know how much of the scientific publications in the Mexico came from public and private institutions.

The first step was to download the yearly data (2016-2024) for research institutions in Mexico from the [Nature Index](https://www.nature.com/nature-index/).
*Note that the data coming from Nature Index describes information about the publications of the previous year. DO NOT GET CONFUSED BY THIS, it can make you use just a few hundred credits mor than needed*

You need to download the Nature Index datasets in a CSV file by yourselves and put them in a directory called "CSV_Academia". Here's a list from where you can get the CSVs:
* [2016](https://www.nature.com/nature-index/research-leaders/2016/institution/all/all/countries-Mexico)
* [2017](https://www.nature.com/nature-index/research-leaders/2017/institution/all/all/countries-Mexico)
* [2018](https://www.nature.com/nature-index/research-leaders/2018/institution/all/all/countries-Mexico)
* [2019](https://www.nature.com/nature-index/research-leaders/2019/institution/all/all/countries-Mexico)
* [2020](https://www.nature.com/nature-index/research-leaders/2020/institution/all/all/countries-Mexico)
* [2021](https://www.nature.com/nature-index/research-leaders/2021/institution/all/all/countries-Mexico)
* [2022](https://www.nature.com/nature-index/research-leaders/2022/institution/all/all/countries-Mexico)
* [2023](https://www.nature.com/nature-index/research-leaders/2023/institution/all/all/countries-Mexico)

I then made a program to read the data and tell me whether each institution is private or public. This is done using the TAVILY API, and yes, I began the project with 1000 credits and now I've ended up with 14; however I had 4 crashes, so I believe that the project takes no more than a 500 credits to complete.

In the [main file](main.py), I just structured this idea using a dictionary to hold whether each institution is public or private and a Pandas DataFrame to store the yearly "Nature Index's share" for public and private institutions.

If you run the code, there should be somwhere aroun here an Institution Dictionary JSON file (inst_dict.json) containing info on whether the institutions are public or private and a Returned DataFrame CSV file containing the results of running the program.

## Clarifications
* There are probably better options than TAVILY for this task, howver this is what I had at hand

Anyway, Goodbye.