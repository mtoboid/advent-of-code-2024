from pathlib import Path

class Day1:
    """Advent of code 2024 day 1"""

    @staticmethod
    def run() -> None:
        print("Running day 1...")

        file = Path('./days/day01/input')
        with file.resolve().open() as f:
            data = f.read().split('\n')

        listA: [int] = []
        listB: [int] = []

        for pair in data:
            if pair != "":
                a, b = pair.split()
                listA.append(int(a))
                listB.append(int(b))

        listA.sort()
        listB.sort()


        # Part 1
        listSum: [int] = []

        for i in range(len(listA)):
            listSum.append(abs(listA[i] - listB[i]))

        print('Total diffs: ', sum(listSum))


        # Part 2
        similarityList: [int] = []
        startIdxB: int = 0

        for ia in range(len(listA)):
            count: int = 0
            while startIdxB < len(listB) & listB[startIdxB] < listA[ia]:
                startIdxB+=1
            for ib in range(startIdxB, len(listB)):
                if listB[ib] == listA[ia]:
                    count+=1
                if listB[ib] > listA[ia]:
                    similarityList.append(listA[ia] * count)
                    break

        print('Overall similarity score: ', sum(similarityList))

