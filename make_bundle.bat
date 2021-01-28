pyinstaller --noconfirm -w -i lifesaver.ico pobhelp.py
copy lifesaver* .\dist\pobhelp\
copy static.key .\dist\pobhelp\
copy *.ovpn .\dist\pobhelp\

mkdir .\dist\pobhelp\TightVNC-bundle
copy .\TightVNC-bundle .\dist\pobhelp\TightVNC-bundle

mkdir .\dist\pobhelp\Openvpn-bundle
copy .\Openvpn-bundle .\dist\pobhelp\Openvpn-bundle
