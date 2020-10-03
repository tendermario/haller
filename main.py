#! /usr/bin/env python
from effect import set_to_effect, action_list

class Main:
  file_path = './setlist'
  current_effect = 0

  def __init__(self):
    with open(self.file_path) as set_file:
      self.effect_list = set_file.readlines()

  def set_next_effect(self):
    next_effect = self.effect_list[self.current_effect].replace('\n', '')
    print('Setting to %s' % next_effect)

    set_to_effect(next_effect)

    self.current_effect += 1

    if self.current_effect > len(self.effect_list) - 1:
      self.current_effect = 0


def main():
  main_boi = Main()
  print("Welcome to Nanoleaf CLI. Please enter a command.")
  print("type 'list' to see all effects registered.")
  print("type 'n' to play next effect from 'setlist' file.")
  print("type 'q' to exit.")

  while True:
    command = input('> ')

    if command.lower() == 'n':
      main_boi.set_next_effect()
    elif command.lower() == 'q' or command.lower() == 'quit' or command.lower() == 'exit':
      exit()
    elif command.lower() == 'list':
      action_list()
    else:
      print('Setting to %s' % command)
      set_to_effect(command)

if __name__ == '__main__':
    main()