import json

file = "notes.json"


def read():
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return data


def write(data):
    f = open(file, "w")
    json.dump(data, f, indent=4)
    f.close()


def menu():
    print("\n--- K Vault ---")
    print("1 View")
    print("2 Add")
    print("3 Search")
    print("4 Edit")
    print("5 Delete")
    print("6 Exit")
    print("7 Export notes")  



def view(n):
    print("-------------- List ---------------")
    if len(n) == 0:
        print("No notes")
        print("\n---------------------------------")
        return

    for x in n:
        print(x["id"], "-", x["title"], "| tags:", ", ".join(x["tags"]))
    print("-----------------------------------")


def add(n):
    t = input("Title: ")
    c = input("Content: ")
    tg = input("Tags (comma): ")

    tags = []
    for i in tg.split(","):
        if i.strip() != "":
            tags.append(i.strip())

    note = {
        "id": len(n) + 1,
        "title": t,
        "content": c,
        "tags": tags
    }

    n.append(note)
    write(n)
    print("Added")


def search(n):
    k = input("Search: ").lower()
    ok = False

    for x in n:
        tlist = []
        for z in x["tags"]:
            tlist.append(z.lower())

        if k in x["title"].lower() or k in x["content"].lower() or k in tlist:
            print("\n========== NOTE ==========")
            print("ID:      ", x["id"])
            print("Title:   ", x["title"])
            print("Content: ", x["content"])
            print("Tags:",  ", ".join(x["tags"]))
            print("==========================\n")
            ok = True

    if ok == False:
        print("Nothing found")


def edit(n):
    i = int(input("Note id: "))

    for x in n:
        if x["id"] == i:
            x["title"] = input("New title: ")
            x["content"] = input("New content: ")
            tg = input("New tags: ")

            tags = []
            for a in tg.split(","):
                if a.strip() != "":
                    tags.append(a.strip())

            x["tags"] = tags
            write(n)
            print("Updated")
            return

    print("Id not exist")


def delete(n):
    i = int(input("Delete id: "))

    for x in n:
        if x["id"] == i:
            n.remove(x)
            write(n)
            print("Deleted")
            return

    print("Id not exist")


def export(n):
    if len(n) == 0:
        print("No notes to export")
        return

    f = open("enotes.txt", "w")
    for x in n:
        f.write("ID: " + str(x["id"]) + "\n")
        f.write("Title: " + x["title"] + "\n")
        f.write("Content: " + x["content"] + "\n")
        f.write("Tags: " + ", ".join(x["tags"]) + "\n")

        f.write("------------------------\n")
    f.close()
    print("Notes exported to enotes.txt")



def main():
    n = read()
    while True:
        menu()
        ch = input("Choice: ")

        if ch == "1":
            view(n)
        elif ch == "2":
            add(n)
        elif ch == "3":
            search(n)
        elif ch == "4":
            edit(n)
        elif ch == "5":
            delete(n)
        elif ch == "6":
            print("Bye")
        elif ch == "7":
            export(n)
            break
        else:
            print("Wrong choice")


main()
