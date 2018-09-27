# p96

signals = {"green": "go", "yellow": "go faster", "red": "smile for the camera"}
save_signals = signals
signals["blue"] = "confuse everyone"
print(save_signals)

signals = {"green": "go", "yellow": "go faster", "red": "smile for the camera"}
original_signals = signals.copy()
signals["blue"] = "confuse everyone"
print(signals)
print(original_signals)
