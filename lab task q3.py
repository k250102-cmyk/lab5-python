import json
record=[{"model_name":"Ai model", "accuracy":60, "precision":0.4, "recall":3,"F1-score":45},{"model_name":"business model", "accuracy":20, "precision":0.6, "recall":2,"F1-score":49}]
file=open("model_results.json","w")
json.dump(record,file)
print("model created successfully")
file=open("model_results.json","r")
read_file=json.load(file)
print(read_file)
highest_accuracy=0
for model in record:
    if model["accuracy"]>highest_accuracy:
        highest_accuracy=model["accuracy"]
        
print("the model with highest accuracy",highest_accuracy)
#model with highest F1-score
highest_score=0
for model in record:
    if model["F1-score"]>highest_score:
        highest_score=model["F1-score"]

print("the model with highest score:",highest_score)
file=open("model_results.json","a")
new_record={"model_name":"cyber model", "accuracy":30, "precision":0.7, "recall":2,"F1-score":89}
record.append(new_record)
file.close()

file = open("model_results.json", "w")

json.dump(record, file, indent=4)

file.close()

print("New record added successfully")
    #update a new record in a file
target_model="Ai model"
file=open("model_results.json","r")
read_file=json.load(file)
found=False
for model in record:
    if model["model_name"]==target_model:
        model["accuracy"] = int(input("Enter new accuracy: "))
        model["precision"] = float(input("Enter new precision: "))
        model["recall"] = int(input("Enter new recall: "))
        model["F1_score"] = int(input("Enter new F1-score: "))

        found = True
        break

if found==True:
    print("updated successfully")
else:
    print("cannot update the records because they don't exists")

#remove a model&#39;s result when required.
target_name="business_model"
for model in record:
    if model["model_name"]==target_name:
        record.remove(model)

print("deleted successfully")
file = open("model_results.json", "w")

json.dump(record, file, indent=4)

file.close()
file=open("model_results.json","r")
read_file=json.load(file)
print(read_file)
print("JSON file updated.")