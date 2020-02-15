from apps import wave
from apps.assess import PolynomialSpotFactor

superFactor = PolynomialSpotFactor("スーパー")
superFactor.appendData("イズミヤ", 35.041133, 135.781177, 3.0)
superFactor.appendData("カナート", 35.041141, 135.778983)
wave.appendFactor(superFactor, 1.2)
