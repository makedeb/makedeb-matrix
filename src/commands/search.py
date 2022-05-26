import cfg
import util

async def search():
    await util.fetch_mpr_archive()

    try:
        pkg_search = cfg.args[1]
    except IndexError:
        pkg_search = None

    if pkg_search is None:
        msg = f"Please specify a search query."
        await util.send_bot_markdown_message(cfg.room_id, msg)
        return
    
    # Search packages.
    matching_packages = []

    for pkg in cfg.mpr_package_json:
        if pkg_search in pkg["Name"]:
            matching_packages += [pkg]

        elif pkg["Description"] is not None and pkg_search in pkg["Description"].lower():
            matching_packages += [pkg]
        
        # Only process the first 10 results.
        if len(matching_packages) == 10:
            break

    # Return results.
    if len(matching_packages) == 0:
        await util.send_bot_text_message(cfg.room_id, "No results found.")
        return

    elif len(matching_packages) == 1:
        results_str = "Found 1 package:\n"
    else:
        results_str = "Found %s packages:\n" % len(matching_packages)

    for pkg in matching_packages:
        pkgname = pkg["Name"]
        pkgver = pkg["Version"]
        pkgdesc = pkg["Description"]

        results_str += f"\n- [**{pkgname}**/{pkgver}](https://{cfg.mpr_url}/packages/{pkgname})\n"

        if pkgdesc is not None:
            results_str += f"{pkgdesc}\n"

    await util.send_bot_markdown_message(cfg.room_id, results_str)
