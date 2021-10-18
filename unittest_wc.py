# python3 -m unittest unittest_wc
import unittest
import subprocess


class TestWC(unittest.TestCase):
    def test_common_files(self):
        self.assertEqual(
            subprocess.check_output('python3 wc.py testinputs/empty_test.txt', shell=True),
            b'\t0\t0\t0\ttestinputs/empty_test.txt\n'
        )

        self.assertEqual(
            subprocess.check_output('python3 wc.py testinputs/emoji.txt', shell=True),
            b'\t2\t3\t11\ttestinputs/emoji.txt\n'
        )

        self.assertEqual(
            subprocess.check_output('python3 wc.py testinputs/html.html', shell=True),
            b'\t10\t12\t124\ttestinputs/html.html\n'
        )

        self.assertEqual(
            subprocess.check_output('python3 wc.py testinputs/pyscript.py', shell=True),
            b'\t1\t1\t14\ttestinputs/pyscript.py\n'
        )

    def test_binary_files(self):
        self.assertEqual(
            subprocess.check_output('python3 wc.py testinputs/pdf.pdf', shell=True),
            b'\t130\t596\t7985\ttestinputs/pdf.pdf\n'
        )

    def test_flag_combination(self):
        self.assertEqual(
            subprocess.check_output('python3 wc.py -l -w testinputs/emoji.txt', shell=True),
            b'\t2\t3\ttestinputs/emoji.txt\n'
        )

        self.assertEqual(
            subprocess.check_output('python3 wc.py -w -l testinputs/emoji.txt', shell=True),
            b'\t2\t3\ttestinputs/emoji.txt\n'
        )

        self.assertEqual(
            subprocess.check_output('python3 wc.py -c testinputs/emoji.txt', shell=True),
            b'\t11\ttestinputs/emoji.txt\n'
        )

    def test_illegal_flags(self):
        self.assertEqual(
            subprocess.check_output('python3 wc.py -t testinputs/emoji.txt', shell=True),
            b'wc: illegal option --t\n\nusage: wc [-clw] [file ...]\n\n'
        )

        self.assertEqual(
            subprocess.check_output('python3 wc.py -tyt testinputs/emoji.txt', shell=True),
            b'wc: illegal option --tyt\n\nusage: wc [-clw] [file ...]\n\n'
        )

        self.assertEqual(
            subprocess.check_output('python3 wc.py -m testinputs/emoji.txt', shell=True),
            b'We don\xe2\x80\x99t handle that situation yet!\n'
        )

    def test_multiple_paths(self):
        self.assertEqual(
            subprocess.check_output('python3 wc.py testinputs/emoji.txt testinputs/html.html', shell=True),
            b'\t2\t3\t11\ttestinputs/emoji.txt\n'
            b'\t10\t12\t124\ttestinputs/html.html\n'
            b'\t12\t15\t135\ttotal\n'
        )

        self.assertEqual(
            subprocess.check_output('python3 wc.py testinputs/emoji.txt testinputs/html.htm', shell=True),
            b'\t2\t3\t11\ttestinputs/emoji.txt\n'
            b'wc: testinputs/html.htm: open: No such file or directory\n'
            b'\t2\t3\t11\ttotal\n'
        )

    def test_empty_inputs(self):
        self.assertEqual(
            subprocess.check_output('python3 wc.py', shell=True),
            b'We don\xe2\x80\x99t handle that situation yet!\n'
        )

    def test_slash_inputs(self):
        self.assertEqual(
            subprocess.check_output('python3 wc.py -', shell=True),
            b'wc: -: open: No such file or directory\n'
        )

        self.assertEqual(
            subprocess.check_output('python3 wc.py -- -f', shell=True),
            b'wc: -f: open: No such file or directory\n'
        )

        self.assertEqual(
            subprocess.check_output('python3 wc.py - -r -c testinputs/text.txt', shell=True),
            b'wc: illegal option --r\n\nusage: wc [-clw] [file ...]\n\n'
        )


if __name__ == '__main__':
    unittest.main()
