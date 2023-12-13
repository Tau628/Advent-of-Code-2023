#Advent of Code 2023, Day 6, Part 1

output_prod = 1

times = input()
distances = input()

times = list(map(lambda x: x.strip(), times.split()))
times = times[1:]
times = list(map(int, times))

distances = list(map(lambda x: x.strip(), distances.split()))
distances = distances[1:]
distances = list(map(int, distances))

for race in range(len(times)):
    possible_timings = 0
    for t in range(1, times[race]):
        speed = t
        traveled = speed*(times[race]-t)

        if traveled > distances[race]:
            possible_timings += 1

    output_prod *= possible_timings

print(output_prod)
