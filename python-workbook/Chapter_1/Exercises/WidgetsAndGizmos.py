"""
file:WidgetsAndGizmos.py
------------------------
This program reads the number of widgets and the number of gizmos from the user.
Then program should compute and display the total weight of the parts.
Each widget weighs 75 grams. Each gizmo weighs 112 grams
"""

number_of_widgets = int(input("Enter the number of widgets: "))
number_of_gizmos = int(input("Enter the number of gizmos: "))

total_widgets = number_of_widgets * 75
total_gizmos = number_of_gizmos * 112

print("The total of weight of widgets is ", total_widgets)
print("The total of weight of gizmos is ", total_gizmos)
