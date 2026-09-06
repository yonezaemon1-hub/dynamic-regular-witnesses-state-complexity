#!/usr/bin/env python3
"""Finite implementation audit for Paper 7 regular slow-cone constructions.
NOT A PROOF: checks exactly the 6,253 finite parameter cases reported in the manuscript.
"""

def add_edge(adj,u,v):
    assert u!=v
    assert v not in adj[u], ('duplicate',u,v)
    adj[u].add(v); adj[v].add(u)

def cycle(adj,seq):
    for i,u in enumerate(seq): add_edge(adj,u,seq[(i+1)%len(seq)])

def match_halves(adj,verts):
    m=len(verts); assert m>=4 and m%2==0
    h=m//2
    for i in range(h): add_edge(adj,verts[i],verts[i+h])

def cpower2(adj,seq):
    n=len(seq)
    for i,u in enumerate(seq):
        for k in (1,2):
            v=seq[(i+k)%n]
            if v not in adj[u]: add_edge(adj,u,v)

def remove_edge(adj,u,v):
    adj[u].remove(v); adj[v].remove(u)

def protected_quartic(adj,S,x,z=None):
    before={v:set(adj[v]) for v in S+[x]}
    cpower2(adj,S)
    edges=[]
    for u in S:
        for v in adj[u]:
            if v in S and u<v: edges.append((u,v))
    uv=next(e for e in sorted(edges) if z is None or z not in e)
    remove_edge(adj,*uv); add_edge(adj,uv[0],x); add_edge(adj,uv[1],x)
    return 2

def protected_cubic(adj,S,x,z=None):
    s=len(S); cycle(adj,S)
    if s%2==0:
        h=s//2; M=[]
        for i in range(h): add_edge(adj,S[i],S[i+h]); M.append((S[i],S[i+h]))
        uv=next(e for e in M if z is None or z not in e)
        remove_edge(adj,*uv); add_edge(adj,uv[0],x); add_edge(adj,uv[1],x)
        return 2
    h=(s-1)//2
    for i in range(1,h+1): add_edge(adj,S[i],S[i+h])
    add_edge(adj,S[0],x); return 1

def comp_quartic(adj,R,con):
    con=list(con); ords=[v for v in R if v not in con]
    if len(con)==0: cpower2(adj,R)
    elif len(con)==1:
        cycle(adj,[con[0]]+ords); cycle(adj,ords[0::2]+ords[1::2])
    elif len(con)==2:
        x,y=con
        if len(R)==6:
            for i,u in enumerate(R):
                for v in R[i+1:]: add_edge(adj,u,v)
            a,b,c,d=ords
            for e in [(x,y),(x,a),(x,b),(y,c),(y,d)]: remove_edge(adj,*e)
        else:
            cycle(adj,[x]+ords+[y]); cycle(adj,ords[0::2]+ords[1::2])
    else: assert False

def comp_cubic(adj,R,resid):
    con=list(resid); ords=[v for v in R if v not in con]
    ds=[resid[v] for v in con]
    if len(con)==0:
        cycle(adj,ords); match_halves(adj,ords)
    elif len(con)==1:
        x=con[0]; d=ds[0]
        if d==2: cycle(adj,[x]+ords); match_halves(adj,ords)
        else: cycle(adj,ords); add_edge(adj,x,ords[0]); match_halves(adj,ords[1:])
    else:
        x,y=con; d1,d2=ds
        if (d1,d2)==(2,1): x,y,d1,d2=y,x,1,2
        if (d1,d2)==(1,1):
            add_edge(adj,x,ords[0])
            for i in range(len(ords)-1): add_edge(adj,ords[i],ords[i+1])
            add_edge(adj,ords[-1],y); match_halves(adj,ords)
        elif (d1,d2)==(2,2):
            cycle(adj,[x]+ords+[y]); match_halves(adj,ords)
        elif (d1,d2)==(1,2):
            if len(ords)==3:
                allv=[x,y]+ords
                for i,u in enumerate(allv):
                    for v in allv[i+1:]: add_edge(adj,u,v)
                a,b,c=ords
                for e in [(x,y),(x,a),(x,b),(y,c)]: remove_edge(adj,*e)
            else:
                cycle(adj,[y]+ords); add_edge(adj,x,ords[0]); match_halves(adj,ords[1:])
        else: assert False,(d1,d2)

