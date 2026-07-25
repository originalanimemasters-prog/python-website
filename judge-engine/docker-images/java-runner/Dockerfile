# Java Runner Dockerfile
FROM openjdk:11-jre-slim

WORKDIR /sandbox

RUN addgroup judge && adduser -D -G judge judge
USER judge

COPY runner.sh /sandbox/

CMD ["bash", "runner.sh"]
