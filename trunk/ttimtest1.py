from pylab import *
from ttim import *

ml = ModelMaq(kaq=[1.0,5.0],z=[3,2,1,0],c=[10.],Saq=[0.3,0.01],Sll=[0.001],tmin=0.001,tmax=1000000.0,M=20)
#w1 = InternalStorageWell(ml,0.,0.,.1,1,[1])
w1 = Well(ml,xw=0.,yw=0,rw=.1,Q=[1],layer=[1])
ml.solve()

############################################
# following lines create figures in manual, 
# MLU output read in from data files *.fth
############################################
t0 = 10**linspace(-3,4,50)
h0 = ml.head(.2,0,t0)
r0=loadtxt('x0y0.fth')

figure(1)
semilogx(t0,-h0[0],'b+')
semilogx(t0,-h0[1],'g+')
semilogx(r0[:,0], -r0[:,1],'b')
semilogx(r0[:,0], -r0[:,2],'g')
legend(('ttim, upper', 'ttim, lower', 'mlu, upper', 'mlu, lower'), loc=2)
xlabel('time')
ylabel('drawdown')
title('r=0.2')
show()

t1 = 10**linspace(-2,5,50)
h1 = ml.head(1,0,t1)
r1=loadtxt('x1y0.fth')

figure(2)
semilogx(t1,-h1[0],'b+')
semilogx(t1,-h1[1],'g+')
semilogx(r1[:,0], -r1[:,1],'b')
semilogx(r1[:,0], -r1[:,2],'g')
legend(('ttim, upper', 'ttim, lower', 'mlu, upper', 'mlu, lower'),loc=2)
xlabel('time')
ylabel('drawdown')
title('r=1.0')
show()

t5 = 10**linspace(-1,6,50)
h5 = ml.head(5,0,t5)
r5=loadtxt('x5y0.fth')

figure(3)
semilogx(t5,-h5[0],'b+')
semilogx(t5,-h5[1],'g+')
semilogx(r5[:,0], -r5[:,1],'b')
semilogx(r5[:,0], -r5[:,2],'g')
legend(('ttim, upper', 'ttim, lower', 'mlu, upper', 'mlu, lower'),loc=2)
xlabel('time')
ylabel('drawdown')
title('r=5.0')
show()
 
t10 = 10**linspace(-1,6,50)
h10 = ml.head(10,0,t10)
r10=loadtxt('x10y0.fth')

figure(4)
semilogx(t10,-h10[0],'b+')
semilogx(t10,-h10[1],'g+')
semilogx(r10[:,0], -r10[:,1],'b')
semilogx(r10[:,0], -r10[:,2],'g')
legend(('ttim, upper', 'ttim, lower', 'mlu, upper', 'mlu, lower'),loc=2)
xlabel('time')
ylabel('drawdown')
title('r=10')
show()
