import os.path as op
from adb import adb_commands
from adb import sign_m2crypto
from random import randint

# needed to connect to an Android device post KitKat
signer = sign_m2crypto.M2CryptoSigner(op.expanduser('~/.android/adbkey'))
# instance of ADB object
adb = adb_commands.AdbCommands()
# get a handle to the device
device = adb.ConnectDevice(rsa_keys=[signer])
# get a screenshot and save the image
n = randint(1, 1000)
with open(f'screens/screenshot{n}.png', 'wb') as img_file:
	conn = device.protocol_handler.Open(device._handle, "shell:screencap -p".encode('utf8'))
	
	for data in conn.ReadUntilClose():
		img_file.write(data)