```bash 
curl http://localhost:11434/api/generate -d '{
    "model": "llama3.2",
    "prompt": "Why is the sky blue?",
    "stream": false
}'
```

```bash 
curl http://localhost:11434/api/chat -d '{
    "model": "llama3.2",
    "messages": [{ "role": "user", "content": "Tell me a fun fact about India" }],
    "stream": false
}'
```