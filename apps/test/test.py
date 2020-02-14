from apps.assess import Wave, PolynomialSpotFactor

superFactor = PolynomialSpotFactor(title="スーパー")
superFactor.appendData("イズミヤ", 1.0, 3.0)
superFactor.appendData("カナート", 3.4, 5.1)

wave = Wave()
wave.appendFactor(superFactor, 3)
scores = wave.evaluate(1.3, 3.4)
print(scores[0].total)