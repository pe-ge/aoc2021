from math import ceil
from functools import reduce

packet = "820D4A801EE00720190CA005201682A00498014C04BBB01186C040A200EC66006900C44802BA280104021B30070A4016980044C800B84B5F13BFF007081800FE97FDF830401BF4A6E239A009CCE22E53DC9429C170013A8C01E87D102399803F1120B4632004261045183F303E4017DE002F3292CB04DE86E6E7E54100366A5490698023400ABCC59E262CFD31DDD1E8C0228D938872A472E471FC80082950220096E55EF0012882529182D180293139E3AC9A00A080391563B4121007223C4A8B3279B2AA80450DE4B72A9248864EAB1802940095CDE0FA4DAA5E76C4E30EBE18021401B88002170BA0A43000043E27462829318F83B00593225F10267FAEDD2E56B0323005E55EE6830C013B00464592458E52D1DF3F97720110258DAC0161007A084228B0200DC568FB14D40129F33968891005FBC00E7CAEDD25B12E692A7409003B392EA3497716ED2CFF39FC42B8E593CC015B00525754B7DFA67699296DD018802839E35956397449D66997F2013C3803760004262C4288B40008747E8E114672564E5002256F6CC3D7726006125A6593A671A48043DC00A4A6A5B9EAC1F352DCF560A9385BEED29A8311802B37BE635F54F004A5C1A5C1C40279FDD7B7BC4126ED8A4A368994B530833D7A439AA1E9009D4200C4178FF0880010E8431F62C880370F63E44B9D1E200ADAC01091029FC7CB26BD25710052384097004677679159C02D9C9465C7B92CFACD91227F7CD678D12C2A402C24BF37E9DE15A36E8026200F4668AF170401A8BD05A242009692BFC708A4BDCFCC8A4AC3931EAEBB3D314C35900477A0094F36CF354EE0CCC01B985A932D993D87E2017CE5AB6A84C96C265FA750BA4E6A52521C300467033401595D8BCC2818029C00AA4A4FBE6F8CB31CAE7D1CDDAE2E9006FD600AC9ED666A6293FAFF699FC168001FE9DC5BE3B2A6B3EED060"

sum_version_numbers = 0


def to_binary(hex_number):
    binary = str(bin(int(hex_number, 16))[2:])
    num_leading_zeros = len(hex_number) * 4 - len(binary)
    return f"{'0' * num_leading_zeros}{binary}"


def op(type_id, numbers):
    if type_id == 0:
        return sum(numbers)
    elif type_id == 1:
        return reduce(lambda x, y: x * y, numbers)
    elif type_id == 2:
        return reduce(lambda x, y: min(x, y), numbers)
    elif type_id == 3:
        return reduce(lambda x, y: max(x, y), numbers)
    elif type_id == 5:
        return 1 if numbers[0] > numbers[1] else 0
    elif type_id == 6:
        return 1 if numbers[0] < numbers[1] else 0
    elif type_id == 7:
        return 1 if numbers[0] == numbers[1] else 0


def process_subpacket(subpacket_bin):
    global sum_version_numbers
    if subpacket_bin == "" or subpacket_bin is None:
        return None, None

    sum_version_numbers += int(subpacket_bin[:3], 2)
    type_id = int(subpacket_bin[3:6], 2)

    if type_id == 4:
        idx = 6
        number = []
        while True:
            next_bit = subpacket_bin[idx]
            idx += 1
            number.append(subpacket_bin[idx : idx + 4])
            idx += 4
            if next_bit == "0":
                break

        return int("".join(number), 2), subpacket_bin[idx:]

    else:
        length_type_id = subpacket_bin[6]
        if length_type_id == "0":
            total_length_in_bits = int(subpacket_bin[7 : 7 + 15], 2)
            another_subpacket, subpacket_bin = (
                subpacket_bin[7 + 15 : 7 + 15 + total_length_in_bits],
                subpacket_bin[7 + 15 + total_length_in_bits :],
            )
            numbers = []
            while True:
                number, another_subpacket = process_subpacket(another_subpacket)
                numbers.append(number)
                if another_subpacket is None or another_subpacket == "":
                    return op(type_id, numbers), subpacket_bin
        else:
            number_of_subpackets = int(subpacket_bin[7 : 7 + 11], 2)
            another_subpacket = subpacket_bin[7 + 11 :]
            numbers = []
            for _ in range(number_of_subpackets):
                number, another_subpacket = process_subpacket(another_subpacket)
                numbers.append(number)

            return op(type_id, numbers), another_subpacket


packet_bin = to_binary(packet)

result, _ = process_subpacket(packet_bin)

print(sum_version_numbers)
print(result)
