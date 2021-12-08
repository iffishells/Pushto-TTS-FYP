import pandas as pd
def update_database_with_new_words(updated_words_list):
    
    print("update_database_with_new_words : Called")
    file_path = "Datasets/Pastho-dictionary(pos).xlsx"
    
    data = pd.read_excel(file_path)
    
    back_dict = data.to_dict(orient='list')
    
    
    for index in range(len(updated_words_list)):
        
        if updated_words_list[index][0] not in back_dict['token']:
            back_dict["token"].append(updated_words_list[index][0])
            back_dict["Adjective"].append(updated_words_list[index][1])
        else:
            print(updated_words_list[index][0]+ " already in the database")
        
    data = pd.DataFrame(data = back_dict)
    data.to_excel(file_path)
    return data.tail
    
    