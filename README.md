# Scrape-University-Club-Info
Grabs club names and emails for organizations using Campus Labs. Key is that you have to click on the filters on the Campus Lab page and select at least one filter otherwise you'll get an error about selecting the wrong button trying to log in. 

1. `cd /.../Scrape-University-Club-Info/requirements.txt`
2. `pip3 install -r requirements.txt`
3. `cd /.../Scrape-University-Club-Info`
4. `python parse_clubs.py --url --chrome --agent`

Finally, output should be both array of dicts of clubs + emails as well as xlxs file in the repo
