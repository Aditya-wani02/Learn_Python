row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")


place=input("where do you want to put the treasure???")
a=int(place[0])-1
b=int(place[1])-1

map[b][a]="X"

print(f"{row1}\n{row2}\n{row3}")
