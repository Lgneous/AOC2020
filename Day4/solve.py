valid = {
    "byr": lambda x: len(x) == 4 and int(x) in range(1920, 2003),
    "iyr": lambda x: len(x) == 4 and int(x) in range(2010, 2021),
    "eyr": lambda x: len(x) == 4 and int(x) in range(2020, 2031),
    "hgt": lambda x: x.endswith("cm") * (int(x[:-2]) in range(150, 194)) + x.endswith("in") * (int(x[:-2]) in range(59, 77)),
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda x: len(x) == 9 and int(x),
    "hcl": lambda x: x.startswith("#") and all(x in "0123456789abcdef" for x in x[1:]),
    "cid": lambda _: True
}

def solve(content, valid):
    inputs = content.split("\n\n")
    count = 0
    for passport in inputs:
        fields = passport.split()
        keys = set()
        for field in fields:
            key, value = field.split(":")
            try:
                if valid.get(key, lambda _: False)(value):
                    keys.add(key)
            except ValueError:
                pass
        count += keys - {'cid'} == {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return count


def part1(input_file):
    input_file.seek(0)
    class FakeValid:
        def get(self, *args, **kwargs):
            return lambda _: True
    return solve(input_file.read(), FakeValid())


def part2(input_file):
    input_file.seek(0)
    return solve(input_file.read(), valid)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            print(part1(f))
            print(part2(f))
