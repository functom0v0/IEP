from gmssl import sm3,func
import random
import time

def birthdayAttack(listlen,rd,hashlen):
    print("前",hashlen,"比特: ")
    rdmlst = []
    dictA = dict()
    
    for i in range(pow(2,listlen)):
        r = random.randint(0, pow(2,64))
        if r not in rdmlst:
            rdmlst.append(r)
            
    for i in range(pow(2,rd)):
        msg = str(rdmlst[i])
        bmsg = str(rdmlst[i])
        tmphash = sm3.sm3_hash(func.bytes_to_list(bytes(bmsg,encoding = 'utf-8')))
        tmphash = tmphash[0:hashlen]
        if tmphash not in dictA:
            dictA[tmphash] = []
            dictA[tmphash].append(msg)
        else:
            dictA[tmphash].append(msg)
    flag = 0
    
    for key,lst in dictA.items():
        if(len(lst)>=2):
            flag=1
            print("哈希值:", key)
            print("碰撞值:",lst)
            for k in range(len(lst)):
                msg = str(lst[k])
                tmphash = sm3.sm3_hash(func.bytes_to_list(bytes(msg, encoding='utf-8')))
                print(tmphash)
    if flag == 0:
        print("无碰撞")

start = time.time()
birthdayAttack(17,16,7)
end = time.time()
print("耗时{:.5f}s".format(end-start))
