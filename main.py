from generate_excel import GenerateExcel


def dec_to_bin(IP):
    bin_list = list()
    for i in IP:
        bin_list.append("{:b}".format(i))
    return complete_octeto(bin_list[:])


def complete_octeto(bin_ip):
    bin_list = bin_ip[:]
    octeto = ""
    for i in range(len(bin_list)):
        if len(bin_list[i]) < 8:
            for j in range(8 - len(bin_list[i])):
                octeto += "0"
            octeto += bin_list[i]
            bin_list[i] = octeto
            octeto = ""
    return bin_list


def bin_to_dec(bin_ip):
    bin_ip = complete_octeto(bin_ip[:])  # TODO
    dec_ip = list()
    dec_ip.append(int(bin_ip[0], 2))
    dec_ip.append(int(bin_ip[1], 2))
    dec_ip.append(int(bin_ip[2], 2))
    dec_ip.append(int(bin_ip[3], 2))

    return dec_ip


def split_ip(IP):
    new_ip = IP.split(".")
    return new_ip


def string_bin_ip(IP_bin):
    string_bin = ""
    for i in IP_bin:
        string_bin += i
    return string_bin


def hosts_formule(num_hosts, formule=True):
    flag = 2
    if formule is not True:
        flag = 0
    n_hosts = 0
    idx = 0
    while  n_hosts<num_hosts:   
            idx += 1
            n_hosts = pow(2, idx) - flag        
    return n_hosts, idx


def calc_mask(n):
    string_mask = ""
    for i in range(32):
        if i < 32 - n:
            string_mask += "1"
        else:
            string_mask += "0"
    mask = list()
    mask.append(string_mask[:8])
    mask.append(string_mask[8:16])
    mask.append(string_mask[16:24])
    mask.append(string_mask[24:32])
    return mask


def first_ip(ip):
    newip = ip
    if ip[3] < 255:
        newip[3] = ip[3] + 1
    elif ip[3] == 255 and ip[2] < 255:
        newip[2] = ip[2] + 1
        newip[3] = 0
    elif ip[3] == 255 and ip[2] == 255 and ip[1] < 255:
        newip[1] = ip[2] + 1
        newip[2] = 0
        newip[3] = 0
    return newip


def last_ip(ip):
    newip = ip
    if ip[3] > 0:
        newip[3] = ip[3] - 1
    elif ip[3] == 0 and ip[2] > 0:
        newip[2] = ip[2] - 1
        newip[3] = 255
    elif ip[3] == 0 and ip[2] == 0 and ip[1] > 0:
        newip[1] = ip[2] + 1
        newip[2] = 255
        newip[3] = 255
    return newip


def string_IP_to_IP(string_IP):
    dir_ip = list()
    dir_ip.append(string_IP[:8])
    dir_ip.append(string_IP[8:16])
    dir_ip.append(string_IP[16:24])
    dir_ip.append(string_IP[24:32])
    return dir_ip


def broadcast(bIP, n):
    bynary_string_ip = string_bin_ip(bIP)
    brcast = bynary_string_ip[: len(bynary_string_ip) - n]
    for i in range(n):
        brcast += "1"

    return bin_to_dec(complete_octeto(string_IP_to_IP(brcast)))

def wildcard(mask):
    wildcard=list()
    for octeto in mask:
        wildcard.append(255-octeto)
    
    return wildcard



# Press the green button in the gutter to run the script.
if __name__ == "__main__":

    # ejercicio1
    # LAN

    #nets = [[[42,168, 16, 0],[135,125,120,110,110,90,88,88,70,60,60,45,44,40,30,22,14]]]

    # nets = [
    #    # [[33,0,8,0],[  672,365,214,20,4]]
    #      [[33, 0, 8,0],[135,125,110,90,88,70,40,14,4]],
    #      [[33, 0, 12,0],[120,110,60,45,30,4]],
    #      [[33, 0 , 14,0],[88,60,44,22,4]],
    #     [[33, 0 , 15,0],[20]]
    # ]

    # WAN
    #nets=[[[33,0,15,108],[2,2,2]]]

    total_nets = list()
    for net in nets:
        total_host = list()
        ip = net[0]
        host = net[1]
        for n in host:
            new_net = subnet(ip, n,True)
            aux = [int(x) for x in (new_net[6].split("."))]
            ip = first_ip(aux[:])
            total_host.append(new_net[:])
        total_nets.append(total_host)

    excel = GenerateExcel()
    columns = [
            "Encontrados",
            "Dir IP",
            "Prefijo",
            "Mascara",
            "Primera ip",
            "Ultima IP",
            "Broadcast",
            "wildcard"
        ]
    excel.columns = columns
    name = "prueba-"
    idx = 0
    for i in total_nets:
        idx += 1
        
        rows = list()
        for j in i:
            rows.append(j)
   
        
        excel.rows = rows
        excel.generate(name + str(idx))
    excel.save_book()
