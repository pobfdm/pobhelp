pyinstaller -w -i lifesaver.ico pobhelp.py
copy lifesaver* .\dist\pobhelp\
mkdir .\dist\pobhelp\TightVNC-bundle
copy .\TightVNC-bundle .\dist\pobhelp\TightVNC-bundle

