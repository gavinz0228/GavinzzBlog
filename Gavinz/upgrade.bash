echo '' >> .bashrc && echo 'source virtualenvwrapper.sh' >> .bashrc
source virtualenvwrapper.sh
mkvirtualenv django17 --python=/usr/bin/python3.4
pip install django ## this may take a couple of minutes