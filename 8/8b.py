from copy import copy


def rev_mapping(mapping):
    reved_mapping = {}
    for key, val in mapping.items():
        if type(val) is list:
            reved_mapping[val[0]] = key
        else:
            reved_mapping[val] = key
    return reved_mapping


ORIG_SEGMENTS = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

REV_ORIG_SEGMENTS = rev_mapping(ORIG_SEGMENTS)


def verify_signals(signals, mapping):
    used = set()
    for signal in signals:
        mapped_signal = ""
        for char in signal:
            mapped_signal += mapping[char][0]
        used.add("".join(sorted(mapped_signal)))

    return used == set(ORIG_SEGMENTS.values())


def get_segments(signals):
    mapping = {x: list("abcdefg") for x in "abcdefg"}

    # handle segment "1"
    mapping["c"] = []
    mapping["f"] = []
    for signal in signals:
        signal_1 = signal
        if len(signal) == 2:
            for char in signal:
                for char_to_remove in "abdeg":
                    mapping[char_to_remove].remove(char)
                mapping["c"].append(char)
                mapping["f"].append(char)
            break

    # handle segment "7"
    for signal in signals:
        if len(signal) == 3:
            for char in signal:
                if char in signal_1:
                    continue
                mapping["a"] = [char]
                for char_to_remove in "bcdefg":
                    if char in mapping[char_to_remove]:
                        mapping[char_to_remove].remove(char)
                break

    # handle segment "4"
    for signal in signals:
        if len(signal) == 4:
            for char in signal:
                for char_to_remove in "aeg":
                    if char in mapping[char_to_remove]:
                        mapping[char_to_remove].remove(char)

                for char_to_keep in "bcdf":
                    mapping[char_to_keep] = list(
                        set(mapping[char_to_keep]).intersection(signal)
                    )

    # guess the rest
    for char_11, char_12 in zip(mapping["b"], reversed(mapping["b"])):
        for char_21, char_22 in zip(mapping["c"], reversed(mapping["c"])):
            for char_31, char_32 in zip(mapping["e"], reversed(mapping["e"])):
                mapping_copy = mapping.copy()
                mapping_copy["b"] = [char_11]
                mapping_copy["d"] = [char_12]
                mapping_copy["c"] = [char_21]
                mapping_copy["f"] = [char_22]
                mapping_copy["e"] = [char_31]
                mapping_copy["g"] = [char_32]
                mapping_copy = rev_mapping(mapping_copy)
                if verify_signals(signals, mapping_copy):
                    return mapping_copy


result = 0
for line in open("input.txt").read().split("\n")[:-1]:
    signals, numbers = line.split(" | ")
    segments = get_segments(signals.split(" "))
    final_number = ""
    for number in numbers.split(" "):
        mapped_number = ""
        for char in number:
            mapped_number += segments[char]

        final_number += str(REV_ORIG_SEGMENTS["".join(sorted(mapped_number))])

    result += int(final_number)

print(result)
