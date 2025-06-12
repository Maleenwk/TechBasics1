import pyjokes
import cowsay
import termcolor

from termcolor import colored


# get a joke from pyjokes
joke = pyjokes.get_joke()

# colored ascii, using cowsay's underlying API to print the colored version
trex_text = cowsay.get_output_string("trex", joke)

# colored ascii with joke
print(colored(trex_text, "blue"))


