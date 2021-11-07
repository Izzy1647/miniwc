'''
>>> import subprocess

>>> # empty file
>>> subprocess.check_output('python3 wc.py testinputs/empty_test.txt', shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty_test.txt\\n'

>>> # file with emoji
>>> subprocess.check_output('python3 wc.py testinputs/emoji.txt', shell=True)
b'\\t2\\t3\\t11\\ttestinputs/emoji.txt\\n'

>>> # html file
>>> subprocess.check_output('python3 wc.py testinputs/html.html', shell=True)
b'\\t10\\t12\\t124\\ttestinputs/html.html\\n'

>>> # py script
>>> subprocess.check_output('python3 wc.py testinputs/pyscript.py', shell=True)
b'\\t1\\t1\\t14\\ttestinputs/pyscript.py\\n'

>>> # flags combination: -l -w
>>> subprocess.check_output('python3 wc.py -l -w testinputs/emoji.txt', shell=True)
b'\\t2\\t3\\ttestinputs/emoji.txt\\n'

>>> # reversed flags combination: -w -l
>>> subprocess.check_output('python3 wc.py -w -l testinputs/emoji.txt', shell=True)
b'\\t2\\t3\\ttestinputs/emoji.txt\\n'

>>> # test flag -c
>>> subprocess.check_output('python3 wc.py -c testinputs/emoji.txt', shell=True)
b'\\t11\\ttestinputs/emoji.txt\\n'

>>> # illegal flag
>>> subprocess.check_output('python3 wc.py -t testinputs/emoji.txt', shell=True)
b'wc: illegal option --t\\n\\nusage: wc [-clw] [file ...]\\n\\n'

>>> # illegal flag
>>> subprocess.check_output('python3 wc.py -tyt testinputs/emoji.txt', shell=True)
b'wc: illegal option --tyt\\n\\nusage: wc [-clw] [file ...]\\n\\n'

>>> # multiple files
>>> subprocess.check_output('python3 wc.py testinputs/emoji.txt testinputs/html.html', shell=True)
b'\\t2\\t3\\t11\\ttestinputs/emoji.txt\\n\\t10\\t12\\t124\\ttestinputs/html.html\\n\\t12\\t15\\t135\\ttotal\\n'

>>> # multiple files with an illegal path
>>> subprocess.check_output('python3 wc.py testinputs/emoji.txt testinputs/html.htm', shell=True)
b'\\t2\\t3\\t11\\ttestinputs/emoji.txt\\nwc: testinputs/html.htm: open: No such file or directory\\n\\t2\\t3\\t11\\ttotal\\n'

>>> # -m (in wc but not in wc.py, can't handle yet!)
>>> subprocess.check_output('python3 wc.py -m testinputs/empty_test.txt', shell=True)
b'\\t0\\ttestinputs/empty_test.txt\\n'

>>> # binary files, goes wrong, however hard to solve it
>>> subprocess.check_output('python3 wc.py testinputs/pdf.pdf', shell=True)
b'\\t130\\t596\\t7985\\ttestinputs/pdf.pdf\\n'

>>> # treat - as missing file
>>> subprocess.check_output('python3 wc.py -', shell=True)
b'wc: -: open: No such file or directory\\n'

>>> # --
>>> subprocess.check_output('python3 wc.py -- -f', shell=True)
b'wc: -f: open: No such file or directory\\n'

>>> # treat - as missing file
>>> subprocess.check_output('python3 wc.py - -r -c testinputs/text.txt', shell=True)
b'wc: illegal option --r\\n\\nusage: wc [-clw] [file ...]\\n\\n'
'''