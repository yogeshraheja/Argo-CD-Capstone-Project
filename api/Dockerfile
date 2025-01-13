# BASE IMAGE For Build
FROM ghcr.io/kmayer10/python-flask:latest
RUN apt-get update
RUN apt-get install -y python3-psycopg2
RUN mkdir /app
WORKDIR /app
EXPOSE 8000
# Adding Application Code
COPY . .
# Command to start the container
CMD ["bash","startup.sh"]
