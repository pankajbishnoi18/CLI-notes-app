note1="hey there this is the first note"
note2="this is the second one"
existing_notes=[note1,note2]  

j=1
while j>0:

    print("select the command you  want to execute")
    print("1-add a new note")
    print("2-view the existing notes")
    print("20-to delete any note")
    print("press 16 to exit the app")
    i=int(input())
    if i==1:
    
        print("now type whatver you want to write")
        text=input()
        note3=text
        print("do you want to save the note to the existing notes ,answer in yes or no only")
        resp=input()
        if resp=="yes":
           existing_notes.append(note3)
           print("saved successfully")
        if resp=="no":
           continue
           
    if i==2:
     for k in range(len(existing_notes)):
        print(f"{k+1}--{existing_notes[k]}")
    print("_______________________________________________________________________________________________________")
    print("_______________________________________________________________________________________________________")
    if i==16:
         break
    if i==20:
        for k in range(len(existing_notes)):
           print(f"{k+1}--{existing_notes[k]}")
        print("enter the number of the note which you want to delete")
        d=int(input())
        existing_notes.pop(d-1)
        print(f"note no {d} is deleted successfully")












