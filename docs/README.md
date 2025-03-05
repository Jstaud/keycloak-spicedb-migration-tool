# Keycloak to SpiceDB Migration Tool

## Overview
The Keycloak to SpiceDB Migration Tool is an open-source CLI tool that automates the migration of Keycloak realms to SpiceDB schemas.

## Features
- Parses Keycloak realm export JSON files
- Transforms Keycloak data to SpiceDB schema
- Handles user interaction for missing information
- Generates SpiceDB schema output
- Writes generated schema files to disk

## Installation
To install the tool, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Jstaud/k2spicedb.git
cd k2spicedb
pip install -r requirements.txt
```

## Usage
To use the CLI tool, run the following command:

```bash
python -m k2spicedb.cli --realm-export <path_to_keycloak_export> --out <path_to_output_schema> [-v]
```

### Example
```bash
python -m k2spicedb.cli --realm-export examples/example_keycloak_export.json --out examples/example_spicedb_schema.zed -v
```

## Contributing
We welcome contributions to the project. Please see the [CONTRIBUTING.md](../CONTRIBUTING.md) file for guidelines on how to contribute.

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
