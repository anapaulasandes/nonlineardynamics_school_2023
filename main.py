import network

import argparse
import datetime
import scipy.stats as stat
import matplotlib.pyplot as plt

def main(ni,ne):

    time_max = 1000


    spikes = []
    times = []

    #fig = plt.figure(figsize=(6,6))

    #ax1 = fig.add_subplot(111)

    #t0 = datetime.datetime.now()

    net = network.Network(ni,ne)

    #t1 = datetime.datetime.now()


    

    # print('configured network in:', t1 - t0)

    #t0 = datetime.datetime.now()

    for t in range(time_max):
        net.input[0 : net.numEx] = 5.0 * stat.norm.rvs(size=net.numEx)
        net.input[net.numEx : ] = 2.0 * stat.norm.rvs(size=net.numIn)

        tmp = net.update()
        for n in tmp:
            spikes.append(n)
            times.append(t)

    #t1 = datetime.datetime.now()

    #print('simulated', time_max, 'steps in: ', t1 - t0)

    #ax1.set_title(f'Ne={ne}, Ni={ni}')

    #ax1.plot(times, spikes, ',k')


    #xl, xr = ax1.get_xlim()
    #yb, yt = ax1.get_ylim()

    #ax1.set_aspect(abs((xr - xl) / (yb - yt))  * 1.0)
    #ax1.axhline(color='r', y=net.numEx - 0.5, xmax=time_max)

    

    return times, spikes

    

if __name__ == "__main__":
    main()