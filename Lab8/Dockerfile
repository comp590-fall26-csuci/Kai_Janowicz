FROM debian:13-slim

WORKDIR /app

run apt-get update && apt-get install -y build-essential

COPY /Lab3/ /app/
COPY /Lab8/script.sh /app/script.sh

RUN chmod +x /app/script.sh 

ENTRYPOINT ["/app/script.sh"]
CMD ["ls"]
