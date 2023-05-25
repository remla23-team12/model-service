# model-service

This repository contains a docker file for building an image which can be used to spawn container that is a Flask web-service.

To give the model-service a test run, without the front-end [app](https://github.com/remla23-team12/app), the following instructions can be followed:

1. Make sure the Docker engine is running.
2. In your terminal make sure to navigate to the directory/folder where the `dockerfile` is located, if not already there.
3. In your terminal execute the following command and wait for it to finish:
    ```bat
    docker build -t test .
    ```
4. In your terminal execute the following command and wait for it to finish:
    ```bat
    docker run --rm -p8080:8080 test
    ```
    The exposed port of the container is port 8080 and it is forwarded to localhost's port 8080.
5. You can visit http://localhost:8080/apidocs/ to take a look at the API documentation provided by Flassger. `model-service` only accepts http POST requests. You could use curl or Postman to make a POST request to http://localhost:8080/ with the following contents in the body of the http request:
    ```json
    {
        "msg": "We are so glad we found this place."
    }
    ```
    The response will be:
    ```json
    {
        "message": "We are so glad we found this place.",
        "result": 1,
        "lib_version": "0.1.5"
    }
    ```
    The `result` key is mapped to the value 1, which means that the model predicts the message to have a postive sentiment.
    ```
    If you want to change lib version, make sure your chosen lib version exist, and modify requirements.txt
6. Once done you can use `Ctrl + C` in your terminal to exit and remove the container.
