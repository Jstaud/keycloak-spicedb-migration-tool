def generate_spicedb_schema(transformed_data):
    """
    Generates SpiceDB schema from the transformed data.

    Args:
        transformed_data (dict): Transformed SpiceDB schema data.

    Returns:
        str: Generated SpiceDB schema.
    """
    schema = ""

    # Example schema generation logic
    for user in transformed_data.get('users', []):
        schema += f"user {user['username']}\n"

    for role in transformed_data.get('roles', []):
        schema += f"role {role['name']}\n"

    for group in transformed_data.get('groups', []):
        schema += f"group {group['name']}\n"

    return schema
