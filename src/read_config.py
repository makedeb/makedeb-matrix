import cfg
import logging
import jsonschema

from jsonschema import validate
from yaml import load, Loader
from yaml.scanner import ScannerError

# Our config schema.
config_schema = {
    "type": "object",
    "required": ["auth"],
    "properties": {
        "auth": {
            "type": "object",
            "required": ["homeserver", "username", "access_token"],
            "properties": {
                "homeserver": {
                    "type": "string"
                },
                "username": {
                    "type": "string"
                },
                "access_token": {
                    "type": "string"
                }
            }
        },

        "config": {
            "type": "object",
            "required": ["prefix"],
            "properties": {
                "prefix": {
                    "type": "string"
                }
            }
        },

        "commands": {
            "type": "object",
            "required": ["faq"],
            "properties": {
                "faq": {
                    "type": "object",
                    "required": ["messages"],
                    "properties": {
                        "messages": {
                            "type": "object",
                            "patternProperties": {
                                ".*": {
                                    "type": "object",
                                    "required": ["description", "value"],
                                    "properties": {
                                        "description":  {
                                            "type": "string",
                                        },
                                        "value": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

def read_config():
    try:
        with open(cfg.config_file, "r") as file:
            data = file.read()
    except FileNotFoundError:
        logging.error(f"Unable to find config file at '{cfg.config_file}'.")
        exit(1)

    try:
        cfg.config = load(data, Loader=Loader)
    except ScannerError as exc:
        logging.error(f"Error parsing config file at '{cfg.config_file}'.")
        logging.error(exc)
        exit(1)

    try:
        validate(instance=cfg.config, schema=config_schema)
    except jsonschema.exceptions.ValidationError as exc:
        logging.error(f"Error validating config file at '{cfg.config_file}'.")
        logging.error(exc)
        exit(1)
