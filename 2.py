class Student:
    def __init__(self, id, name, major):
        self._id = id
        self._name = name
        self._major = major
 
s1 = Student('STUST001', '大B', '資工')
print("學生s1姓名=",s1._name)
print("學生s1學號=",s1._id)
print("學生s1科系=",s1._major)
s2 = Student('STUST002', '大C', '資工')
print("學生s2姓名=",s2._name)
print("學生s2學號=",s2._id)
print("學生s2科系=",s2._major)
s3 = Student('4B1G0175', '林泳成', '資工')
print("學生s3姓名=",s3._name)
print("學生s3學號=",s3._id)
print("學生s3科系=",s3._major)