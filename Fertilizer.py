#Advent of Code 2023, Day 5, Part 2

class conversion_map:
  def __init__(self, destination_start, source_start, range_length):
    self.destination_start = destination_start
    self.source_start = source_start
    self.range_length = range_length


def transform(source_value, conv_maps):
    for cMap in conv_maps:
        diff = source_value - cMap.source_start
        if diff >= 0 and diff < cMap.range_length:
            return cMap.destination_start + diff

    return source_value

def transform_range(source_range, conv_maps):
    for cMap in conv_maps:
        diff = source_value - cMap.source_start
        if diff >= 0 and diff < cMap.range_length:
            return cMap.destination_start + diff

    return source_value


output_sum = 0

#First line
line = input()
_, nums = line.split(": ")
seeds = list(map(int, nums.split()))

#Blank line
_ = input()

#Seed-Soil Header
_ = input()


seed2soil = []
while(True):
    line = input()
    if line.upper() == "":
        _ = input()
        break
    nums = list(map(int, line.split()))
    seed2soil.append( conversion_map(nums[0], nums[1], nums[2]) )

soil2fertilizer = []
while(True):
    line = input()
    if line.upper() == "":
        _ = input()
        break
    nums = list(map(int, line.split()))
    soil2fertilizer.append( conversion_map(nums[0], nums[1], nums[2]) )

fertilizer2water = []
while(True):
    line = input()
    if line.upper() == "":
        _ = input()
        break
    nums = list(map(int, line.split()))
    fertilizer2water.append( conversion_map(nums[0], nums[1], nums[2]) )

water2light = []
while(True):
    line = input()
    if line.upper() == "":
        _ = input()
        break
    nums = list(map(int, line.split()))
    water2light.append( conversion_map(nums[0], nums[1], nums[2]) )

light2temperature = []
while(True):
    line = input()
    if line.upper() == "":
        _ = input()
        break
    nums = list(map(int, line.split()))
    light2temperature.append( conversion_map(nums[0], nums[1], nums[2]) )

temperature2humidity = []
while(True):
    line = input()
    if line.upper() == "":
        _ = input()
        break
    nums = list(map(int, line.split()))
    temperature2humidity.append( conversion_map(nums[0], nums[1], nums[2]) )

humidity2location = []
while(True):
    line = input()
    if line.upper() == "":
        _ = input()
        break
    nums = list(map(int, line.split()))
    humidity2location.append( conversion_map(nums[0], nums[1], nums[2]) )


my_locations = []

it = iter(seeds)
seeds = list(zip(it, it))
for (seed_start, seed_range) in seeds:

    print(f"Seed: {seed_start}, {seed_range}")

    for seed in range(seed_start, seed_start+seed_range):
        
        soil        = transform(seed,        seed2soil)
        fertilizer  = transform(soil,        soil2fertilizer)
        water       = transform(fertilizer,  fertilizer2water)
        light       = transform(water,       water2light)
        temperature = transform(light,       light2temperature)
        humidity    = transform(temperature, temperature2humidity)
        location    = transform(humidity,    humidity2location)
        my_locations.append(location)

print(min(my_locations))
