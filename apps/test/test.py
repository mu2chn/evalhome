from apps.assess import Wave, PolynomialSpotFactor

superFactor = PolynomialSpotFactor("スーパー")
superFactor.appendData("イズミヤ", 35.041133, 135.781177, 3.0)
superFactor.appendData("カナート", 35.041141, 135.778983)

wave = Wave()
wave.appendFactor(superFactor, 1.2)
scores = wave.evaluate(35.041058, 135.782566)
print(scores[0].total)