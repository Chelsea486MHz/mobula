from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import hashlib
import config
import dalai
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
db = SQLAlchemy(app)

# DALAI configuration
Dalai = dalai.Dalai()


# Represents the entries in the database
class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(64), unique=True, nullable=False)


@app.route('/completion', methods=['POST'])
def runCompletion():

    # Check if the authorization token is included in the request headers
    token = request.headers.get('Authorization')
    if not token:
        return 'Unauthorized', 401

    # Validate the hashed authorization token against the database
    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    print(hashed_token)
    if not Token.query.filter_by(token=hashed_token).first():
        return 'Unauthorized', 401

    # Get the prompt
    prompt = request.form.get('prompt')

    # Generate the request object from the prompt
    dalairequest = Dalai.generate_request(prompt=prompt, model=config.DALAI_MODEL)

    # Return the prompt completion
    return Dalai.request(dalairequest)


if __name__ == '__main__':
    app.run(os.environ.get('DEBUG', False))
