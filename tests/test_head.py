import unittest
from head import head_command

class TestHead(unittest.TestCase):

    def test_should_return_first_ten_rows_by_default(self):
        expected_rows = [
            "S.P.I.R.I.T.\n",
            "Spirit, let's hear it\n",
            "S.P.I.R.I.T.\n",
            "Spirit, let's hear it\n",
            "Let's go!\n",
            "\n",
            "I've had enough\n",
            "There's a voice in my head\n",
            "Says I'm better off dead\n",
            "\n"
        ]
        args_list = ["head.py", "happy-song.txt"]

        self.assertEqual(head_command(args_list), expected_rows)

    def test_should_return_first_five_rows_using_n_flag(self):
        expected_rows = [
            "S.P.I.R.I.T.\n",
            "Spirit, let's hear it\n",
            "S.P.I.R.I.T.\n",
            "Spirit, let's hear it\n",
            "Let's go!\n",
        ]
        args_list = ["head.py", "happy-song.txt", "-n", "5"]

        self.assertEqual(head_command(args_list), expected_rows)

    def test_should_return_file_does_not_exists_if_file_name_is_incorrect(self):
        expected_msg = "File does not exists\n"
        args_list = ["head.py", "sad-song.py"]

        self.assertEqual(head_command(args_list), expected_msg)
