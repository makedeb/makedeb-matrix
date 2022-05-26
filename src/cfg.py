import os

from commands.faq import faq
from commands.search import search
from commands.list import list
from commands.help import help

config_file = os.environ.get("CONFIG_FILE", "./config.yaml")

cmd_definitions = {
    "faq": (faq, "Show frequently asked questions"),
    "list": (list, "Show information for a package on the MPR"),
    "search": (search, "Search for a package on the MPR"),
    "help": (help, "Bring up this help menu")
}

mpr_url = "mpr.makedeb.org"

# The following are modified during runtime.
mpr_package_json = []
