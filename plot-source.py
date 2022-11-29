import matplotlib.pyplot as plt

xArray = [];
yArray = [];

with open('NGC5772_i.txt') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        if count:
            index = count - 1
            lineArray = line.split()
            x = lineArray[0]
            y = lineArray[1]
            x = count
            y = count * 2.15
            xArray.append(x)
            yArray.append(y)
            print(str(x) + ' ' + str(y))
        count += 1
plt.plot(xArray, yArray,'r--')
plt.show()
plt.savefig('NGC5772_i-txt.png')
 plt.get_backend()
