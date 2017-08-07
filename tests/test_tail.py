import unittest
from tail import tail_command

class TestTail(unittest.TestCase):

    def test_should_return_last_ten_rows_by_default(self):
        expected_rows = [
            "Let's sing along\n",
            "A little fucking louder\n",
            "A little fucking louder\n",
            "Well, don't you feel so much better?\n",
            "\n",
            "S.P.I.R.I.T.\n",
            "Spirit, let's hear it (well, that's the spirit)\n",
            "\n",
            "S.P.I.R.I.T.\n",
            "Spirit, let's hear it (yeah, that's the spirit)\n"
        ]
        args_list = ["tail.py", "happy-song.txt"]

        self.assertEqual(tail_command(args_list), expected_rows)

    def test_should_return_five_last_rows_using_n_flag(self):
        expected_rows = [
            "S.P.I.R.I.T.\n",
            "Spirit, let's hear it (well, that's the spirit)\n",
            "\n",
            "S.P.I.R.I.T.\n",
            "Spirit, let's hear it (yeah, that's the spirit)\n"
        ]
        args_list = ["tail.py", "happy-song.txt", "-n", "5"]

        self.assertEqual(tail_command(args_list), expected_rows)

    def test_should_return_file_does_not_exists_if_file_name_is_incorrect(self):
        expected_msg = "File does not exists\n"
        args_list = ["tail.py", "sad-song.py"]

        self.assertEqual(tail_command(args_list), expected_msg)

    def test_should_return_all_rows_reversed_if_flag_r_is_used(self):
        expected_rows = [
            "I'm going round in circles\n",
            "And I'm going round in circles\n",
            "But my head is like a carousel\n",
            "And I really wish that you could help\n",
            "'Cause the nightmares in our heads are bad enough\n",
            "Don't wake us up, we'd rather just keep dreaming\n"
        ]
        args_list = args_list = ["tail.py", "happy-song-short.txt", "-r"]

        self.assertEqual(tail_command(args_list), expected_rows)

    def test_should_return_cannot_combine_n_with_r(self):
        expected_msg = "Cannot combine -n with -r\n"
        args_list = ["tail.py", "-r", "-n", "5", "happy-song.txt"]

        self.assertEqual(tail_command(args_list), expected_msg)
