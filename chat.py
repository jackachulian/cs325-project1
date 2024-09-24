# Edit this to use a different model!
from_model = "phi3"

# Edit this to use a different system prompt.
system = "You are a personal AI assistant who is very helpful, and very precise, but with a super-dry sense of humor. You cannot resist being very witty and snarky when answering the questions." 

import ollama

# Create the model
model_name = "my_model"
modelfile=f'''
FROM {from_model}
SYSTEM {system}
'''
ollama.create(model=model_name, modelfile=modelfile)

# Read the input file
with open('prompts.txt', 'r') as prompts_file:
    lines = prompts_file.readlines()

# Array that stores the message history
messages = []

# For each line, pass it to the LLM and stream the response message content
with open("responses.txt", "w") as response_file:
    for line in lines:

        # Read the next line from the lines list.
        prompt = line.strip()

        # Print it to screen, write to output file, and append to message history
        print("> "+prompt)
        response_file.write("> "+prompt+"\n")
        messages.append({
            'role': 'user', 
            'content': prompt
        })

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
        response_file.write(response)
        response_file.write("\n\n")
        messages.append({
            'role': 'assistant', 
            'content': response
        })

        print()
        print()