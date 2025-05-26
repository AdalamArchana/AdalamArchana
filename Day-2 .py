'''def secretcode(s):
    cu,cs,cn,cp,space=0,0,0,0,0
    for i in s:
        if i.isupper():
            cu+=1
        elif i.islower():
            cs+=1 
        elif i.isdigit():
            cn+=1
        elif i.isspace():
            space+=1
        else:
            cp+=1
    if(len(s)>=8 and s[0].isupper() and cu>=2 and cs>=2 and space==0 and cn>0 and cp>0):
        print("Valid Secret Code")
    else:
        print("Not a valid secret code")
    print(f"capital:{cu} ")
    print(f"small:{cs} ")
    print(f"number:{cn} ")
    print(f"special:{cp} ")
    print(f"space:{space} ")
s=input()
secretcode(s)
#630387947'''


'''t=(1,99.9,'happy',[1,2,3],None)
print(t)   #all elements
print(t[2]) #single elements
print(t[2:]) #certain part of tuple

#operators
t1=(1,2,3,4) 
print(t+t1) #cocatination
print(t1*3) #repetetion
print(t1>=t) #relation
print("happy" in t)
print(t1 is not t)'''

'''name="Archana"
print(tuple(name))
print(sorted(name))'''

'''pack='Apis','Kiddo','charan','yamini'
print(pack)
n1,n2,n3,n4=pack
print(n1,n2,n3,n4)'''

'''#arbitrary variable
suresh,*ramesh,naresh=(1,1,1,1,1,1,1,1,)
print(suresh,naresh,ramesh,sep='\t')'''


'''#set
s=set() #empty set
s1={1} #set with single elements
print(type(s1))
s2={1,2,3,4,5,6}
print(s2)
s3={44,55}
print(s2>s3)
print(66 not in s2)
print(s3 is not s2)'''

'''s={1,2,3,4}
s.add(6)
s.update({7,8,9})
s.remove(7)
s.discard(99)#if key is not present it won't rise any error
s.clear()#empties the set
print(s)'''

'''
s1={1,2,3,4,5}
s2={4,5,6,7,8}
#** sets internally uses hashing concept **
print(s1.union(s2))
s1.update(s2)
print(s1 | s2)
s1.update(s2)
print(s1.difference(s2))#return unique items from set 1
print(s1 - s2)
s1.difference_update(s2)#permanent
print(s1)
print(s1.intersection(s2))
print(s1 & s2)
print(s1.intersection_update(s2))
print(s1)
print(s1.symmetric_difference(s2))
print(s1^s2)
print(s1.symmetric_difference_update(s2))
print(s1)
print({4,5}.issubset(s1))
print(s1.issuperset({4,5}))
print(s1.isdisjoint(s2))'''

#dictionary
'''d={}#empty dictionary
print(type(d))
movies={
    1:"aa",
    2:"Bahubali",
    3:"Three",
    4:"aa Naluguruko",
    5:"Guru"
}'''
'''movies.update({6:"athadu"})
movies[3]="Mugguru monagalu"#replace
movies.pop(6)
movies.popitem()
print(movies)'''
#in order to add a new key we can use the below syntax
#obj[['key']='value']
#If the key is exist the value will be replace are else a key will be added to the new dictionary 
'''print(movies.setdefault(55,'five'))
print(movies)'''
'''digits={
    'one':1,'Two':2,'Three':3,'Four':4
    }
print('one' is digits)'''

'''l1=["NTR","Nani","Ram","RCB","Sam"]
print={dict.fromkeys(l1,100)}'''

'''movies={
    1:"aa",
    2:"Bahubali",
    3:"Three",
    4:"aa Naluguru",
    5:"Guru"
}
print(sorted(movies.values (),reverse=True))'''
'''
li1={'hulk','Iron man','super man','Bat man','Thor'}
li2={'lady hulk','wonder women','lady bug','wanda','Black widow'}
print(zip(li1,li2))'''

'''d={}
for i in range(5):
    a=input()
    b=int(input())
    d[a]=b
print(d)
print(max(d.values()))'''


'''names=['Adithya','Archana','Charan','Yamini','Navya']
d={}
for i in names:
    d[i]=len(i)
print(d)'''

'''
names=['vinod','sriram','jyoshna','faiza']
print({k:k*k for k in range(10,16) if k%2==0})
print({name:len(name) for name in names})
print({name:'even_length' if len(name)%2==0 else "odd_length" for name in names if len(name)>5})
'''

'''
name=input()
d=


'''

#collections modules
'''#counter
from collections import Counter
import random
#syntax:- variable =counter (sequence)
#string="My name is Apis"
s=[random.randrange(1,8) for i in range(10)]
var=Counter(s)
print(var)'''

'''
#default dict
from collections import defaultdict
#syntax:var=defaultdict(default_factory)
d= defaultdict(int)
d['a']=1
d['b']=2
print(d['a'])
print(d['b'])
print(d['c'])'''

'''
from collections import defaultdict
d= defaultdict(list)
d['cricket']=('kohli')
d['badminton']=('sindhu')
print(d['cricket'])
print(d['badminton'])
print(d['football'])
'''                


'''
#deque
from collections import deque
d=deque([1,2,3,4,5])
d.append(6)
d.appendleft(1)
d.pop()
d.popleft()
#d.extend([1,2,3])
#d.extendleft([-2,-1,0])
#d.remove(5)
#d.reverse()
d.rotate(-3)# +right,-left
print(d)
'''


#namedtuple
student= namedtuple(typename: 'student',field_names['name','branch','marks'])
s1=student('Apis','Aids','3009')
print(s1.name)
print(s1.marks)








































































