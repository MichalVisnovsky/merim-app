import configparser

from loguru import logger

CFG_PATH = "./config.ini"
_config_cache = None

def get_config() -> dict:

    # Use cached config if available
    global _config_cache
    if _config_cache is not None:
        return _config_cache

    config = configparser.ConfigParser()
    ret = dict()
    logger.debug(f"Loading config from {CFG_PATH}")
    if not config.read(CFG_PATH):
        logger.error("Config file not found")
        return ret

    for section in config.values():
        if section.name not in ["DEFAULT"]:
            continue

        for key, value in section.items():
            try:
                value = int(value)
                ret.update({key: value})
            except ValueError:
                ret.update({key: value})

    logger.debug(f"Config loaded")

    # Cache the config
    _config_cache = ret
    return ret