import logging

def configure_logging():
    """
    Configures logging settings for the project.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
