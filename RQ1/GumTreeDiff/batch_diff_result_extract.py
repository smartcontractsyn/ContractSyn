import numpy as np

dirNamePatterns = ["PA", "SPA", "SECPA", "SA"]
batch_diff_result_filename = "batch_diff_result.txt"

output_matrix = [['Contract', 'Total', 'Move', 'Update', 'Insert', 'Delete', 'Tree-Insert', 'Tree-Delete']]

table_tag = []
for i in range(len(output_matrix[0])):
    table_tag.append("----")
output_matrix.append(table_tag)

column_tags = ["Total Num of Actions",
                "Move Num",
                "Update Num",
                "Insert Num",
                "Delete Num",
                "Tree Insert Num",
                "Tree Delete Num"]

with open(batch_diff_result_filename, "r", encoding='utf-8') as ifile:
    curContract = ""
    lines = ifile.readlines()
    cnt = 0
    for line in lines:
        line = line.strip("\n")
        line = line.strip(b'\xef\xbb\xbf'.decode('utf-8'))
        for dn in dirNamePatterns:
            if line.startswith(dn): 
                curContract = line
                output_matrix.append([curContract])
                break
        for tag in column_tags:
            if tag in line:
                output_matrix[-1].append(line.split(" ")[-1])
                break
        cnt+=1


for line in output_matrix:
    print("| " + " | ".join(line) + " |")

# print(np.matrix(output_matrix))

    