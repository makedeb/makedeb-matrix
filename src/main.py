#!/usr/bin/env python3
import cfg
import logging
import traceback
import util

import simplematrixbotlib as botlib

from read_config import read_config

def main():
    # Setup.
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    read_config()

    cfg.prefix = cfg.config["config"]["prefix"]

    # Log in.
    creds = botlib.Creds(homeserver=cfg.config["auth"]["homeserver"], username=cfg.config["auth"]["username"], access_token=cfg.config["auth"]["access_token"])
    cfg.bot = botlib.Bot(creds)

    @cfg.bot.listener.on_message_event
    async def entrypoint(room, message):
        match = botlib.MessageMatch(room, message, cfg.bot, cfg.config["config"]["prefix"])

        if (not match.is_not_from_this_bot()) or (not match.prefix()):
            return

        # Set up argument lists for commands.
        cfg.args = match.args()

        try:
            cfg.cmd = cfg.args[0]
        except IndexError:
            cfg.cmd = None
        
        # Check if specified command is valid.
        if cfg.cmd not in cfg.cmd_definitions:
            prefix = cfg.config["config"]["prefix"]
            
            if cfg.cmd is None:
                msg = "Please specify a command.\n"
            else:
                msg = f"Unknown command `{cfg.cmd}`.\n"
            msg += f"Type `{prefix} help` for a list of available commands."

            await util.send_bot_markdown_message(room.room_id, msg)
            return

        # Set up environment for commands, and run the command.
        cfg.room = room
        cfg.room_id = room.room_id

        try:
            await cfg.cmd_definitions[cfg.cmd][0]()
        except Exception:
            await util.send_bot_markdown_message(room.room_id, f"There was an error processing your request. Please try again, or report an issue with `{cfg.prefix} faq license`.")
            logging.error(
                traceback.format_exc()
            )

    cfg.bot.run()

if __name__ == "__main__":
    main()
