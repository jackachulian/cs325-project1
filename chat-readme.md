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

## Running the project
To run the project, run the Python script:
```sh
python chat.py
```
The script will read the prompts from `prompts.txt` and pass them to the AI one by one, printing them to the terminal and storing them in `responses.txt`.

## Changing the prompts
The prompts from the project rubric are contained in prompts.txt, which the program will read from. To give the LLM different prompts, edit `prompts.txt`, putting one prompt per line (seperated by newlines).



Tutorial loosely followed to make this project: https://www.youtube.com/watch?v=xE0KAAuCb60