def nested(pool,tb,first):
    z=pool[0]
    if tb==0: return z,{}
    C={tb:{z},tb-1:set(pool[:first])}; idx=first
    for t in range(tb-2,-1,-1): C[t]=set(C[t+1])|{pool[idx]}; idx+=1
    assert idx==len(pool); return z,C

def connected(adj):
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen: seen.add(v); stack.append(v)
    return len(seen)==len(adj)

def verify(adj,d):
    assert connected(adj)
    assert all(len(ns)==d for ns in adj)
    # symmetry + simplicity implicit in add/remove, verify anyway
    for u,ns in enumerate(adj):
        assert u not in ns
        for v in ns: assert u in adj[v]

def audit_case(n,t0,t1,d):
    extra=4 if d==4 else 3; first=5 if d==4 else 4
    U0=list(range(t0+extra)); U1=list(range(len(U0),len(U0)+t1+extra)); M=list(range(len(U0)+len(U1),n))
    assert len(M)>=(6 if d==4 else 5)
    z0,C0=nested(U0,t0,first); z1,C1=nested(U1,t1,first)
    zs=[z0,z1]; Cs=[C0,C1]; ts=[t0,t1]
    graphs=[]
    for t in range(max(ts)):
        adj=[set() for _ in range(n)]; S_all=set(); con_bd={}; usedM=set()
        for b in (0,1):
            tb=ts[b]
            if t>=tb: continue
            if t==tb-1:
                S=sorted(Cs[b][t]); x=next(v for v in M if v not in usedM); usedM.add(x); z=zs[b]
            else:
                S=sorted(Cs[b][t+1]); x=next(iter(Cs[b][t]-Cs[b][t+1])); z=None
            assert S_all.isdisjoint(S); S_all.update(S); assert x not in S_all; assert x not in con_bd
            bd=protected_quartic(adj,S,x,z) if d==4 else protected_cubic(adj,S,x,z)
            con_bd[x]=bd
        R=[v for v in range(n) if v not in S_all]
        if d==4: comp_quartic(adj,R,con_bd)
        else:
            resid={x:3-bd for x,bd in con_bd.items()}
            assert (sum(resid.values())+3*(len(R)-len(resid)))%2==0
            comp_cubic(adj,R,resid)
        verify(adj,d); graphs.append(adj)
    B0=[]
    for b in (0,1):
        B={zs[b]}; tb=ts[b]
        for t in range(tb-1,-1,-1):
            N=set()
            for v in B: N.update(graphs[t][v])
            B |= N
            assert B==Cs[b][t],(n,t0,t1,d,b,t,B,Cs[b][t])
        B0.append(B)
    assert B0[0].isdisjoint(B0[1])

def main():
    q=c=0
    for n in range(15,41):
        m=n-14
        for t0 in range(m+1):
            for t1 in range(m-t0+1): audit_case(n,t0,t1,4); q+=1
    for n in range(12,41,2):
        m=n-11
        for t0 in range(m+1):
            for t1 in range(m-t0+1): audit_case(n,t0,t1,3); c+=1
    assert q==3653 and c==2600
    print('VERDICT=PASS_CONSTRUCTION_AUDIT_NOT_A_PROOF')
    print('QUARTIC_CASES='+str(q)); print('CUBIC_CASES='+str(c)); print('TOTAL_CASES='+str(q+c)); print('FAILURES=0')
if __name__=='__main__': main()
