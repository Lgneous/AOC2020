import sys


def swap(instr):
    swap = {"nop": "jmp", "jmp": "nop"}
    instr[0] = swap[instr[0]]


def reset(instr):
    for ins in instr:
        ins[2] = False


def run(instr):
    i = 0
    acc = 0
    while i < len(instr):
        ins, n, has_ran = instr[i]
        if has_ran:
            return False, acc
        instr[i][2] = True
        if ins == "nop":
            i += 1
        elif ins == "jmp":
            i += n
        elif ins == "acc":
            acc += n
            i += 1
    return True, acc


def part1(input_file):
    input_file.seek(0)
    inputs = input_file.read().strip().split("\n")
    instr = []
    for input in inputs:
        ins, n = input.split()
        instr.append([ins, int(n), False])
    return run(instr)[1]


def part2(input_file):
    input_file.seek(0)
    inputs = input_file.read().strip().split("\n")
    instr = []
    for input in inputs:
        ins, n = input.split()
        instr.append([ins, int(n), False])
    for i in instr:
        reset(instr)
        if i[0] in {"nop", "jmp"}:
            swap(i)
            b, n = run(instr)
            swap(i)
            if b:
                return n


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            print(part1(f))
            print(part2(f))
