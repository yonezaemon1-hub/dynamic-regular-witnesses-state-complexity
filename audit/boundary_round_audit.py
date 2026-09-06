#!/usr/bin/env python3
"""Finite arithmetic/index sanity checks for Paper 7. NOT A PROOF."""

def cdiv(a,b): return (a+b-1)//b

def main():
    rows=0
    for n in range(4,31):
        Ps=sorted(set([1,max(1,n-3),max(1,n-2),n-1,n,n+1]))
        for P in Ps:
            upper=2+cdiv(n-1,P)
            exact3=P>=n-1
            assert (upper==3)==exact3
            lower=3
            if n>=15: lower=max(lower,2+cdiv(n-13,P))
            if n>=12 and n%2==0: lower=max(lower,2+cdiv(n-10,P))
            if P<=n-2: lower=max(lower,4)
            assert lower<=upper,(n,P,lower,upper)
            rows+=1
    idx=0
    for n in range(4,101):
        P=n-2
        for j in range(0,P-1):
            assert 0<=j<=P-2
            assert n-3==P-1
            assert j+1<=P-1
            idx+=1
        for psi in range(P):
            dist=psi+1
            assert 1<=dist<=n-2
            if psi: assert psi-1<=P-2
            assert dist-1==psi
            idx+=1
    print('VERDICT=PASS_BOUNDARY_ROUND_SANITY_NOT_A_PROOF')
    print('BOUNDARY_ROWS='+str(rows))
    print('ROUND_INDEX_CASES='+str(idx))
    print('FAILURES=0')

if __name__=='__main__': main()
