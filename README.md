# Usage

Generate an authentication token:

`$ python3 -c 'import secrets; print(secrets.token_urlsafe(32));'`

Hash the token:

`$ python3 -c 'import hashlib; print(hashlib.sha256("YOUR_TOKEN".encode()).hexdigest());'`

Edit `sql/init.sql` to insert the hash in the database:

`INSERT INTO token (token) VALUES ('YOUR_TOKEN');`

Deploy with Docker Compose:

`$ docker compose up -d`

Send requests over HTTP:

`$ curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: YOUR_TOKEN" -d "prompt=How are you?" http://localhost:8000/completion`

# Credits

Mobula uses code from dalaipy. Check it out here: [GitHub](https://github.com/wastella/dalaipy)

Check out DALAI here: [GitHub](https://github.com/cocktailpeanut/dalai)