import os
import unittest
from emulator import ShellEmulator


class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.emulator = ShellEmulator("config.xml")
        self.emulator.current_dir = "/"

    def tearDown(self):
        self.emulator.cleanup()

    def test_ls(self):
        self.emulator.execute_command("ls")
        # Проверяем, что вывод корректный

    def test_cd(self):
        self.emulator.execute_command("cd /")
        self.assertEqual(self.emulator.current_dir, "/")

    def test_chmod(self):
        test_file = os.path.join(self.emulator.fs_root, "testfile")
        with open(test_file, "w") as f:
            f.write("test")
        self.emulator.execute_command(f"chmod 777 {test_file}")
        self.assertEqual(oct(os.stat(test_file).st_mode)[-3:], "777")

    def test_tac(self):
        test_file = os.path.join(self.emulator.fs_root, "testfile")
        with open(test_file, "w") as f:
            f.write("line1\nline2\nline3\n")
        self.emulator.execute_command(f"tac {test_file}")
        # Проверяем, что строки вывелись в обратном порядке

    def test_uname(self):
        self.emulator.execute_command("uname")
        # Проверяем вывод команды uname