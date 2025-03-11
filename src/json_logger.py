import json
import logging

def log_json(json_obj, log_level='info', logger=None):
    """
    Log a JSON object with proper formatting and optional log level.

    Args:
        json_obj (dict): The JSON object to be logged
        log_level (str, optional): Logging level. Defaults to 'info'. 
                                   Supports 'debug', 'info', 'warning', 'error', 'critical'
        logger (logging.Logger, optional): Custom logger. If None, uses root logger.

    Returns:
        str: Formatted JSON string that was logged

    Raises:
        TypeError: If json_obj is not a dictionary
        ValueError: If an invalid log level is provided
    """
    # Validate input
    if not isinstance(json_obj, dict):
        raise TypeError("Input must be a dictionary")

    # Validate log level
    log_levels = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }

    if log_level.lower() not in log_levels:
        raise ValueError(f"Invalid log level. Must be one of: {', '.join(log_levels.keys())}")

    # Use default logger if none provided
    if logger is None:
        logger = logging

    # Format JSON with indentation
    formatted_json = json.dumps(json_obj, indent=2)

    # Log the formatted JSON
    log_levels[log_level.lower()](formatted_json)

    return formatted_json