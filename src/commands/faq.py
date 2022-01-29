import cfg

async def faq():
    # Get needed info.
    try:
        requested_faq = cfg.args[1]
    except IndexError:
        requested_faq = None

    faqs = cfg.config["commands"]["faq"]["messages"]
    
    if requested_faq is None:
        msg = f"Please specify an FAQ to view.\nA list of FAQs can be found with `{cfg.prefix} faq list`."
        await cfg.bot.api.send_markdown_message(cfg.room_id, msg)

    elif requested_faq == "list":
        msg = "Available FAQs:\n"
        
        for faq in faqs:
            description = faqs[faq]["description"]
            msg += f"- `{faq}`: {description}\n"

        await cfg.bot.api.send_markdown_message(cfg.room_id, msg)

    elif requested_faq in faqs:
        msg = faqs[requested_faq]["value"]
        await cfg.bot.api.send_markdown_message(cfg.room_id, msg)

    else:
        msg = f"Unknown FAQ `{requested_faq}`.\nType `{cfg.prefix} faq list` to view the list of FAQs."
        await cfg.bot.api.send_markdown_message(cfg.room_id, msg)

    return
