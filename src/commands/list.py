import cfg
import util

from datetime import datetime

async def list():
    await util.fetch_mpr_archive()

    try:
        pkgname = cfg.args[1]
    except IndexError:
        await util.send_bot_markdown_message(cfg.room_id, "Please specify a package.")
        return
    
    # Search packages.
    matching_packages = []

    for pkg in cfg.mpr_package_json:
        if pkgname == pkg["Name"]:
            pkgver = pkg["Version"]
            maintainer = pkg["Maintainer"]
            pkgdesc = pkg["Description"]
            url = pkg["URL"]
            votes = pkg["NumVotes"]
            popularity = pkg["Popularity"]
            ood = pkg["OutOfDate"]

            msg = f"[**{pkgname}**/{pkgver}](https://{cfg.mpr_url}/packages/{pkgname})\n"
            msg += f"**Maintainer:** {maintainer}\n"
            msg += f"**Description:** {pkgdesc}\n"

            if url is not None:
                msg += f"**Homepage:** {url}\n"

            msg += f"**Votes:** {votes}\n"
            msg += f"**Popularity:** {popularity}\n"

            if ood is None:
                ood_str = "N/A"
            else:
                ood_str = datetime.utcfromtimestamp(ood).strftime("%Y-%m-%d")

            msg += f"**Out of Date:** {ood_str}\n"

            await util.send_bot_markdown_message(cfg.room_id, msg)
            return
    
    await util.send_bot_markdown_message(cfg.room_id, "Couldn't find the specified package.")
