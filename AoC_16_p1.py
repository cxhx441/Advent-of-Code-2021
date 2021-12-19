import unittest
x_to_hex = {'0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'}

with open("AoC_16_input_sample.txt") as f:
    hex_input = f.readline()[:-1]

def hex_input_2_bin(hex_input):
    packet = ''
    for char in hex_input:
        packet += x_to_hex[char]
    return packet

def parse_literal(packet):
    # ID = 4 means packet is a literal value
    binary = ''
    for idx in range(0, len(packet), 5):
        binary += packet[idx+1:idx+5]
        if packet[idx] == '0':
            num_rep = int(binary, 2)
            p_literals.append(num_rep)
            packet = packet[idx + 5:]
            return num_rep, packet

def parse_len_type_0(packet):
    bit_count = int(packet[:15], 2)
    packet = packet[15:]
    target_packet_len = len(packet[bit_count:])
    nums_list = []
    while len(packet) != target_packet_len:
        num_rep, packet = parse_packet(packet)
        nums_list.append(num_rep)
    return nums_list, packet

def parse_len_type_1(packet):
    sub_packet_count = int(packet[:11], 2)
    packet = packet[11:]
    nums_list = []
    for _ in range(sub_packet_count):
        num_rep, packet = parse_packet(packet)
        nums_list.append(num_rep)
    return nums_list, packet

def parse_operator(packet, p_ID):
    p_len_type_ID = int(packet[0])
    packet = packet[1:]
    if p_len_type_ID == 0:
        nums_list, packet = parse_len_type_0(packet)
    elif p_len_type_ID == 1:
        nums_list, packet = parse_len_type_1(packet)
    if p_ID == 0: # sum
        num_rep = 0
        for num in nums_list:
            num_rep += num
    elif p_ID == 1: # product
        num_rep = 1
        for num in nums_list:
            num_rep *= num
    elif p_ID == 2: # min
        num_rep = None
        for num in nums_list:
            if num_rep == None or num < num_rep:
                num_rep = num
    elif p_ID == 3: # max
        num_rep = None
        for num in nums_list:
            if num_rep == None or num > num_rep:
                num_rep = num
    elif p_ID == 5: # greater than
        if nums_list[0] > nums_list[1]:
            num_rep = 1
        else:
            num_rep = 0
    elif p_ID == 6: # less than
        if nums_list[0] < nums_list[1]:
            num_rep = 1
        else:
            num_rep = 0
    elif p_ID == 7: # equal to
        if nums_list[0] == nums_list[1]:
            num_rep = 1
        else:
            num_rep = 0
    return num_rep, packet

def parse_packet(packet):
    p_version = int(packet[:3], 2)
    p_versions.append(p_version)
    p_ID = int(packet[3:6], 2)
    packet = packet[6:]
    #literal
    if p_ID == 4:
        num_rep, packet = parse_literal(packet)
        return num_rep, packet
    #operator
    elif p_ID != 4:
        num_rep, packet = parse_operator(packet, p_ID)
        return num_rep, packet

p_versions = []
p_literals = []
nums = []
packet1 = 'D2FE28' # total 6
packet2 = '38006F45291200' # total 9
packet3 = 'EE00D40C823060' # total 16
packet4 = '8A004A801A8002F478'
packet5 = '620080001611562C8802118E34'
packet6 = 'C0015000016115A2E0802F182340'
packet7 = 'A0016C880162017C3686B18A3D4780'
packet8 = 'C200B40A82'
packet9 = '04005AC33890'
packet10 = '880086C3E88112'
packet11 = 'CE00C43D881120'
packet12 = 'D8005AC2A8F0'
packet13 = 'F600BC2D8F'
packet14 = '9C005AC2F8F0'
packet15 = '9C0141080250320F1802104A08'
packet16 = '005410C99A9802DA00B43887138F72F4F652CC0159FE05E802B3A572DBBE5AA5F56F6B6A4600FCCAACEA9CE0E1002013A55389B064C0269813952F983595234002DA394615002A47E06C0125CF7B74FE00E6FC470D4C0129260B005E73FCDFC3A5B77BF2FB4E0009C27ECEF293824CC76902B3004F8017A999EC22770412BE2A1004E3DCDFA146D00020670B9C0129A8D79BB7E88926BA401BAD004892BBDEF20D253BE70C53CA5399AB648EBBAAF0BD402B95349201938264C7699C5A0592AF8001E3C09972A949AD4AE2CB3230AC37FC919801F2A7A402978002150E60BC6700043A23C618E20008644782F10C80262F005679A679BE733C3F3005BC01496F60865B39AF8A2478A04017DCBEAB32FA0055E6286D31430300AE7C7E79AE55324CA679F9002239992BC689A8D6FE084012AE73BDFE39EBF186738B33BD9FA91B14CB7785EC01CE4DCE1AE2DCFD7D23098A98411973E30052C012978F7DD089689ACD4A7A80CCEFEB9EC56880485951DB00400010D8A30CA1500021B0D625450700227A30A774B2600ACD56F981E580272AA3319ACC04C015C00AFA4616C63D4DFF289319A9DC401008650927B2232F70784AE0124D65A25FD3A34CC61A6449246986E300425AF873A00CD4401C8A90D60E8803D08A0DC673005E692B000DA85B268E4021D4E41C6802E49AB57D1ED1166AD5F47B4433005F401496867C2B3E7112C0050C20043A17C208B240087425871180C01985D07A22980273247801988803B08A2DC191006A2141289640133E80212C3D2C3F377B09900A53E00900021109623425100723DC6884D3B7CFE1D2C6036D180D053002880BC530025C00F700308096110021C00C001E44C00F001955805A62013D0400B400ED500307400949C00F92972B6BC3F47A96D21C5730047003770004323E44F8B80008441C8F51366F38F240'

cur_pack = hex_input_2_bin(packet16)
parse_packet(cur_pack)
total = 0
for p_version in p_versions:
    total += p_version
print(total)
def check_total(packet, expected_total):
    cur_pack = hex_input_2_bin(packet)
    print(cur_pack)
    # print(cur_pack)
    total = 0
    p_versions.clear()
    parse_packet(cur_pack)
    for p_version in p_versions:
        total += p_version
    print(total, expected_total, total == expected_total)

check_total(packet1, 6)
check_total(packet2, 9)
check_total(packet3, 14)
check_total(packet4, 16)
check_total(packet5, 12)
check_total(packet6, 23)
check_total(packet7, 31)

def check_final_num_rep(packet, exp_val):
    cur_pack = hex_input_2_bin(packet)
    print(cur_pack)
    num_rep, packet = parse_packet(cur_pack)
    print(exp_val, ":", num_rep, exp_val == int(num_rep))

check_final_num_rep(packet8, 3)
check_final_num_rep(packet9, 54)
check_final_num_rep(packet10, 7)
check_final_num_rep(packet11, 9)
check_final_num_rep(packet12, 1)
check_final_num_rep(packet13, 0)
check_final_num_rep(packet14, 0)
check_final_num_rep(packet15, 1)
check_final_num_rep(packet16, 1)
