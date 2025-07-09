import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_videos(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def main():
    try:
        while True:
            print("\nYOUTUBE MANAGER")
            print("Choose an option:")
            print("1. List all the videos")
            print("2. Add a YouTube video")
            print("3. Update the YouTube video details")
            print("4. Delete the video")
            print("5. Exit")

            choice = input("Enter your choice: ")

            match choice:
                case '1':
                    list_all_videos()
                case '2':
                    name = input("Enter video name: ")
                    time = input("Enter the time of video: ")
                    add_videos(name, time)
                case '3':
                    print('*' * 70 )
                    
                    list_all_videos()
                    video_id = int(input("Enter the video ID to update: "))
                    name = input("Enter the updated name: ")
                    time = input("Enter the updated time: ")
                    update_videos(video_id, name, time)
                    print('*' * 70)
                    print("/n")
                case '4':
                    video_id = int(input("Enter the video ID to delete: "))
                    delete_videos(video_id)
                case '5':
                    print("Exiting... Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
