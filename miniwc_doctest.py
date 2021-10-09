'''
>>> import subprocess
>>> subprocess.check_output('python3 miniwc.py testinputs/test.txt', shell=True)
'9  5  28  testinputs/test.txt\\n'

>>> import subprocess
>>> subprocess.check_output('python3 miniwc.py testinputs/ctest.txt', shell=True)
'6  9  99  testinputs/ctest.txt\\n'

>>> import subprocess
>>> subprocess.check_output('python3 miniwc.py testinputs/btest.txt', shell=True)
'7  7  16  testinputs/btest.txt\\n'

>>> import subprocess
>>> subprocess.check_output('python3 miniwc.py testinputs/dtest.txt', shell=True)
'10  6  38  testinputs/dtest.txt\\n'

>>> import subprocess
>>> subprocess.check_output('python3 miniwc.py testinputs/htest.html', shell=True)
'10  12  124  testinputs/htest.html\\n'

>>> import subprocess
>>> subprocess.check_output('python3 miniwc.py testinputs/ptest.py', shell=True)
'1  1  14  testinputs/ptest.py\\n'
'''


