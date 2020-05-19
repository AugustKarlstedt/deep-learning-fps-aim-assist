from detecto import core, utils, visualize
import matplotlib.pyplot as plt

dataset = core.Dataset('frames/')
model = core.Model(['enemy'])

model.fit(dataset, verbose=True)
model.save('model.pth')
