import os

from commands.faq import faq
from commands.help import help

config_file = os.environ.get("CONFIG_FILE", "./config.yaml")

cmd_definitions = {
    "faq": (faq, "Show frequently asked questions"),
    "help": (help, "Bring up this help menu")
}    
