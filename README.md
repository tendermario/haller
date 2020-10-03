# Haller
Easy and cool effects and visualizations for your Nanoleaf Aurora.

## What is it?
Haller is a wrapper around https://github.com/bharat/nanoleaf that provides some additional, higher level functionality to control your Nanoleaf Aurora

## What can it do?
1. Automatically find and connect to your Aurora
1. Turn on/off your Aurora from a script
1. Handle rotation of your Aurora (so that you can script "left to right" type effects)
1. Real-time display effects (including some samples)
1. Audio visualization effects (including some samples)

### Requirements
1. Python3
1. Python modules: bokeh, pyaudio, numpy, scipy, (maybe some other python dev tools?)

## First time setup

1. `brew install pipenv`
1. `cd haller` (or whatever you name the dir)
1. `pipenv shell`
1. `pipenv run pip install pip==18.0` (maybe)
1. `pipenv install`
1. `git clone git@github.com:bharat/nanoleaf.git` inside the haller directory


## Quick start

1. Hit the pairing button on your Aurora
1. run `config.py`. It will discover your Aurora, pair with it and create a file called `aurora.ini` containing config data.

## Notes on controls

- Press and hold power + arrow for 10 seconds until flashing for hard reset to factory defaults and go into pair mode.
- Press and hold power for 5 seconds to go into pairing mode

## How do I use it?

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
