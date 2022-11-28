# Quickstart

1. Before you can start working with repository you must have the *pipenv*. Please see the
documentation [Pipenv](https://pipenv.pypa.io/en/latest/).
2. After you have made sure that pipenv is installed, you must installed all the dependecies from ```Pipfile```. Use the following command to install:
  ```
    pipenv install --dev
  ```

3. To configure vscode to work with this repository, you can use the files in the vs_code_example directory. Just copy to the .vscode directory. If you haven't, just create this folder.
4. To start, just press `f5` key anywhere.


# Environment Variables

`API_KEY` - you must specify the API key from OKX client.

`API_SECRET_KEY` - you must specify the API_SECRET_KEY from OKX client.

`API_PASSPHRASE` - you must specify the API_PASSPHRASE from OKX client.

To use demo bot mode you must set `DEMO_MODE` to 1


# Start Celery Worker

If you don't have a docker -> <a href="https://docs.docker.com/engine/install/ubuntu/">install it</a>.

In order to setup broker run:

```
  docker run -d -p 5672:5672 rabbitmq
```

To run celery scheduler service you need:

```
  celery -A task worker --loglevel=info
```

```
  celery -A task beat --loglevel=info
```
One command per terminal!
