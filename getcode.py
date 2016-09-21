__author__ = 'hly'
with open('code','r') as code:
    files = code.readlines()
    for f in files:
        with open(f.strip(),'r') as ff:
            with open('codefile','a') as codef:
                codef.write(str(f))
                codef.write(ff.read())
