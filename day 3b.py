my_input = 277678
n = 1

m=5;
h=2*m-1;
A=matrix(h, h);
print1(A[m, m]=1, ", ");
T=[[1, 0], [1, -1], [0, -1], [ -1, -1], [ -1, 0], [ -1, 1], [0, 1], [1, 1]];
for(n=1, (h-2)^2-1, g=sqrtint(n);
    r=(g+g%2)\2;
    q=4*r^2;
    d=n-q;
    if(n<=q-2*r, j=d+3*r;
       k=r, if(n<=q, j=r;
               k=-d-r, if(n<=q+2*r, j=r-d;
                          k=-r, j=-r;
                          k=d-3*r)));
    j=j+m;
    k=k+m;
    s=0;
    for(c=1, 8, v=[j, k];
        v+=T[c];
        s=s+A[v[1], v[2]]);
    A[j, k]=s;
    print1(s, ", "))
