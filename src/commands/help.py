import cfg
import util

async def help():
    msg  = "List of available commands:\n"
    
    for cmd in cfg.cmd_definitions:
        cmd_description = cfg.cmd_definitions[cmd][1]
        msg += f"- `{cmd}`: {cmd_description}\n"

    await util.send_bot_markdown_message(cfg.room_id, msg)
