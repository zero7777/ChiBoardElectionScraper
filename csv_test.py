import csv

def writeCSV(data, file_name):

	return

if __name__ == "__main__":
    f = open('test.csv','w')
    w = csv.writer(f,delimiter='|')
    w.writerows([["a","b","c"],[1,2,3]])
