# C++ Runner Dockerfile
FROM gcc:latest

WORKDIR /sandbox

RUN addgroup judge && adduser -D -G judge judge
USER judge

COPY runner.sh /sandbox/

CMD ["bash", "runner.sh"]
