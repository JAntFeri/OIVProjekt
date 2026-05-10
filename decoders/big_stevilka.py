def base256_to_int(numbers):
    total = 0
    for index, value in enumerate(reversed(numbers)):
        total += value * (256 ** index)
    return total

def izracun_ostankov(stevilka):
    modul1 = 4722366482869645213697
    modul2 = 4722366482869645213709
    modul3 = 4722366482869645213717

    ostanek1 = stevilka % modul1
    ostanek2 = stevilka % modul2
    ostanek3 = stevilka % modul3

    print(f"Ostanek 1: {ostanek1}")
    print(f"Ostanek 2: {ostanek2}")
    print(f"Ostanek 3: {ostanek3}")

my_numbers = [115, 117, 112, 101, 114, 32, 107, 117, 108, 32, 115, 107, 114, 105, 118, 110, 111, 32, 115, 112, 111, 114, 111, 99, 105, 108, 111]
result = base256_to_int(my_numbers)

print(f"The result is: {result}")

izracun_ostankov(result)