
def dec_to_bin(IP):
    bin_list = list()
    for i in IP:
        bin_list.append('{:b}'.format(i))
    return complete_octeto(bin_list[:])

def complete_octeto(bin_ip):
    bin_list=bin_ip[:]
    octeto=""
    for i in range(len(bin_list)):
        if len(bin_list[i])<8:
            for j in range(8-len(bin_list[i])):
                octeto += "0"
            octeto+=bin_list[i]
            bin_list[i]=octeto
            octeto=""
    return bin_list

def bin_to_dec(bin_ip):
    din_ip=complete_octeto(bin_ip[:])
    dec_ip=list()
    dec_ip.append(int(bin_ip[0],2))
    dec_ip.append(int(bin_ip[1], 2))
    dec_ip.append(int(bin_ip[2], 2))
    dec_ip.append(int(bin_ip[3], 2))

    return dec_ip

def split_ip(IP):
    new_ip=IP.split(".")
    return new_ip

def string_bin_ip(IP_bin):
    string_bin=""
    for i in IP_bin:
        string_bin+=i
    return string_bin
def host_formule(num_host):
    n_host=0
    idx=0
    while num_host>=n_host:
        idx+=1
        n_host=pow(2,idx)-2
    return n_host, idx

def calc_mask(n):
    string_mask=""
    for i in range(32):
        if i <  32-n:
            string_mask+="1"
        else:
            string_mask+="0"
    mask = list()
    mask.append(string_mask[: 8])
    mask.append(string_mask[8: 16])
    mask.append(string_mask[16: 24])
    mask.append(string_mask[24: 32])
    return mask
def first_ip(ip):
    newip=ip
    if ip[3]<255:
        newip[3]=ip[3]+1
    elif ip[3] == 255 and ip[2] < 255:
        newip[2]=ip[2] +1
        newip[3]=0
    elif ip[3] == 255 and ip[2] == 255 and ip[1] < 255:
        newip[1] = ip[2] + 1
        newip[2] = 0
        newip[3] = 0
    return newip
def last_ip(ip):
    newip=ip
    if ip[3]>0:
        newip[3]=ip[3]-1
    elif ip[3] == 0 and ip[2] > 0:
        newip[2]=ip[2] -1
        newip[3]=255
    elif ip[3] == 0 and ip[2] == 0 and ip[1] > 0:
        newip[1] = ip[2] + 1
        newip[2] = 255
        newip[3] = 255
    return newip

def string_IP_to_IP(string_IP):
    dir_ip = list()
    dir_ip.append(string_IP[: 8])
    dir_ip.append(string_IP[8: 16])
    dir_ip.append(string_IP[16: 24])
    dir_ip.append(string_IP[24: 32])
    return dir_ip

def broadcast(bIP, n):
    bynary_string_ip= string_bin_ip(bIP)
    brcast = bynary_string_ip[:len(bynary_string_ip)-n]
    for i in range(n):
        brcast +="1"

    return bin_to_dec(complete_octeto(string_IP_to_IP(brcast)))


def subnet(ip,num_host):
    binary_IP = dec_to_bin(ip[:])
    num_host_n = host_formule(num_host)
    new_mask=bin_to_dec(calc_mask(num_host_n[1]))

    Dir_IP = ip
    First_IP = first_ip(Dir_IP[:])

    dir_broadcast = broadcast(binary_IP[:],num_host_n[1])
    last_IP = last_ip(dir_broadcast[:])

    return num_host_n[0],Dir_IP, 32-num_host_n[1],new_mask,First_IP,last_IP,dir_broadcast



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    #ejercicio1
    #LAN
    '''
    nets=[[[172, 100, 7, 0],[120, 50]],
         [[172, 100, 7, 0],[200, 60]],
         [[172, 100, 7, 0],[175, 40]],]
    '''
    #WAN
    #nets=[[[192,14,2,0],[1,1,1]]]

    #Ejercicio 2

    #LAN
    '''
    nets=[[[10,1,32,0],[250,150]],
         [[10,1,32,0],[50,30]],
         [[10,1,32,0],[160,68]],
         [[10,1,32,0],[128,120]]]
    '''

    #WAN
    #nets = [[[170, 20, 0, 0], [1,1,1,1,1]]]

    total_nets=list()
    for net in nets:
        total_host = list()
        ip=net[0]
        host=net[1]
        for n in host:
            new_net=subnet(ip,n)
            ip=first_ip( new_net[6][:])
            total_host.append(new_net[:])
        total_nets.append(total_host)

    for i in total_nets:
        print("\nEnc    Dir IP      Prefijo       Mascara          Primera ip           Ultima IP          Broadcast")
        print(
            "--------------------------------------------------------------------------------------------------------")
        for j in i:
            print(j)
        print("--------------------------------------------------------------------------------------------------------")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
