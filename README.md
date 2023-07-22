![Mobula logo](logo.png)

# Mobula is a self-hosted AI solution.

Quickly deploy web-based Dalai instances with token-based authentication using a secure Flask-based stack.

# Usage

Generate an authentication token:

`$ python3 -c 'import secrets; print(secrets.token_urlsafe(32));'`

Hash the token:

`$ python3 -c 'import hashlib; print(hashlib.sha256("YOUR_TOKEN".encode()).hexdigest());'`

Edit `sql/init.sql` to insert the hash in the database:

`INSERT INTO token (token) VALUES ('YOUR_TOKEN');`

Deploy with Docker Compose:

`$ docker compose up -d`

Send prompts over HTTP:

`$ curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: YOUR_TOKEN" -d "text=How are you?" http://localhost:8000/completion`

# Configuration

Mobula is configured to use the LLAMA 7B model by default, on four threads. To change the thread count, edit `app.py`:

```
    # Generate the request object from the prompt
    dalairequest = Dalai.generate_request(
        prompt=prompt,
        model=config.DALAI_MODEL,
        threads=1
    )
```

To change the model, change the variable in `docker-compose.yml`:

```
    environment:
      DALAI_MODEL: alpaca.7B
```

Then edit the `./dalai/Dockerfile` to install your model:

```
# Install dalai and its dependencies
RUN npm install dalai && \
    npx dalai alpaca setup && \
    npx dalai alpaca install 7B
```

# Credits

Mobula uses code from dalaipy. Check it out here: [GitHub](https://github.com/wastella/dalaipy)

Check out DALAI here: [GitHub](https://github.com/cocktailpeanut/dalai)