# CS325 Project 2
Web scraper that takes in ids to Steam games and saves the top 10 reviews to a text file.

For instructions on the AI prompt responder (Project 1) look at chat-readme.md.

## Virtual Environment
To start the virtual environment, open a terminal in this root folder and type:
```sh
python -m venv .venv
```
Then install the dependencies:
```sh
pip install -r requirements.txt
```

## Running the project
To run the webscraper, run the Python script:
```sh
python scraper.py
```

## Changing the Steam games to webscrape
To change the games that the webscraper scrapes the reviews of, go to Steam and find the game you want to webscrape. The ID will be in the website's URL.
For example, Mana Cycle's URL is https://store.steampowered.com/app/2864390. So the ID is "2864390".
Once you have the ID, add it to the `game_ids_to_scrape` list at the top of `scraper.py`.
