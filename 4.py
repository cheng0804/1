class Course:
    def __init__(self, code, name, credits, compulsory, teacher, schedule):
        self.code = code          # 課程代碼
        self.name = name          # 課程名稱
        self.credits = credits    # 學分數
        self.compulsory = compulsory  # 必選修
        self.teacher = teacher    # 任課老師
        self.schedule = schedule  # 上課時間

# 使用建構子建立物件
c1 = Course("CS101", "Introduction to Computer Science", 3, "必修", "Dr. Smith", "Monday 10:00 AM - 12:00 PM")
c2 = Course("ENG202", "English Literature", 4, "選修", "Prof. Johnson", "Wednesday 2:00 PM - 4:00 PM")

# 可以透過物件的屬性來取得相應的資訊
print("課程名稱:", c1.name)
print("任課老師:", c2.teacher)
