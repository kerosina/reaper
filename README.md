# Reaper
```
   ██▀███  ▓█████ ▄▄▄       ██▓███  ▓█████  ██▀███
  ▓██ ▒ ██▒▓█   ▀▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
  ▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
  ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄
  ░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
  ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
    ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
    ░░   ░    ░    ░   ▒   ░░          ░     ░░   ░
     ░        ░  ░     ░  ░            ░  ░   ░
```
Discord selfbot in python. Modular, extensible and simple.

## Getting started

You need to have python3 and pip installed, usually by installing python3 and python3-pip with your package manager. On windows, install python3 from the installer on their site and it'll come with pip.

Then, you need to install the dependencies:
```bash
$ pip install -r requirements.txt
```
on some linux distributions like debian or arch, it may complain about possible conflicts with the package manager. If you get that error, append `--break-system-packages` to the command.

After that, copy `config.toml.example` to `config.toml` and modify it however you like.

## Using the selfbot

To see commands and their purpose, use the command `help`.

Some commands, like nuke or spam, require variables to be set. Those are not set on the toml file as they are temporary.

To view them, you can use the command `get` with no arguments, or give it the name of a variable whose value you want to see.

To edit a variable, you use the command `set`. For example, assuming the default prefix, run `*set spamtext Test 123` to set the spam text to "Test 123".

## Issues

If you have issues with the bot, set LogLevel to "debug" on the config.toml and describe your issue along with showing the console output on the [Issues tab](https://github.com/kerosina/reaper/issues).
