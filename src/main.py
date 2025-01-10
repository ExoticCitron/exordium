from exordium import get_logger

# Create a logger
logger = get_logger(__name__)

# Log to terminal only (default behavior)
logger.info("This will only be printed to the terminal")

# Configure file logging
logger.configure_file_logging("my_log_file.log")

# Now logs will be written to both terminal and file
logger.info("This will be printed to the terminal and written to the file")
logger.debug("Debug message")
logger.warning("Warning message")

# Close file logging when you're done
logger.close_file_logging()

# This will only be printed to the terminal again
logger.info("Back to terminal-only logging")