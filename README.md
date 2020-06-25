# App Demo

docker run -d --name app-demo -p 5000:5000 \
           -e ENV_1=FirstSecret \
           -e ENV_1=SecondSecret \
           kadashy/app-demo:latest
