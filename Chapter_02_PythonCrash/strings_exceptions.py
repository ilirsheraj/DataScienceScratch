single_quoted_string = 'data science'
double_quoted_string = "data science"  # my favorite one
print(single_quoted_string)
print(double_quoted_string)
print(single_quoted_string == double_quoted_string)

# backslash for special characters
tab_sting = "\t"
print(len(tab_sting))

# raw-string
not_tab_string = r"\t"
# Do the same with double-backslash
not_tab_string_2 = "\\t"
print(not_tab_string)
print(len(not_tab_string))
print(not_tab_string_2)
print(len(not_tab_string_2))

# Create multi-line strings with triple-quotes
multi_line_string = """This is the first line
This is the second line
This is the third line"""
print(multi_line_string)

# f-string and format() method
first_name = "Ilir"
last_name = "Sheraj"
full_name_1 = first_name + " " + last_name
print(full_name_1)
full_name_2 = "{} {}".format(first_name, last_name)
print(full_name_2)
full_name_3 = f"{first_name}, {last_name}"
print(full_name_3)

# Exceptions: Save the code from crashing
try:
	print(0 / 0)
except ZeroDivisionError:
	print("Cannot divide by zero")
