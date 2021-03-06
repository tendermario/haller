# Nanoleaf Aurora Controller
Customize interactions. Make cool effects and visualizations for your Nanoleaf Aurora.

## What is it?
This is a fork of https://github.com/bharat/haller, which is a wrapper around https://github.com/bharat/nanoleaf that provides some additional, higher level functionality to control your Nanoleaf Aurora.

## What can it do?
1. Automatically find and connect to your Aurora
1. Turn on/off your Aurora from a script
1. Handle rotation of your Aurora (so that you can script "left to right" type effects)
1. Real-time display effects (including some samples)
1. Audio visualization effects (including some samples)

### Prerequisites
1. Python3
1. This directory cloned
1. The nanoleaf directory cloned into that directory

```
git clone git@github.com:tendermario/haller.git
cd haller
git clone git@github.com:bharat/nanoleaf.git
```

## First time setup

Option 1: venv

1. `./install.sh`

Option 2: pipenv (I can't do this anymore for some reason)

1. `brew install pipenv`
1. `cd haller` (or whatever you name the dir)
1. `pipenv shell`
1. `pipenv run pip install pip==18.0` (maybe)
1. `pipenv install`


## Quick start

1. Hit the pairing button on your Aurora
1. run `config.py`. It will discover your Aurora, pair with it and create a file called `aurora.ini` containing config data.

This will persist until you reset your Nanoleaf. You can have your phone and computer connected to the panels at the same time.

## Coming back

Just turn on your panels and it should be good to go.

## Test commands

`./display.py --streaming flash --speed 0.1`
`./display.py --streaming flash --speed 1`
`./display.py --streaming flash --speed 0.3`
(seizure warning): `./display.py --streaming flash --speed 0.1`
(seizure warning): `./display.py --streaming flash --speed 0.01`

## Notes on controls

- Hard reset: Press and hold power + arrow for 10 seconds until flashing for hard reset to factory defaults and go into pair mode.
- Pairing: Press and hold power for 5 seconds to go into pairing mode

## Debugging notes:

- I think nanoleaf.nanoleaf.aurora Aurora has its API changed, so methods like panel_prepare doesn't work in display.py --streaming red_epilepsy might want to pull the latest nanoleaf repo.
- Todo: Fix streaming
- Todo: Make streaming accessible from the CLI

## How do I use it?

Run `./main.py` to open the CLI. It will have instructions.

Run `./display.py --streaming <name>` to use streaming mode, which will run against a preset algo defined as: `<name>_streaming` method in the file.

## How do I use it? (original)

NOTE: This is the original maintainer's notes, and a lot of it does not currently work.

### Configure your panel orientation
By default your Aurora will have an arbitrary orientation. You can control that orientation by using the `--rotate` argument to `config.py`. Haller will save that orientation and use it in the future.

1. `config.py --plot` will create an HTML file called `plot.html` that contains a visual representation of your panel layout
1. `config.py --rotate <degrees>` will calculate a new rotation of your panel layout. Use this with `--plot` to visualize to make sure that your panel rotation matches your physical layout. The results of this rotation are cached in `aurora.ini` for the future.

Here's what a sample plot looks like:
![Aurora Plot](screenshots/plot.png "This is a screenshot of my Aurora setup after I've rotated it")

### Effects
1. `effect.py --list` to list all effects
1. `effect.py --set <name>` to choose an effect
1. `effect.py --create` creates a hardcoded effect called `Scripted`. Work in progress here.

#### Effects - A deeper learning

##### For rhythm, add this to the object for now:

```
"animType" : "plugin",
"pluginType": "rhythm",
"pluginUuid":"60333927-cc36-4a5a-a682-9bd114de8bff",
```


### Streaming

This uses the `External Control` feature of Aurora to allow dynamic effects. There are a few hardcoded ones, but the code is an example for what you can do. Try `display.py --streaming wipe` to see one of them.

### Visualization

Using the streaming interface, you can turn your Aurora into a music visualizer. Try `visualizer.py --viz amplitude` for yourself. You can see what it looks like here: https://www.youtube.com/watch?v=nnojsRrwK4c
