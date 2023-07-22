#
# Build image
#
FROM python:3.11 AS image-build

RUN apt update
RUN apt install -y --no-install-recommends \
    build-essential \
    python3-dev \
    gcc
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --use-pep517

#
# Production image
#
FROM python:3.11-alpine

# Container settings
ENV APP_USER app
ENV APP_DIR "/$APP_USER"

# Python security
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR 1

# App settings
ENV TIMEOUT 120
ENV DEBUG False
WORKDIR $APP_DIR
EXPOSE 8000

# Install dependencies from the build image venv
COPY --from=image-build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install the app
COPY app.py .
COPY dalai.py .
COPY config.py .

# Add user and group
RUN addgroup -S $APP_USER && \
    adduser -s /bin/true -u 1000 -D -h $APP_DIR -G $APP_USER $APP_USER

# Run the app
USER $APP_USER
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "$TIMEOUT", "app:app"]