import os
import logging
from typing import Any, Dict, List, Optional


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Set up and return a logger with the specified name and level."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(name)s: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Get an environment variable or return default."""
    value = os.getenv(key, default)
    if value is None:
        raise EnvironmentError(
            f"Environment variable '{key}' not set and no default provided."
        )
    return value


def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks of specified size."""
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """Flatten a nested list into a single list."""
    return [item for sublist in nested_list for item in sublist]


def safe_get(d: Dict, keys: List[Any], default: Any = None) -> Any:
    """Safely get a nested value from a dict."""
    for key in keys:
        if isinstance(d, dict) and key in d:
            d = d[key]
        else:
            return default
    return d
