import sys


def x_to_y_for_mapping(x, mapping):
    for map_range in mapping:
        if x in map_range[0]:
            return x + map_range[1].start - map_range[0].start
    return x


def transform(r, diff):
    return range(r.start + diff, r.stop + diff)


def convert_one_interval(interval_to_convert, conversion):
    unconverted = [interval_to_convert]
    converted = []
    for mapping in conversion:
        m = mapping[0]
        new_unconverted = []
        for c in unconverted:
            if (c.start < m.start and c.stop < m.start) or (c.start > m.stop and c.stop > m.stop):
                # There are no intersections
                new_unconverted.append(c)
            else:
                if c.start < m.start:
                    new_unconverted.append(range(c.start, m.start))
                converted.append(
                    transform(range(max(c.start, m.start), min(c.stop, m.stop)), mapping[1].start - mapping[0].start))
                if c.stop > m.stop:
                    new_unconverted.append(range(m.stop, c.stop))
        unconverted = new_unconverted
    converted += unconverted
    return converted


def do_convert_range(intervals_to_convert, conversion):
    # take each range, which will be different things
    converted_intervals = []
    for interval in intervals_to_convert:
        converted_intervals += convert_one_interval(interval, conversion)
    return converted_intervals


def main():
    with open("day5.in") as data:
        data = data.read()
        seeds = data.split("\n")[0].strip().split(" ")[1:]
        seeds = [int(seed) for seed in seeds]
        conversions = data.split("\n\n")[1:]
        conversions = [mapping.split("\n")[1:] for mapping in conversions]
        conversions = [[[int(j) for j in i.strip().split(" ")] for i in conversion] for conversion in conversions]
        conversions = [
            [[range(one_map[1], one_map[1] + one_map[2]), range(one_map[0], one_map[0] + one_map[2])] for
             one_map in conversion] for conversion in conversions]

        # Part 1
        min_location = sys.maxsize
        for seed in seeds:
            x = seed
            for conversion in conversions:
                x = x_to_y_for_mapping(x, conversion)
            min_location = min(x, min_location)
        print(min_location)

        # Part 2
        final_ranges = []
        seed_ranges = list(zip(seeds[::2], seeds[1::2]))
        for seed_range in seed_ranges:
            x = [range(seed_range[0], seed_range[0] + seed_range[1])]
            for conversion in conversions:
                x = do_convert_range(x, conversion)
            final_ranges += x
        min_final = sys.maxsize
        for r in final_ranges:
            min_final = min(min_final, r.start)
        print(min_final)


if __name__ == '__main__':
    main()
