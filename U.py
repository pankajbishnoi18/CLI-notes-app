note1="hey there this is the first note"
note2="this is the second one"
existing_notes=[f"1-{note1}  ,  2-{note2}"]  
print("select the command you bkhkhggkhkhhbg want to execute")
print("1-add a new note")
print("2-view the existing notes")
i=int(input())

if i==1:
    print("type name of the note")
    name=input()
    print("now type whatver you want to write")
    text=input()
    note3=text
    print("do you want to save the note to the existing notes ,answer in yes or no only")
    resp=input()
    if resp=="yes":
        existing_notes.append(f"3-{note3}")
        print("saved successfully")
        print(existing_notes)
if i==2:
    for i in range(len(existing_notes)):
        print(f"{i+1}--{existing_notes[i]}")







