# Usage

Edit `sql/init.sql` to add your authentication token. Generate one with this command:

`$ python3 -c 'import secrets; print(secrets.token_urlsafe(32));'`

Deploy with Docker Compose:

`$ docker compose up -d`

Send requests over HTTP:

`$ curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: YOUR_TOKEN" -d "prompt=How are you?" http://localhost:8000/completion`

# Credits

Mobula uses code from dalaipy. Check it out here: [GitHub](https://github.com/wastella/dalaipy)

Check out DALAI here: [GitHub](https://github.com/cocktailpeanut/dalai)