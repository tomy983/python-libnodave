# Python interface to the libnodave C lib

## How to install 

Compile and install the libnodave c libs

    git clone git://github.com/tomy983/libnodave.git 
    cd libnodave
    make
    sudo make install
    cd ..
    git clone https://github.com/netdata-be/python-libnodave.git
    cd python-libnodave
    sudo python3 setup.py install
    
Try it (example tested on S7 CPU315 with 700-751-8MD21 MPI to RS232 adapter by Systeme Helmholz

    sudo python3 example.py

*Changes to the __init__.py must be followed by "sudo python3 setup.py install"
