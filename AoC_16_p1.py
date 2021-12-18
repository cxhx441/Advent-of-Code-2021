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

def parse_literal_packet(literal_packet):
    # ID = 4 means packet is a literal value
    binary = ''
    for idx in range(0, len(literal_packet), 5):
        # print(idx, ': ', literal_packet[idx])
        binary += literal_packet[idx+1:idx+5]
        if literal_packet[idx] == '0':
            # print(binary)
            num_rep = int(binary, 2)
            p_literals.append(num_rep)
            # leading_zero = len(literal_packet) - len(literal_packet)%4 + 1

            new_start = idx + 5
            return num_rep, new_start

def parse_packet(packet):
    p_version = int(packet[:3], 2)
    p_versions.append(p_version)
    p_ID = int(packet[3:6], 2)
    if p_ID == 4:
       return parse_literal_packet(packet[6:])

    elif p_ID != 4:
        #operator
        p_len_type_ID = int(packet[6])
        if p_len_type_ID == 0:
            bit_count = int(packet[7:7+15], 2)
            sub_packets = packet[7+15:]
            while bit_count != 0:
                num_rep, idx_end = parse_packet(sub_packets)
                idx_end += 6
                sub_packets = sub_packets[idx_end:]
                bit_count -= idx_end
        elif p_len_type_ID == 1:
            sub_packet_count = int(packet[7:7+11], 2)
            sub_packets = packet[7+11:]
            for _ in range(sub_packet_count):
                num_rep, idx_end = parse_packet(sub_packets)
                idx_end += 6
                sub_packets = sub_packets[idx_end:]




p_versions = []
p_literals = []
packet1 = 'D2FE28' # total 6
packet2 = '38006F45291200' # total 9
packet3 = 'EE00D40C823060' # total 16
packet4 = '8A004A801A8002F478'
packet5 = '620080001611562C8802118E34'
packet6 = 'C0015000016115A2E0802F182340'
packet7 = 'A0016C880162017C3686B18A3D4780'

# cur_pack = hex_input_2_bin(packet2)
# print(cur_pack)
# parse_packet(cur_pack)
# total = 0
# for p_version in p_versions:
#     total += p_version

def check_total(packet, expected_total):
    cur_pack = hex_input_2_bin(packet)
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
check_total(packet5, 23)
check_total(packet6, 31)
