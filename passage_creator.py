
with open("passages.txt", 'r') as file:
    my_list =file.readlines()

edited_passage_list = []
for n in my_list:
    if n != '\n':
        n.replace('\n', "")
        edited_passage_list.append(n[:-1])

clean_passage_list = edited_passage_list