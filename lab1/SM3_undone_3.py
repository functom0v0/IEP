#message="011000010110001001100011"
message=bin(int("abc",16))[2:]
msg1=[]
numGroup = 0

#循环左移
##def CSL(bits, n):
##    return int(bits[n:]+bits[:n],2)

def CSL1(bits, n):
    n = n % 32
    return ((bits << n) & 0xFFFFFFFF) | ((bits & 0xFFFFFFFF) >> (32 - n)) 
    

#填充及得到B分组
def pad(msg):
    #填充
    msg = list(msg)
    l = len(msg)
    padlen = list(bin(l)[2:])
    tmp = 64-len(padlen)
    for i in range(tmp):
        padlen.insert(0,'0')#得到64位比特串
    msg += '1'
    k = 0  #num of 0
    for i in range(512):
        if ((l+1+i) %512) == 448:
            k = i
            break
    pad0 = [ '0' for i in range(k)]
    msg += pad0
    msg += padlen
    #消息分组
    for i in range(0,len(msg),512):
        msg1.append(msg[i:i+512])
    global numGroup
    numGroup = len(msg1)

    
#压缩
def cpr(v,b,w,w1):
    #分配字
    A = v[0]
    B = v[1]
    C = v[2]
    D = v[3]
    E = v[4]
    F = v[5]
    G = v[6]
    H = v[7]

    for j in range(16):
            T = 0x79cc4519
            tmp1 = CSL1(A,12)
            ss1  = CSL1(tmp1 + E + CSL1(T,j),7)
            ss2  = ss1 ^ tmp1
            tt1 = (A^B^C + D + ss2 + w1[j]) 
            tt2 = (E^F^G + H + ss1 + w[j])  
            D = C
            C = CSL1(B,9)
            B = A
            A = tt1
            H = G
            G = CSL1(F,19)
            F = E
            E = tt2^CSL1(tt2,9)^CSL1(tt2,17)
            
    for j in range(16,64):
            T = 0x7a879d8a
            tmp1 = CSL1(A,12)
            ss1  = CSL1(tmp1 + E + CSL1(T,j),7)
            ss2  = ss1 ^ tmp1
            tt1 = (((A & B)|(B & C)|(A & C)) + D + ss2 + w1[j])    
            tt2 = (((E & F)|((E^0xFFFFFFFF) & G)) + H + ss1 + w[j])
            D = C
            C = CSL1(B,9)
            B = A
            A = tt1
            H = G
            G = CSL1(F,19)
            F = E
            E = tt2^CSL1(tt2,9)^CSL1(tt2,17)
    #tmp1 = hex(A)[2:]+hex(B)[2:]+hex(C)[2:]+hex(D)[2:]+hex(E)[2:]+hex(F)[2:]+hex(G)[2:]+hex(H)[2:]
    #tmp1 = int(str(A)+str(B)+str(C)+str(D)+str(E)+str(F)+str(G)+str(H))
    #print(len(hex(int(tmp1))))

    A = A & 0xFFFFFFFF
    B = B & 0xFFFFFFFF
    C = C & 0xFFFFFFFF
    D = D & 0xFFFFFFFF
    E = E & 0xFFFFFFFF
    F = F & 0xFFFFFFFF
    G = G & 0xFFFFFFFF
    H = H & 0xFFFFFFFF

    resV = [A^v[0],B^v[1],C^v[2],D^v[3],
            E^v[4],F^v[5],G^v[6],H^v[7]]
    return resV

#消息扩展
def ext(b):
    w = [0 for i in range(68)]
    w1= [0 for i in range(64)]
    for i in range(16):
        tmp1 = i*32
        tmp2 = b[tmp1:tmp1+32]
        w[i] = int(''.join(tmp2),2)
        
    for j in range(16,68):
        tmp1 = w[j-16]^w[j-9]^(CSL1(w[j-3],15))
        tmp2 = tmp1^CSL1(tmp1,15)^CSL1(tmp1,23)
        w[j] = tmp2^(CSL1(w[j-13],7))^w[j-13]

    for j in range(64):
        w1[j] = w[j]^w[j+4]
    return w,w1

##def WperB():
##    for i in range(numGroup):

def SM3():
    IV= [0x7380166f,0x4914b2b9,0x172442d7,0xda8a0600,0xa96f30bc,0x163138aa,0xe38dee4d,0xb0fb0e4e]
    pad(message)
    for i in range(numGroup):
        w,w1 = ext(msg1[i])
        IV = cpr(IV,msg1[i],w,w1)
        for j in IV:
            print(hex(j),end = " ")
        print()

SM3()


