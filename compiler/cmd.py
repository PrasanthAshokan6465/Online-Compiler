import sys
import subprocess

cmd="python c.py"
l=[]
#subprocess.call(cmd, shell=True)
re=subprocess.run(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
er=str(re.stderr)[2:-1]
print(er)
print(re.stdout)
if er!="":
    l.append("err")
    e=open('output.txt','w')
    for i in er.split("\\r\\n")[1:]:
        #print(i)
        if (r'\t' in i):
            for j in i.split(r"\t"):
                #print(j)
                e.write(j+" ")
            e.writelines("\n")
        else:
            e.writelines(i)
            e.writelines("\n")
    e.close()
else:
    st=str(re.stdout)
    si=(st.index(">"))
    oc=st[si+1:-1]
    l.append("noerr")
    e=open('output.txt','w')
    for i in oc.split("\\r\\n")[1:]:
        #print(i)
        if (r'\t' in i):
            for j in i.split(r"\t"):
                #print(j)
                e.write(j+" ")
            e.writelines("\n")
        else:
            e.writelines(i)
            e.writelines("\n")
    e.close()
we=open("output.txt","r")
for i in we.readlines():
    l.append(i)
print(l)