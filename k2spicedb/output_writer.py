def write_schema_to_file(schema, file_path):
    """
    Writes the generated schema to a .zed file.

    Args:
        schema (str): The generated SpiceDB schema.
        file_path (str): Path to the output .zed file.
    """
    with open(file_path, 'w') as file:
        file.write(schema)
