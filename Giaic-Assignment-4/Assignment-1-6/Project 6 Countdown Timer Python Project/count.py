import time

def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        time_format = f'{mins:02}:{secs:02}'
        print(time_format, end='\r')  
        time.sleep(1) 
        total_seconds -= 1
    print("Time's up!            ")

def main():
    print("Welcome to the Countdown Timer!")
    
 
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))

    countdown_timer(minutes, seconds)

if __name__ == "__main__":
    main()
