# App Demo

This app its a demo for validate a functional app, this app response a health check and a calculation of pi numbers using python and flask

## Calculate numbers of pi

get

/probe/pi

docker run -d --name app-demo -p 5000:5000 \
           -e ENV_1=FirstSecret \
           -e ENV_1=SecondSecret \
           kadashy/app-demo:latest
