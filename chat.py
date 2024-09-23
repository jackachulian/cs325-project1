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

# For each line, pass it to the LLM and stream the response message content
with open("response.txt", "w") as response_file:
    for line in lines:
        prompt = line.strip()

        print("> "+prompt)
        response_file.write("> "+prompt+"\n")

        stream = ollama.chat(
            model=model_name,
            messages=[{
                'role': 'user', 
                'content': prompt
            }],
            stream=True
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
            response_file.write(chunk['message']['content'])

        response_file.write("\n\n")
        print()
        print()