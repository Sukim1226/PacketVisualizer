import matplotlib.pyplot as plt
#a = [x for x in range(0, 11)]
#b = [y for y in range(0, 11)]
#plt.plot(a, b)
#plt.show()

fig, gnt = plt.subplots()
gnt.set_ylim(0, 50)
gnt.set_xlim(0.160)
gnt.set_xlabel('Time')
gnt.set_ylabel('Packet')

gnt.set_yticks([15, 25, 35])
#gnt.set_yticks([10, 20, 30])
gnt.set_yticklabels(['Wi-Fi', 'ZB', 'BLE'])

gnt.grid(True)

gnt.broken_barh([(40, 50)], (30, 9), facecolors = ('tab:orange'))
gnt.broken_barh([(100, 10), (150, 10)], (10, 9), facecolors = 'tab:blue')
gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9), facecolors = ('tab:red'))

plt.show()
