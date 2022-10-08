'''
https://adventofcode.com/2021/day/16
'''
DAY = 16


from utils import *
from functools import reduce
from operator import mul


VERSION_SUM = 0


def parser(test=False):
    return Input(DAY, 2021, test=test)[0]


def test_decoder():
    global VERSION_SUM
    
    # Part 1
    VERSION_SUM = 0
    decoder(hex_decoder('8A004A801A8002F478')) # 16
    assert VERSION_SUM == 16
    VERSION_SUM = 0
    decoder(hex_decoder('620080001611562C8802118E34')) # 12
    assert VERSION_SUM == 12
    VERSION_SUM = 0
    decoder(hex_decoder('C0015000016115A2E0802F182340')) # 23
    assert VERSION_SUM == 23
    VERSION_SUM = 0
    decoder(hex_decoder('A0016C880162017C3686B18A3D4780')) # 31
    assert VERSION_SUM == 31

    # Part 2
    assert decoder(hex_decoder('C200B40A82'))[0] == 3
    assert decoder(hex_decoder('04005AC33890'))[0] == 54
    assert decoder(hex_decoder('880086C3E88112'))[0] == 7
    assert decoder(hex_decoder('CE00C43D881120'))[0] == 9
    assert decoder(hex_decoder('D8005AC2A8F0'))[0] == 1
    assert decoder(hex_decoder('F600BC2D8F'))[0] == 0
    assert decoder(hex_decoder('9C005AC2F8F0'))[0] == 0
    assert decoder(hex_decoder('9C0141080250320F1802104A08'))[0] == 1


def hex_decoder(input):
    val = ''
    for h in input:
        val += f'{int(h, 16):04b}'
    return val 


def decoder(binary_input):
    # print(f'{binary_input=}')
    
    # Version
    V = int(binary_input[:3], 2)
    # print(f'{V=}')

    global VERSION_SUM
    VERSION_SUM += V
    
    # Type
    T = int(binary_input[3:6], 2)
    # print(f'{T=}')

    if T == 4: # Literal value
        s = 6
        literal_binary = ''
        while True:
            block = binary_input[s:s+5]
            literal_binary += binary_input[s+1:s+5]
            s += 5
            if block[0] == '0':
                break

        literal_int = int(literal_binary, 2)
        # print(f'{literal_int=}')
        return literal_int, s

    else: # Operator: retrieve operands
        packets = []

        length_type_ID = binary_input[6]
        # print(f'{length_type_ID=}')

        if length_type_ID == '0': # Length of sub-packets
            supbacket_length = int(binary_input[7:7+15], 2)
            # print(f'{supbacket_length=}')

            f = 7+15
            while  binary_input[f:] and int(binary_input[f:]) and (supbacket_length > 0):
                packet, fe = decoder(binary_input[f:f+supbacket_length])
                packets.append(packet)
                f += fe
                supbacket_length -= fe

        if length_type_ID == '1': # Number of sub-packets
            supbacket_number = int(binary_input[7:7+11], 2)
            # print(f'{supbacket_number=}')
            f = 7 + 11
            fe = 0
            for _ in range(supbacket_number):
                packet, fe = decoder(binary_input[f:])
                packets.append(packet)
                f += fe

    if T == 0: # Sum
        return sum(packets), f
    elif T == 1: # Product
        return reduce(mul, packets), f
    elif T == 2: # Minimum
        return min(packets), f
    elif T ==3: # Maximum
        return max(packets), f
    elif T == 5: # Greater than (returns 1 or 0)
        return int(packets[0] > packets[1]), f
    elif T == 6: # Less than (returns 1 or 0)
        return int(packets[0] < packets[1]), f
    elif T == 7: # Equal to (returns 1 or 0)
        return int(packets[0] == packets[1]), f

    return None, f


def part1(input):
    global VERSION_SUM
    VERSION_SUM = 0
    decoder(hex_decoder(parser()))
    return VERSION_SUM


def part2(input):
    return decoder(hex_decoder(parser()))[0]
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test_decoder()
    main()