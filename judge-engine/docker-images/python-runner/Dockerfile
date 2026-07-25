# Python Runner Dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /sandbox

# Setup isolation
RUN useradd -m -s /bin/bash judge
USER judge

COPY runner.py /sandbox/

CMD ["python", "runner.py"]
