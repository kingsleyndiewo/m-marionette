import os.path as op
from adb import adb_commands
from adb import sign_m2crypto

# needed to connect to an Android device post KitKat
signer = sign_m2crypto.M2CryptoSigner(op.expanduser('~/.android/adbkey'))
# instance of ADB object
adb = adb_commands.AdbCommands()
# get a handle to the device
device = adb.ConnectDevice(rsa_keys=[signer])
# run an adb shell command to click for 2 seconds
device.Shell('input touchscreen swipe 500 500 500 500 2000')