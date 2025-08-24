# asteroids

Arcade classic Asteroids, coded in Python with Pygame!

## How to run the code

### Docker:
1. Build the image
  ```
  docker build -t asteroids-app .
  ```
2. Run the container
  ```
  docker run --rm -it asteroids-app
  ```

  ```--rm``` automatically removes the container after your exit. 
  ```-it``` runs the container in interactive mode.

### Running on your bare metal:
I used ```uv``` as the package manager for this project. If you do not have it installed, you can check out how to install it on your system [here](https://github.com/astral-sh/uv)

After installing uv and downloading/cloning the repo. You can run the code by doing the following:

1. Create the venv
  ```
  python3 -m .venv
  ```
  or
  ```
  uv venv
  ```

2. Activate the venv
  ```
  source .venv/bin/activate
  ```

3. Run the main program
  ```
  uv run main.py
  ```

Enjoy!
