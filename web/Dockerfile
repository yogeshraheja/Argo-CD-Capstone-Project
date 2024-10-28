# BASE IMAGE
FROM ghcr.io/kmayer10/python-flask:latest
RUN apt-get install -y python3-requests
RUN mkdir -p /app/templates
WORKDIR /app
EXPOSE 8000
# Adding Application Code
COPY . .
# Command to start the container
CMD ["bash","startup.sh"]
