# Exordium

Exordium is a custom VSCode-style logger for Python, providing colorful and informative log messages.

## Installation

You can install Exordium using pip:

```
pip install exordium
```

Or directly from the GitHub repository:

```
pip install git+https://github.com/yourusername/exordium.git
```

## Usage

Here's a simple example of how to use Exordium:

```python
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
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
