import re


def main():
    runEjemplo1()
    runEjemplo2()
    runEjemplo3()

def runEjemplo1():
    patter = r"ab*"
    palabras = ["a", "ab", "abbb", "abab", "b", ""]
    for p in palabras:
        res = re.fullmatch(patter, p)
        print(f"{p} -> {bool(res)}")

def runEjemplo2():
    regex = "[TO][0-9]{3}"
    list = ["T001", "O120", "T01", "X001", "T0001"]
    for codigo in list:
        res = re.match(regex, codigo)
        print(f"{codigo} => {bool(res)}")

def runEjemplo3():
    patter = "Sensores: T001 reporta 23.5 C; O001 reporta 12 PERSONAS; T002 reporta -2 C"
    regex = r"([TO][0-9]{3})"
    while True:
        res = re.search(regex, patter)
        if res is None:
            break
        print(f"Se encontró: {res.group(1)}")
        patter = patter[res.end():]

if __name__ == "__main__":
    main()