import time
import random
import math
import randomoptimize
import hilldown
import annealingoptimize
import geneticoptimize

people = [('Seymour','BOS'), 
('Franny','DAL'),
('Zooey','CAK'),
('Walt','MIA'),
('Buddy','ORD'),
('Les','OMA')]

destination='LGA'

flights={}
#
for line in file('schedule.txt'):
  origin,dest,depart,arrive,price=line.strip( ).split(',')
  flights.setdefault((origin,dest),[])
  flights[(origin,dest)].append((depart,arrive,int(price)))

def getminutes(t):
  x=time.strptime(t,'%H:%M')
  return x[3]*60+x[4]
  
def printschedule(r):
  for d in range(len(r)/2):
    name=people[d][0];
    origin=people[d][1];
    out=flights[(origin,destination)][r[d]];
    ret=flights[(destination,origin)][r[d+1]];
    print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name,origin,out[0],out[1],out[2],ret[0],ret[1],ret[2]);
    
def schedulecost(sol):
  totalprice=0
  latestarrival=0
  earliestdep=24*60
  
  for d in range(len(sol)/2):
    # incoming and outcomig
    origin=people[d][1]
    outbound=flights[(origin,destination)][int(sol[d])]
    returnf=flights[(destination,origin)][int(sol[d+1])]
    
    # full price 
    totalprice+=outbound[2]
    totalprice+=returnf[2]
    
    # latest arrival and earliest dep
    if latestarrival<getminutes(outbound[1]):
      latestarrival=getminutes(outbound[1])
    if earliestdep>getminutes(returnf[0]): earliestdep=getminutes(returnf[0])
    

  totalwait=0
  for d in range(len(sol)/2):
    origin=people[d][1]
    outbound=flights[(origin,destination)][int(sol[d])]
    returnf=flights[(destination,origin)][int(sol[d+1])]
    totalwait+=latestarrival-getminutes(outbound[1])
    totalwait+=getminutes(returnf[0])-earliestdep

  if latestarrival>earliestdep: totalprice+=50
  
  return totalprice+totalwait
  
def randomopt(domain,costf):
    return randomoptimize.randomoptimize(domain,costf)
    
def hilldownopt(domain, costf):
    return hilldown.hilldown(domain, costf)
    
def annealingopt(domain, costf):
    return annealingoptimize.annealingoptimize(domain, costf)
    
def geneticopt(domain, costf):
    return geneticoptimize.geneticoptimize(domain, costf)