import os
import sys
def daskolkouzemozno():
    try:
        A = sys.argv[1]
        f = open('output.txt', 'w')
        try:
            f.write(str(os.stat(str(A)).st_size))
            f.close()
            return 0
        except:
            f.write('Can\'t open file' + ' ' + A)
            f.close()
            return 2
    except:
        f = open('output.txt', 'w')
        f.write('Usage: stat filename\n')
        f.close()
        return 1

exit(daskolkouzemozno())