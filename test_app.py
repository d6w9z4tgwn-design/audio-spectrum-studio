import unittest,numpy as np
from app import spectrum
class Test(unittest.TestCase):
 def test_tone(self):
  f,y=spectrum(np.sin(2*np.pi*440*np.arange(8000)/8000),8000);self.assertEqual(f[y.argmax()],440)
