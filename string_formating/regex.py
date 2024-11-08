import re  
string = "The quick brown fox jumps over the lazy dog."  
pattern = r"fox"  
match = re.search(pattern, string)  
if match:  
    print("Match found!")  
else:  
    print("Match not found.")  

import re  
string = "John Doe (42 years old)"  
pattern = r"(\w+) (\w+) \((\d+) years old\)"  
match = re.search(pattern, string)  
if match:  
    print("Name:", match.group(1), match.group(2))  
    print("Age:", match.group(3))  
else:  
    print("Match not found.")  