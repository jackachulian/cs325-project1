import os
import ollama

# Edit this to use a different model!
from_model = "phi3"

# Edit this to use a different system prompt.
system = "Only reply witha  single word based on teh sentiment of any comment given to you: Positive, Negative or Neutral." 

# Create the model
model_name = "my_model"
modelfile=f'''
FROM {from_model}
SYSTEM {system}
'''

ollama.create(model=model_name, modelfile=modelfile)

def respond_to_reviews(filename, sentiment_filename):
    # Read the input file
    with open(filename, 'r', errors="ignore") as prompts_file:
        lines = prompts_file.readlines()

    # For each line, pass it to the LLM and stream the response message content
    with open(sentiment_filename, "w", errors="ignore") as response_file:
        for line in lines:

            # Read the next line from the lines list.
            review = line.strip()
            if not review:
                continue
            prompt = "Describe this reivew and reply with only one word: positive, negative or neutral:\n"+review

            # Print it to screen, write to output file, and append to message history
            print("> "+review)
            messages = [{
                'role': 'user', 
                'content': prompt
            }]

            # Start a stream and read from it to continuously print to the screen
            stream = ollama.chat(
                model=model_name,
                messages=messages,
                stream=True
            )
    
            # Continuously print the message, and store the response in a string by appending incoming content
            response = ""
            for chunk in stream:
                content = chunk['message']['content']
                print(content, end='', flush=True)
                response = response + content

            # Write final reponse to the file and add a new message to history
            response_file.write(response.replace("\n", " ")+'\n')

            print()
            print()

reviews_directory_path = 'steam_reviews'
sentiment_directory_path = 'sentiments'
os.makedirs(sentiment_directory_path, exist_ok=True)
filenames = [f for f in os.listdir(reviews_directory_path) if os.path.isfile(os.path.join(reviews_directory_path, f))]

for filename in filenames:
    input_filename = os.path.join(reviews_directory_path, filename)
    sentiment_filename = os.path.join(sentiment_directory_path, filename)
    respond_to_reviews(input_filename, sentiment_filename)