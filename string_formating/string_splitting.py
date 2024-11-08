text = "Hello world, how are you today?"  
words = text.split()  
#print(words) 

text = "apple,banana,orange,grape"  
fruits = text.split(',')  
#print(fruits)

# splits only the first two
text = "apple-banana-orange-grape"  
fruits = text.split('-', maxsplit=2)  
print(fruits)