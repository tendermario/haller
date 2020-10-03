#!/usr/bin/env python3
import sys
import random
import argparse
import bokeh

import config
from nanoleaf.nanoleaf import Aurora

a = config.aurora()

def effect_scripted():
    palette = [ {
        "hue": random.randint(0, 359),
        "saturation": 100,
        "brightness": random.randint(60, 80)
    } for x in range(1, 10)]

    return {
        "command" : "add",
        "animName" : "Scripted",
        "animType" : "plugin",
        "pluginType": "rhythm",
        "pluginUuid": "60333927-cc36-4a5a-a682-9bd114de8bff",
        "colorType" : "HSB",
        "palette" : palette,
        "transTime" : { "maxValue": 50, "minValue": 50 },
        "delayTime" : { "maxValue": 0,   "minValue": 0 },
        "explodeFactor" : 0.5,
        "direction" : "outwards",
        "loop" : True
    }

def set_to_effect(effect):
    type(effect)
    a.effect = effect

def action_list():
    print('\n'.join(a.effects_list))

def action_set(name):
    if name not in a.effects_list:
        print('%s is an invalid effect\n' % name)
    a.effect = name

# This will save the contents of effect_scripted to a name.
def action_save():
    effect = effect_scripted()
    a.effect_set_raw(effect)

def effect(a, args):
    if args.list:
        action_list()

    elif args.set:
        action_set(args.set)

    elif args.create:
        action_save()


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', action='store_true')
    parser.add_argument('--set', dest='set')
    parser.add_argument('--create', dest='create')
    args = parser.parse_args()

    aurora = config.aurora()
    effect(aurora, args)


if __name__ == '__main__':
    main(sys.argv)
