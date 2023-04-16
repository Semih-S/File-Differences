
IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if len(line1) < len(line2):
        line1 += '\0' * (len(line2) - len(line1))
    elif len(line2) < len(line1):
        line2 += '\0' * (len(line1) - len(line2))
    for letter in range(len(line1)):
        if line1[letter] != line2[letter]:
            return letter
    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    count = ""
    if idx < 0 or idx > min(len(line1), len(line2)):
        return ""
    else:
        for _ in range(idx):
            count += "="
        count += "^"
        return f"{line1}\n{count}\n{line2}\n"


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if lines1 == lines2:
        return (IDENTICAL, IDENTICAL)
    for line_num in range(min(len(lines1), len(lines2))):
        idx = singleline_diff(lines1[line_num], lines2[line_num])
        if idx != IDENTICAL:
            return (line_num, idx)
    if len(lines1) != len(lines2):
        return (max(len(lines1), len(lines2))-1, 0)
    return (IDENTICAL, IDENTICAL)
        

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list_of_lines = []
    with open(filename, "rt", encoding="utf-8") as datafile1:
        for line in datafile1.readlines():
            list_of_lines.append(line)
    list_of_lines = [word.rstrip('\n') for word in list_of_lines]
    return list_of_lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    difference =  multiline_diff(lines1, lines2)
    if difference == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    else:
        line_num = difference[0]
        line1 = lines1[line_num]
        line2 = lines2[line_num]
        separator = "=" * difference[1] + "^"
        return f"Line {line_num}:\n{line1}\n{separator}\n{line2}\n"
