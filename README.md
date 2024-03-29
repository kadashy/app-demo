# Flask Demo App for Kubernetes

This is a demo Flask application designed to be run in a Kubernetes cluster. The app has four defined routes, each implemented by a resource class:

- `/probe/healthy`: Returns the "up" status if the application is running correctly. It also displays the value of the `ENV_1` environment variable.

- `/probe/unhealthy`: Returns the "down" status and an HTTP response code 500 to indicate that the application is not functioning correctly.

- `/probe/error`: Shuts down the application with an exit code of 0. This resource simulates a runtime error.

- `/probe/pi`: Calculates the value of Pi with a number of digits specified by the `pinumbers` parameter. The result is returned as a string.

To run the Flask application, simply run the file in your terminal as follows:

Make sure all dependencies are installed before running the application.

## Example CURL requests

Here are some example CURL requests for each of the defined routes:

### /probe/healthy

`curl http://localhost:5000/probe/healthy`

_Response:_

`{"status": "up", "Env 1": "value_1"}`


### /probe/unhealthy

`curl http://localhost:5000/probe/unhealthy`

_Response:_

`{"status": "down"}`


### /probe/error


_Note:_ This route does not return an HTTP response, as the application shuts down with an exit code of 0.

### /probe/pi

`curl http://localhost:5000/probe/pi?pinumbers=5`

_Response:_

`{"status": "up", "PiCalc": "3.1416"}`

## Run on Kubernetes
`kubectl apply -f https://raw.githubusercontent.com/kadashy/app-demo/master/deployment.yml`

## Run app on Docker

```
docker run -d --name app-demo -p 5000:5000 \
           -e ENV_1=FirstSecret \
           -e ENV_1=SecondSecret \
           kadashy/app-demo:latest
```
