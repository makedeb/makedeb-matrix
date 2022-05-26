import cfg

async def send_bot_markdown_message(*args, **kwargs):
    await cfg.bot.api.send_markdown_message(*args, **kwargs, msgtype="m.notice")

async def send_bot_text_message(*args, **kwargs):
    await cfg.bot.api.send_text_message(*args, **kwargs, msgtype="m.notice")
