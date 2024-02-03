import zymkey
from textwrap import fill
import time

print('Testing data lock...')
src = bytearray(b'\x01\x02\x03\x04')
dst = zymkey.client.lock(src)
print('Original Data')
s = fill(' '.join('{:02X}'.format(c) for c in src), 49)
print(s)
print('Encrypted Data')
s = fill(' '.join('{:02X}'.format(c) for c in dst), 49)
print(s)

print('Testing data unlock...')
new_src = dst
new_dst = zymkey.client.unlock(new_src)
print('Decryped Data')
s = fill(' '.join('{:02X}'.format(c) for c in new_dst), 49)
print(s)

print('Turning LED on...')
zymkey.client.led_on()

time.sleep(1)

print('Turning LED off...')
zymkey.client.led_off()

print("script ended")
