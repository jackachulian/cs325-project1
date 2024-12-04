This readme contains instructions on how to use chat.py to take in prompts from prompts.txt and respond to them.

## Ollama
Ollama is required to interact with the local language models.

Install it here: https://ollama.com/

Or on Github: https://github.com/ollama/ollama

## Installing the Models
This program will use the model phi3 by default. To install the model in Ollama, open the terminal and type:
```sh
ollama run phi3
```
If you would like to download and use a different model, download it and replace 'phi3' with the model of your choice. Make sure to also edit chat.py to use this model instead. You can find a list of models here: https://ollama.com/library
Once the terminal displays `Send a messsage`, this means the LLM was successfully downloaded. You can send it a prompt here to ensure it is working on your device.

## Virtual Environment
To start the virtual environment, open a terminal in this root folder and type:
```sh
python -m venv .venv
```
Then install the dependencies:
```sh
pip install -r requirements.txt
```

## Project 1: Read prompt from a text file
To run the project, run the Python script:
```sh
python chat.py
```
This script will read the prompts from `prompts.txt` and pass them to the AI one by one, printing them to the terminal and storing them in `responses.txt`.
To give the LLM different prompts, edit `prompts.txt`, putting one prompt per line (seperated by newlines).


## Project 2: Steam Reviews webscraper
To run the webscraper, run the Python script:
```sh
python scraper.py
```
To change the games that the webscraper scrapes the reviews of, go to Steam and find the game you want to webscrape. The ID will be in the website's URL.
For example, Mana Cycle's URL is https://store.steampowered.com/app/2864390. So the ID is "2864390".
Once you have the ID, add it to the `game_ids_to_scrape` list at the top of `scraper.py`.

## Project 3: AI determines Sentiment of scraped reviews
To run the script that makes the AI extract the sentiment of each review, run the Python script:
```sh
python semtiments.py
```
This will read all files in the steam_reviews directory. For each file, a new file is created, and each line of the reviews file is read and converted into (ideally) a single word: Positive, Negative or Neutral.

Then to view the extracted results as a graph, run the Python script:
```sh
python semtiment_graph.py
```
while will display the results in matplotlib, graphing Steam game versus review sentiment amount.