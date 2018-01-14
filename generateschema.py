import csv

def x(f_obj):
    reader = csv.DictReader(f_obj, delimiter=',')
    Name=''
    for line in reader:
        # print line["Name"],line["Property"]
        if Name!=line["Name"]:
            print line["Name"], 'is new'
            # DO SOMETHING FOR THE NEW
            Name=line["Name"]
        print line["Property"]
        # DO THE NEEDED FOR PROPERTY
