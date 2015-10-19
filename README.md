
# RaspberryPi-Jasper-LED

1. Type the following command to download the GPIO library as a tarball:<br />
wget http://raspberry-gpio-python.googlecode.com/files/RPi.GPIO-0.4.1a.tar.gz<br /><br/>

2. Unzip the tarball:<br />
tar zxvf RPi.GPIO-0.4.1a.tar.gz<br /><br/>

3. Change to the directory where tarball was inflated:<br />
cd RPi.GPIO-0.4.1a<br /><br/>

4. Install the Python GPIO library in RPi:<br />
sudo python setup.py install<br /><br/>


5. Put file and folder on the following path: <br />
OZ_pi folder : /home/pi/home/pi/OZ_pi  <br />
SHLight module : ../jasper/client/modules/SHLight.py  <br /><br/>

6. Rerun boot.sh in jasper/boot/ to declare module's new words.
