

docker build -f Dockerfile.abc -t v1.0.0 ..
docker tag v1.0.0 latest
docker tag v1.0.0 host/
