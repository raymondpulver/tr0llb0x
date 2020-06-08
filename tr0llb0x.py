#!/usr/bin/env python
from prompt_toolkit.styles import style_from_pygments_cls
from pygments.styles.tango import TangoStyle
from prompt_toolkit.shortcuts import clear
from prompt_toolkit import prompt
from prompt_toolkit.keys import Keys
from prompt_toolkit.key_binding.key_bindings import KeyBindings

kb = KeyBindings()
@kb.add(Keys.ControlC)
def handler(event):
  clear()

style = style_from_pygments_cls(TangoStyle)

if __name__ == '__main__':
  while True:
    prompt('tr0llb0x>>> ', key_bindings=kb)


