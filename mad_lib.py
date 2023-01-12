print("\nWelcome to Mad Libs game:\n")
w1 = input('\nPlease Enter a Noun (tip, it is a sibling): ')
w2 = input('\nPlease Enter a Noun: ')
w3 = input('\nPlease Enter an Adjective: ')
w4 = input('\nPlease Enter a Noun: ')
w5 = input('\nPlease Enter a Verb in present tense: ')
w6 = input('\nPlease Enter a Verb in past tense: ')
w7 = input('\nPlease Enter a Noun :  ')
w8 = input('\nPlease Enter an Adjective: ')
w9 = input('\nPlease Enter an Adjective (it describes a feeling): ')

a="sister"
b="tree"
c="hungry"
d="bread"
e="eat"
f="heard"
g="food"
h="warm"
i="happy"


with open('hungrybird.txt','w') as file:
    file.write("\nThe baby bird was in his nest. He was in his nest with his sister. Their nest was high up in the tree.\nThey were waiting for mama bird. Mom always brought them food. They were hungry. When would mom come home?Would she bring them a worm?\nWould she bring them a fish? Would she bring them a piece of bread? What would mom bring them?\nThey looked at the squirrel nest. The birds looked at the nut. How could they eat a nut? They didn't have strong teeth. The squirrel has strong teeth.\nThe baby birds had no teeth. They had beaks, but no teeth.  They heard mom. They knew her voice. They knew the sound of her wings.\nShe brought them some food. It was still warm. It was delicious.It was pizza. It was pizza with cheese. Baby birds love pizza with cheese.\nThey were so happy. How delicious!\n")
    file.close()
    pass
with open("hungrybird.txt","r") as infile,\
     open("h_b_modified.txt","w") as outfile:
    var=infile.read()  
    var=var.replace(a,w1).replace(b,w2).replace(c,w3).replace(d,w4).replace(e,w5).replace(f,w6).replace(g,w7).replace(h,w8).replace(i,w9) 
    outfile.write(var)
with open("h_b_modified.txt","r") as file:
    var=file.read()
    print("\nPlease read the text below:\n") 
    print(var)
