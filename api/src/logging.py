from loguru import logger

# General setup for logging

# Logging format
log_format = (
    "{time:DD-MM-YYYY HH:mm:ss zz} | "
    "{level: <6} | "
    "{message}"
)

# General logging
logger.add("./log/api_debug.log", rotation="100 MB",
           format=log_format, level="DEBUG")

# Separated info log file
logger.add("./log/api_info.log", rotation="100 MB",
           format=log_format, level="INFO", filter=lambda record: record["level"].name == "INFO")

# Separated error log file
logger.add("./log/api_error.log", rotation="100 MB",
           format=log_format, level="ERROR", filter=lambda record: record["level"].name == "ERROR")
