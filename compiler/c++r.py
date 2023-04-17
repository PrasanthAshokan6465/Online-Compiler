import sys
import subprocess
cmd="python c++e.py -i dev"
sys.stdin=open('input.txt','r')
re=subprocess.run(cmd, shell=True,stdin = sys.stdin,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
er=str(re.stderr)[2:-1]
l=[]
if er!="":
    n=1
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
    si=(st.index("'"))
    oc=st[si+1:-1]
    n=-1
    l.append("noerr")
    e=open('output.txt','w')
    for i in oc.split("\\r\\n"):
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
a='\\'
b=a[-1]
for i in we.readlines(n):
    ii=i.replace(b,'')
    l.append(ii)
print(l)