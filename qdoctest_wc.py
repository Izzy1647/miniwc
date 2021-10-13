'''
>>> import subprocess
>>> subprocess.check_output('python3 wc.py qtestinputs/test1.txt', shell=True)
b'\\t10\\t10\\t20\\tqtestinputs/test1.txt\\n'
>>> subprocess.check_output('python3 wc.py qtestinputs/test2.txt', shell=True)
b'\\t1\\t91\\t575\\tqtestinputs/test2.txt\\n'
>>> subprocess.check_output('python3 wc.py qtestinputs/test3.txt', shell=True)
b'\\t1\\t14\\t79\\tqtestinputs/test3.txt\\n'
>>> subprocess.check_output('python3 wc.py qtestinputs/test4.txt', shell=True)
b'\\t0\\t0\\t0\\tqtestinputs/test4.txt\\n'
>>> subprocess.check_output('python3 wc.py qtestinputs/unicode.txt', shell=True)
b'\\t15\\t101\\t971\\tqtestinputs/unicode.txt\\n'

'''