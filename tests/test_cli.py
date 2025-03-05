import unittest
import subprocess
import os

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.realm_export_path = "examples/example_keycloak_export.json"
        self.output_path = "examples/example_spicedb_schema.zed"

    def test_cli_entry_point(self):
        result = subprocess.run(
            ["python3", "kc2spicedb/cli.py", "--realm-export", self.realm_export_path, "--out", self.output_path],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(self.output_path))

    def test_cli_verbose_logging(self):
        result = subprocess.run(
            ["python3", "kc2spicedb/cli.py", "--realm-export", self.realm_export_path, "--out", self.output_path, "-v"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("DEBUG", result.stdout)

if __name__ == "__main__":
    unittest.main()
