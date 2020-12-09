import sys


def pair_sum(arr, target):
    seen = set()
    for i in arr:
        x = target - i
        if x in seen:
            return True
        seen.add(i)
    return False


def subarray_sum(arr, target):
    for i in range(len(arr)):
        sum_ = arr[i]
        for j in range(i + 1, len(arr)):
            sum_ += arr[j]
            if sum_ > target:
                break
            if sum_ == target:
                return min(arr[i:j]) + max(arr[i:j])
    return -1


def part1(input_file):
    input_file.seek(0)
    inputs = list(map(int, f.read().split()))
    for i in range(25, len(inputs)):
        if not pair_sum(inputs[i - 25: i], inputs[i]):
            return inputs[i]


def part2(input_file):
    input_file.seek(0)
    inputs = list(map(int, f.read().split()))
    return subarray_sum(inputs, part1(input_file))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            print(part1(f))
            print(part2(f))
