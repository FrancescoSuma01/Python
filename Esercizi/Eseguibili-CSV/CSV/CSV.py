from CSVLib import CSV

def main():
    csv = CSV("esempio.csv")
    r = getRowsCount()

    val = csv.getCell(1,1)

    print(csv)
    print(val)

if __name__=="__main__":
    main()