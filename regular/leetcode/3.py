import re
def main():
    s = ".314"
    return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))


if __name__=="__main__":
    print(main())
