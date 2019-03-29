

def read(filename):
    fields = []
    with open(filename, "r") as file:
        line_list = file.readlines()
        for line in line_list:
            var_fields = line.split(",")
            fields.append(var_fields)
        return fields
