import ollama

from_model = "phi3" # Edit this to use a different model!
system = "Respond with very brief answers." # Edit this to use a different system prompt.
model_name = "my_model"

# Create the model
modelfile=f'''
FROM {from_model}
SYSTEM {system}
'''
ollama.create(model=model_name, modelfile=modelfile)

# Read the input file
with open('prompts.txt', 'r') as prompts_file:
    lines = prompts_file.readlines()

messages = []

# For each line, pass it to the LLM and stream the response message content
with open("response.txt", "w") as response_file:
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