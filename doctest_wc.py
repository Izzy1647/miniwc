'''
>>> # empty file
>>> import subprocess
>>> subprocess.check_output('python3 wc.py testinputs/empty_test.txt', shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty_test.txt\\n'

>>> # file with emoji
>>> import subprocess
>>> subprocess.check_output('python3 wc.py testinputs/emoji.txt', shell=True)
b'\\t2\\t3\\t11\\ttestinputs/emoji.txt\\n'

>>> # flags combination: -l -w
>>> import subprocess
>>> subprocess.check_output('python3 wc.py -l -w testinputs/emoji.txt', shell=True)
b'\\t2\\t3\\ttestinputs/emoji.txt\\n'

>>> # reversed flags combination: -w -l
>>> import subprocess
>>> subprocess.check_output('python3 wc.py -w -l testinputs/emoji.txt', shell=True)
b'\\t2\\t3\\ttestinputs/emoji.txt\\n'

>>> # test flag -c
>>> import subprocess
>>> subprocess.check_output('python3 wc.py -c testinputs/emoji.txt', shell=True)
b'\\t11\\ttestinputs/emoji.txt\\n'

>>> # illegal flag
>>> import subprocess
>>> subprocess.check_output('python3 wc.py -t testinputs/emoji.txt', shell=True)
b'wc: illegal option -- t\\n'

>>> # multiple files
>>> import subprocess
>>> subprocess.check_output('python3 wc.py testinputs/emoji.txt testinputs/html.html', shell=True)
b'\\t2\\t3\\t11\\ttestinputs/emoji.txt\\n\\t10\\t12\\t124\\ttestinputs/html.html\\n\\t12\\t15\\t135\\ttotal\\n'

>>> # multiple files with an illegal path
>>> import subprocess
>>> subprocess.check_output('python3 wc.py testinputs/emoji.txt testinputs/html.htm', shell=True)
b'\\t2\\t3\\t11\\ttestinputs/emoji.txt\\nwc: testinputs/html.htm: open: No such file or directory\\n\\t2\\t3\\t11\\ttotal\\n'

>>> # no arguments
>>> import subprocess
>>> subprocess.check_output('python3 wc.py', shell=True)
b'We don\\xe2\\x80\\x99t handle that situation yet!\\n'

>>> # -m (in wc but not in wc.py, can't handle yet!)
>>> import subprocess
>>> subprocess.check_output('python3 wc.py -m testinputs/empty_test.txt', shell=True)
b'We don\\xe2\\x80\\x99t handle that situation yet!\\n'

>>> # binary files, goes wrong, however hard to solve it
>>> import subprocess
>>> subprocess.check_output('python3 wc.py testinputs/pdf.pdf', shell=True)
b'\\t130\\t596\\t7985\\ttestinputs/pdf.pdf\\n'

>>> # treat - as missing file
>>> import subprocess
>>> subprocess.check_output('python3 wc.py -', shell=True)
b'wc: -: open: No such file or directory\\n'
'''