# GPS Graph
*Noé LORRET-DESPRET*<br>
*Laure WARLOP*<br>
*CIR3*<br>


## What is it ?
This is a small python GPS, using a combination of graphs and external dependancies,
we can find for you the shortest way to your destination<br>
**You will need an iPhone, sorry, no way around it**


## Installation

### Virtual Env
```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python main.py
```

### NixOS
```bash
nix develop
python3 main.py
```

## Usage

### Running
The first run will be slow, since there are a lot of cache files to be built<br>
To check command line arguments, try `python3 main.py --help` !<br>


### Credentials
To retrieve your location, we use the iCloud API, so we need you to store your Apple crendentials somewhere<br>
You can use environnement variables or provide a .env file with `--env FILE`
```sh
ICLOUD_EMAIL='email@website.com'
ICLOUD_PWD='secret_password'
```

