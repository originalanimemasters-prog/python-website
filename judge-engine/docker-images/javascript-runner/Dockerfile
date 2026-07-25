# JavaScript Runner Dockerfile
FROM node:18-alpine

WORKDIR /sandbox

RUN addgroup -S judge && adduser -S judge -G judge
USER judge

COPY runner.js /sandbox/

CMD ["node", "runner.js"]
