class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        0 -> c
        1 -> s
        """
        cycle = 0
        while len(students) > 0:
            print(f"Cycle: {cycle}, students: {students}, sandwiches: {sandwiches}")
            if cycle >= len(students):
                return len(students)
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                cycle = 0
            else:
                pref = students.pop(0)
                students.append(pref)
                cycle += 1
        return 0