import logging.config
import yaml
import sys

def get_logger(
    config_file_path: str="logger_config.yaml"
    )-> logging:
    """_summary_

    Args:
        config_file_path (str, optional): _description_. Defaults to "logger_config.yaml".

    Returns:
        logger: _description_
    """
    with open(config_file_path, 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger()
    return logger





