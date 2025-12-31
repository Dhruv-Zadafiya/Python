marks = {
     "Maths": 80,
     "Science": 90,
     "Social Science": 86
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Maths": 88, "English": 90})
print(marks)
print(marks.get("Dhruv")) 
print(marks.get("Maths")) 

print(marks.get("Dhruv3"))
print(marks.popitem()) 

 