import unittest
from k2spicedb.transformer import transform_keycloak_to_spicedb

class TestTransformer(unittest.TestCase):

    def test_transform_keycloak_to_spicedb(self):
        # Test the function to map Keycloak concepts to SpiceDB constructs
        keycloak_data = {
            'users': [{'username': 'user1'}, {'username': 'user2'}],
            'roles': [{'name': 'role1'}, {'name': 'role2'}],
            'groups': [{'name': 'group1'}, {'name': 'group2'}]
        }
        transformed_data = transform_keycloak_to_spicedb(keycloak_data)
        
        # Ensure the transformed data is correct
        self.assertIn('users', transformed_data)
        self.assertIn('roles', transformed_data)
        self.assertIn('groups', transformed_data)
        self.assertEqual(len(transformed_data['users']), 2)
        self.assertEqual(len(transformed_data['roles']), 2)
        self.assertEqual(len(transformed_data['groups']), 2)

if __name__ == '__main__':
    unittest.main()
