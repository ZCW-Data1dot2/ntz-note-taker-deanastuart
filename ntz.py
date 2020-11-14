#!/Users/deana/documents/projects/ntz-note-taker-deanastuart/env python3

import os
import yaml
import sys


def cli():
  cmd = get_args()
  notes = _yaml_r()
  if len(cmd) == 2:
    show_notes()
  elif cmd[2] == 'r':
      remember(cmd[4], cmd[3])
  elif cmd[2] == 'cl':
    clear()
  # if cmd(1) == 'e':
  #     edit(cmd, notes)

def show_notes():

  notes = _yaml_r()

  if bool(notes) is False:
    print("You don't have any saved notes")
  else:
    print(notes)


def remember(note, category=None):
  data = _yaml_r() or {}

  if category is None:
    category = 'To Do'

  try:
    if note not in data[category]:
      data[category].append(note)
      _yaml_w(data)
    else:
      print("You've already made this note.")


  except KeyError:
    data[category] = [note]
    _yaml_w(data)

  show_notes()

# def edit(category,index,note):
#   notes = _yaml_r()
#   try:
#     notes[category][index-1] = note
#   except KeyError:
#     print("There is no note")
#
#     return
#   _yaml_w(notes)

def clear():
  print("Current notes:")
  show_notes()
  answer = input("Are you sure you want to clear? Y/N: ")
  if answer == 'Y' or 'y':
    _yaml_w({})
    print("Notes Deleted")
  else:
    print("Did not delete note")
    return

def _yaml_r():
  try:
    with open('/Users/deana/documents/projects/ntz-note-taker-deanastuart/notes.yaml') as file:
      data = yaml.load(file, Loader=yaml.FullLoader)
      return data
  except FileNotFoundError:
    with open('/Users/deana/documents/projects/ntz-note-taker-deanastuart/notes.yaml') as file:
      return {}


def _yaml_w(notes):
  with open('/Users/deana/documents/projects/ntz-note-taker-deanastuart/notes.yaml', 'w') as file:
    yaml.dump(notes, file)


def get_args():
  return sys.argv


# run the main function
if __name__ == '__main__':
  cli()


