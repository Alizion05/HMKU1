import os
import unittest
from emulator import ShellEmulator


class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        # Initialize the emulator with a valid config file
        self.emulator = ShellEmulator("config.xml")
        self.emulator.current_path = "/"

    def tearDown(self):
        # Clean up after each test
        self.emulator.cleanup()

    def test_ls(self):
        # Example test case for the 'ls' command
        self.emulator.execute_command("ls")
        # You can check for expected directory contents in the output if needed
        # For example, use mock or check the standard output stream.

    def test_cd(self):
        # Test case for 'cd' command
        self.emulator.execute_command("cd /")
        self.assertEqual(self.emulator.current_path, "/")

    def test_chmod(self):
        # Correct the test to use vfs_path_extracted
        test_file = os.path.join(self.emulator.vfs_path_extracted, "testfile")
        with open(test_file, "w") as f:
            f.write("test")
        self.emulator.execute_command(f"chmod 666 {test_file}")
        self.assertEqual(oct(os.stat(test_file).st_mode)[-3:], "666")

    def test_tac(self):
        # Correct the test to use vfs_path_extracted
        test_file = os.path.join(self.emulator.vfs_path_extracted, "testfile")
        with open(test_file, "w") as f:
            f.write("line1\nline2\nline3\n")
        self.emulator.execute_command(f"tac {test_file}")
        # Add checks to verify the order of output or check the terminal output.

    def test_uname(self):
        # Test the 'uname' command
        self.emulator.execute_command("uname")
        # Check the system output for correctness. If needed, you can mock the output of platform.system().
