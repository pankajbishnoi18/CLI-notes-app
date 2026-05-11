
j=1
while j>0:

    print("select the command you  want to execute")
    print("1-add a new note")
    print("2-view the existing notes")
    print("20-to delete any note")
    print("press 16 to exit the app")
    i=int(input())
    if i==1:
        print("write the note......")
        new_note=input()


        with open("notes.txt","a") as file:
            file.write(new_note + "\n")


        
           
    if i==2:
       with open("notes.txt","r") as file:
          saved_notes=file.readlines()
       print(saved_notes)
    print("_______________________________________________________________________________________________________")
    print("_______________________________________________________________________________________________________")
    if i==16:
         break
    if i==20:
        with open("notes.txt","r") as file:
          saved_notes=file.readlines()
        for index,note in enumerate(saved_notes):
            print(f"{index+1}--{note}")
        print("enter the number of the note you want to delete")
        res=int(input())
        saved_notes.pop(res-1)
        with open("notes.txt","w" ) as file:
            file.writelines(saved_notes)
        print("deleted successfuly")
        

        
        











