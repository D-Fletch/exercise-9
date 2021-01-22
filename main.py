#cookie problem 1
p_file = open('preference.txt', 'r')
p_read = p_file.readlines()

for elem in p_read:
    option = elem
    #takes it out of a list

print("you preference: " + option)
change = input("do you want to change it? y/n ")
p_file.close

if change == 'y':
    if option == 'light':
        light = False
    else:
        light = True

    with open('preference.txt', 'w') as p_update:
        if light == False:
            p_update.write("dark")
        else:
            p_update.write("light")

#attributes problem 1


def update_attributes(name, defense, attack):

    with open('attributes.txt', 'w') as a_update:

        #writes it all to the file
        a_update.write('name: ' + str(name) + "\n")
        a_update.write('defense: ' + str(defense) + "\n")
        a_update.write('attack: ' + str(attack) + "\n")


def get_attributes():

    name = input("enter your characters name: ")
    defense = input("enter your defense rating: ")
    attack = input("enter your attack rating: ")
    #could make a verification loop for them both to be under 100 and over 0

    update_attributes(name, defense, attack)


#uncomment to run functions
#get_attributes()

# ROT13 2


def rotate13(word, line_count):
    amount = 13

    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    new_word = ""

    for elem in word:
        i = 0

        for i in range(len(elem)):

            if elem[i] == " ":
                new_word = new_word + " "

            for k in range(len(alphabet)):

                if elem[i] == alphabet[k]:
                    if k + amount < 26:
                        new_letter = alphabet[k + amount]
                        new_word = new_word + new_letter
                    else:
                        new_letter = alphabet[k + amount - 26]
                        new_word = new_word + new_letter
        new_word = new_word + " "

    print(new_word)

    with open('result.txt', 'w') as update13:

        update13.write(new_word)


#im reusing my old caeser cipher code for this
#but it is modified for this problem


def phrase_compiler():

    with open("words_13.txt") as words:
        phrase = []
        line_count = 0

        for elem in words:
            phrase.append(elem.strip())
            line_count += 1

        print(phrase)
        rotate13(phrase, line_count)


#uncomment to run function
#phrase_compiler()

# shopping list  3

# add, create new, removes, output 

def create_shop(num_of_lists):

  with open('shopping list' + str(num_of_lists), 'w') as s_file:

    s_file.write('')


def append_shop(file_name):

  count = int(input("how many items do you want to add? "))

  with open(file_name, 'a') as a_list:

    for x in range(0, count):

      add = str(input("what do you want to add: "))
      
      a_list.write(add + "\n")



def remove_list(list_name):

  shop = []

  with open(list_name, 'r') as a_list:

    items_in = a_list.readlines()

    for x in items_in:
      shop.append(x)
    
  with open(list_name, 'w') as a_file:

    to_remove = input("what item do you want to remove? ")

    for i in range(0, len(shop)):
      if to_remove + "\n" == shop[i]:
        shop.pop(i)
    
    for j in range(0, len(shop)):
      a_file.write(shop[j])    


num_of_lists = 0
'''
create_shop(num_of_lists)
append_shop('shopping list0')
remove_list('shopping list0')
'''


#vending machine problem 3

def create_vend(items):

  with open ('vending_machine', 'w') as v_file:
    
    for x in range(0, len(items)):
      v_file.write(str(items[x]) + "\n")


def vend(items):

  choice = int(input("enter the number of drink you want -"))
  choice = choice - 1
  #to account for array starting at 0

  with open ('vending_machine', 'r') as v_list:
    vending = v_list.readlines()
    #decreases amount of that item by one
    take_one = int(vending[choice])
    take_one -= 1 

    if take_one == -1:
      print("out of stock")
      #recalls function if its out of stock
      vend(items)
    
    #replaces amount with take_one, so stock is minus one
    items.pop(choice)
    items.insert(choice, take_one)

  with open ('vending_machine', 'w') as v_list:

    for x in range(0, len(items)):
      v_list.write(str(items[x]) + "\n")
    

item_amounts = [4, 3, 5, 6, 2, 6, 0, 7, 3, 6, 1, 3, 2, 6, 2, 10, 4, 6, 2, 6, 3, 0, 2, 4, 6, 3]


create_vend(item_amounts)
vend(item_amounts)





