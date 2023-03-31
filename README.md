# Building Your Docker Image
docker build -t urlshortener .

# Run Your Django Docker Container
docker run -p 8000:8000 -t urlshortener

# Running URL Shortener app using Docker Compose
docker-compose up -d -—build
