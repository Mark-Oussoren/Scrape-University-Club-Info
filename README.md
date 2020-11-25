# Scrape-University-Club-Info
Grabs club names and emails for organizations using Campus Labs ~ 1600+ colleges. I recommend on club sites filtering by at least one organization because there can be 900+ organizations, but only 200 or so are relevant to you. If you want to go through multiple clubs, it's very easy to have selenium run in the background and add a loop to run through multiple college club page urls.

1. `cd /.../Scrape-University-Club-Info/requirements.txt`
2. `pip3 install -r requirements.txt`
3. `cd /.../Scrape-University-Club-Info`
4. `python parse_clubs.py --url --chrome --agent`

Finally, output should be both array of dicts of clubs + emails as well as xlxs file in the repo
