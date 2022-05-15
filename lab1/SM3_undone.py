message="011000010110001001100011"


#填充

def CSL(bits, n):
    return bits[n:]+bits[:n]
    
def pad(msg):
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
    return msg


#压缩
def cpr(v):
    words=[ [] for i in range(8)]
    
    for i in range(0,256,32):
        words[i//32] = v[i:i+32]#分配字

    for j in range(64):
        if(0<=j<=15):
            T = ['1', '1', '1', '1', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '1', '0', '0', '1']
        if（16<=j<=63):
            T = ['1', '1', '1', '1', '0', '1', '0', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '0', '1', '1', '0', '0', '0', '1', '0', '1', '0']
        ss1 =CSL(list(bin(
              int(''.join(CSL(words[0],12)),2)
             +int(''.join(words[4]),2)
             +int(''.join(CSL(T,j)),2)
             )[2:]),7)
            



#扩展
def ext():
    pass


