"""
The following example demonstrates elif.
It calculates a grade based on test scores
- 80+ gains an A grade,
- 70–79 a B,
- 60–69 a C,
- 50–59 a D,
- and anything else is an F.
"""
if score >= 80:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'