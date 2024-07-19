import ollama

#LIST MODELS
ollama.list()

model = 'does-not-yet-exist'

try:
  ollama.chat(model)
except ollama.ResponseError as e:
  print('Error:', e.error)
  if e.status_code == 404:
    ollama.pull(model)

#ollama.show('llama3')

#ollama.copy('llama3', 'sam/llama3')

#ollama.embeddings(model='llama3', prompt='The sky is blue because of rayleigh scattering')

#STREAM
#stream = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}], stream=True,)

#for chunk in stream:
#  print(chunk['message']['content'], end='', flush=True)

#CHAT
#print(ollama.chat(model='llama3', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}]))

#GENERATE
#print(ollama.generate(model='llama3', prompt='Why is the sky blue?'))

#Custom HOST
#from ollama import Client
client = ollama.Client(host='http://localhost:11434')
response = client.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'What is up?',
  },
], stream=True)

for chunk in response:
  print(chunk['message']['content'], end='', flush=True)

model = 'does-not-yet-exist'

