#the program exits bug

Pets=[]

with open("pets", 'r', encoding='utf-8') as fp:
    for line in fp:
        info=line.split(";")
        name=info[0]
        ID=info[1]
        age=info[2]

        pet={"name":name,"ID":ID,"age":age}
        Pets.append(pet)


def add_pet():
    name=input("name:")
    ID=int(input("ID:"))
    age=input("age:")

    pet={"name":name,"ID":ID,"age":age}

    Pets.append(pet)
    print("恭喜添加成功")
    print("Total:"+str(len(Pets)))

def delete_pet():
    del_id=int(input("the pet's id you want to delete:"))
    t=0
    for pet in Pets:
        if pet["ID"] == del_id:
            Pets.remove(pet)
            print("Delete it!")
            t=1

    if t==0:
        print("please input valid ID")



def show_allpets():
    for pet in Pets:
        text="this petis :name-{};ID-{};age-{}".format(pet["name"],pet["ID"],pet["age"])
        print(text)


def serch_pet():
    search_name=input("what is your pet's name:")

    for pet in Pets:
        if pet["name"]==search_name:
            text="this petis :name-{};ID-{};age-{}".format(pet["name"],pet["ID"],pet["age"])
            print("Find it:"+text)


def save_exit():

    with open("pets",'w+',encoding='utf-8') as fp:
        #lines=[]

        for pet in Pets:
            text="{};{};{}".format(pet["name"],pet["ID"],pet["age"])
            #lines.append(text)
            fp.write(text+'\n')


def main():


    print("-------")
    print("1-add pet;\n2-show all pets;\n3-search pet;\n4-delete pet;\n5-save and exit")
    print("-------")


    while True:
        option = int(input("plesae enter your option:"))
        if option==1:
            add_pet()
        elif option==4:
            delete_pet()
        elif option==2:
            show_allpets()
        elif option==3:
            serch_pet()
        elif option == 5:
            save_exit()
            break
        else:
            print("please input valid option.")


main()