 -*- coding: utf-8 -*-


def deco(howmuchqq):
    def wrapper():
        howmuchqq()
        if howmuchqq() == 0:
            print("Нет(")
        if howmuchqq() > 10:
            print("Очень много")
    return wrapper

def ORLst(l):
    l[:] = []
    
    
def howmuchqq():
    thenumb = int(0)
    for x in range(len(ls)):
        if x%2 == 0:
            themumb += 1
        else: 
            pass
    return thenumb

if __name__ == '__main__':
    import sys
    import argparse
    ls = sys.argv[1:]
    howmuchqq()
    howmuchqq_afterdeco() = deco(howmuchqq)
    howmuchqq_afterdeco()
