# A project crawling covid data on internet
# Libraries
```
pip install -r requirements.txt
```
# Crawling Data
I have implemented 2 crawlers   
The first crawler crawls data in Vietnam in the last month
```
python crawl_by_time.py
```
The second one can crawl data from 63 provinces in Vietnam. (However, I crawl only the total number of cases and the number of cases in yesterday each province)
```
python crawl_by_province.py
```
