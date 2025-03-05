import argparse
from kc2spicedb.parser import parse_keycloak_export
from kc2spicedb.transformer import transform_keycloak_to_spicedb
from kc2spicedb.prompt_handler import handle_missing_info
from kc2spicedb.schema_generator import generate_spicedb_schema
from kc2spicedb.output_writer import write_schema_to_file
from kc2spicedb.logging_config import configure_logging

def main():
    configure_logging()
    
    parser = argparse.ArgumentParser(description="Keycloak to SpiceDB Migration Tool")
    parser.add_argument("--realm-export", required=True, help="Path to the Keycloak realm export JSON file")
    parser.add_argument("--out", required=True, help="Path to the output SpiceDB schema file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    
    args = parser.parse_args()
    
    if args.verbose:
        import logging
        logging.getLogger().setLevel(logging.DEBUG)
    
    keycloak_data = parse_keycloak_export(args.realm_export)
    transformed_data = transform_keycloak_to_spicedb(keycloak_data)
    user_provided_data = handle_missing_info(transformed_data)
    spicedb_schema = generate_spicedb_schema(user_provided_data)
    write_schema_to_file(spicedb_schema, args.out)

if __name__ == "__main__":
    main()
