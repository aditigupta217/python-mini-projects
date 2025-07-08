import json

def load_data():
    try:
        with open("youtube.txt",'r') as file:
          return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open("youtube.txt",'w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
         print(f"{index}. {video['name']} , Duration: {video['time']}" )
    print("\n")
    print("*" * 70)

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter the time of video:")
    videos.append({'name': name, 'time' : time})
    save_data(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the update name : ")
        time = input("Enter the update time : ")
        videos[index-1] = {'name':name, 'time': time }
        save_data(videos)
        print("Updated sucessfullyy")
    else :
        print("Invalid index selected")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to delet: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data(videos)
        print("deleted sucessfully")
    else:
        print("invalid index")

def main():
    videos = load_data()
    while True :
        print(" YOUTUBE MANAGER ")
        print(" choose an option ")
        print(" 1. List all the videos")
        print(" 2. Add a youtube video")
        print(" 3. Update the youtube video details")
        print(" 4. Delete the video")
        print(" 5. Exit")
        choice = input("Enter the choice : ")

        match choice :
            case '1' : 
                list_all_videos(videos)
            case '2' :
                add_videos(videos)
            case '3' : 
                update_videos(videos)
            case '4' : 
                delete_videos(videos)
            case '5' :
                break
            case _:
                print("invalid choice")
        #print(videos)
            
if __name__ == "__main__" :
    main()
