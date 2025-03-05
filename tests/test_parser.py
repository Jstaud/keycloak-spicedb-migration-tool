import unittest
from kc2spicedb.parser import read_keycloak_export

class TestKeycloakExportParser(unittest.TestCase):

    def test_read_keycloak_export(self):
        # Test the function to read and parse the JSON file
        file_path = 'examples/example_keycloak_export.json'
        keycloak_data = read_keycloak_export(file_path)
        
        # Ensure the structured representation of the Keycloak data is correct
        self.assertIsInstance(keycloak_data, dict)
        self.assertIn('realm', keycloak_data)
        self.assertIn('users', keycloak_data)
        self.assertIn('roles', keycloak_data)

if __name__ == '__main__':
    unittest.main()
