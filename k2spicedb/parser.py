import json

def read_keycloak_export(file_path):
    """
    Reads and parses the Keycloak export JSON file.

    Args:
        file_path (str): Path to the Keycloak export JSON file.

    Returns:
        dict: Structured representation of the Keycloak data.
    """
    with open(file_path, 'r') as file:
        keycloak_data = json.load(file)
    return keycloak_data
