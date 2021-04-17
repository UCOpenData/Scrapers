
def main():
    f = open('raw.txt', 'r')
    content = f.read()
    x = content.split('\n')
    for xx in x:
        print("\"" + xx.split('>')[1].split('<')[0].split(" - ")[0] + "\",")
    for xx in x:
        print("\"" + xx.split('>')[1].split('<')[0].split(" - ")[1] + "\",")
main()