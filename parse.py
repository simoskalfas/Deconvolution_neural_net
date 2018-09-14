def handle_file(filename, make_txt=False):
    datdic = {}
    with open('../Data/' + filename + '.txt', 'r') as f:
        fl = f.readline()
        fl = fl.replace('\r', '')
        fl = fl.replace('\n', '')
        fl = fl.split('\t')
        for i in fl:
            datdic[str(i)] = []
        for line in f:
            spl = line.replace('\r', '')
            spl = spl.replace('\n', '')
            spl = spl.split('\t')
            for j in range(len(spl)):
                datdic[fl[j]].append(float(spl[j]))
    if make_txt:
        with open('splitdata.txt', 'w') as f:
            for i in datdic:
                f.write(str(i))
                f.write(str(datdic[str(i)]))
                f.write('\n')
    return datdic


def aline(datdic, filename, gen_text=False):
    fullkeys = sorted(datdic)
    keys = fullkeys[:-1]
    datamat = [datdic[i] for i in keys]
    fullind = []
    for i in range(0, len(datamat)):
        alist = datamat[i][::]
        alist.sort()
        peaks = alist[-2:]
        alind = [datamat[i].index(j) for j in peaks]
        alind.sort()
        fullind.append(alind)
    firstind = [i[0] for i in fullind]
    disp = [i - min(firstind) for i in firstind]
    print 'Alinement displacement:' + str(disp)
    for i in range(0, len(datamat)):
        datamat[i] = datamat[i][disp[i]:]
        datamat[i] += [0 for _ in range(disp[i])]
        print len(datamat[i])
    retdic = {}
    for i in range(len(keys)):
        retdic[keys[i]] = datamat[i]
    retdic[fullkeys[-1]] = datdic[fullkeys[-1]]
    if gen_text:
        with open(filename + 'alined_' + '.txt', 'w') as f:
            for i in sorted(retdic):
                f.write(str(i))
                f.write('\t')
            f.write('\n')
            for i in range(len(retdic[keys[0]])):
                for j in sorted(retdic):
                    f.write(str(retdic[j][i]))
                    f.write('\t')
                f.write('\n')
    return retdic


def main():
    filename = 'mvar_unsmoothed'
    datadic = handle_file(filename)
    for i in datadic:
        if i != filename:
            datadic[i] = smoother.smooth(datadic[i])
    with open('simple.txt', 'w') as f:
        for i in range(len(datadic['10V'])):
            f.write(str(datadic[filename][i]))
            f.write('\t')
            f.write(str(datadic['10V'][i]))
            f.write('\n')
    with open('moderate.txt', 'w') as f:
        for i in range(len(datadic['38V'])):
            f.write(str(datadic[filename][i]))
            f.write('\t')
            f.write(str(datadic['38V'][i]))
            f.write('\n')


if __name__ == '__main__':
    main()
