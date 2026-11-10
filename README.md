# Password Generator

This program lets users enter their name and choose from three options for what kind of password they want.

## How to run
1. Install Flask: 3.14
2. In the project folder, run: flask run
3. Open Visual Studio Code in the browser

## The three modes
- **Classic:** It takes the name, capitalizes the first letter, and adds 4 random numbers.
- **Mixed:** It replaces letters with random symbols or numbers, then adds 4 random letters or numbers.
- **Random:** It completely generates a random password.

## Security note
If someone knows my name, the easiest mode to guess is Classic because it's simple and it uses your name.
The safest mode is random because it's completely random.

## What I learned
- The hardest part was the `render_template` code—like how `name=name` or `password=password` works.
- I solved it by understanding that the HTML name or password is different from the Python password or name variables.
- One thing I will remember is how I can merge Python and HTML together.
