class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students_left = len(students)
        
        while students_left > 0:
            if students[0] == sandwiches[0] and students_left:
                students.pop(0)
                sandwiches.pop(0)
                students_left = len(students)
            else:
                student = students.pop(0)
                students.append(student)
                students_left -= 1
        return len(students)