FROM python:3.10-slim

# App settings
WORKDIR /root/dalai
EXPOSE 3000

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    curl \
    g++ \
	git \
    make \
    python3-venv \
    software-properties-common

# Add NodeSource PPA to get Node.js 18.x
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -

# Install Node.js 18.x
RUN apt-get update
RUN apt-get install -y nodejs


# Install dalai and its dependencies
RUN npm install dalai && \
    npx dalai alpaca setup && \
    npx dalai llama install 7B

# Run the dalai server
CMD [ "npx", "dalai", "serve" ]