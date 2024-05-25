# Fine tuning LLMs for generation of mojo code

## Setting up the environment
- [x]  WSL (Ubuntu 22.04)
- [x] VS Code

Follow the next steps to install Mojo:

1. In the Ubuntu terminal, install the Modular CLI: `curl https://get.modular.com | sh - && \
modular auth xxxxxxxxxxxxxxxxxxxxxxxxxxx`
2. *It was necessary to install python venv: `sudo apt install python3.10-venv`
3. Install the Mojo SDK: `modular install mojo`

After installing Mojo CLI and SDK, define the necessary environment variables in the .bashrc file:

`export MODULAR_HOME="$HOME/.modular"`

`export PATH="$MODULAR_HOME/pkg/packages.modular.com_mojo/bin:$PATH"`

VS Code Extensions:
- WSL
- IntelliCode
- Mojo
- Python