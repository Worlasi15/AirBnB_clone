import unittest
from io import StringIO
import sys
from unittest.mock import main


class TestMainFunction(unittest.TestCase):
    def test_main_output(self):
        expected_output =
    "Partners for this project are Faith Akadi and Rebecca Frempong\n"
    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    sys.stdout = sys.__stdout__
    self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
