import time
import datetime
import sys


def blast_away_clutter():
    print("\n" * 50) 

#  Input Validation 

def grab_valid_number(question, min_val, max_val):
    while True:
        try:
            n = int(input(question))
            if min_val <= n <= max_val:
                return n
            else:
                print(f"It needs to be between {min_val} and {max_val}.")
        except ValueError:
            print("This is not a valid  number. Try again.")

#        STOPWATCH

def stopwatch ():
    print("\n Get ready to measure the time.")
    input(" Press ENTER to start the clock! ")
    start_time = time.time()
    input("Press ENTER again to stop ")
    end_time = time.time()
    elapsed = end_time - start_time 

    # minutes and seconds break down.
    mins = int(elapsed // 60)
    secs = int(elapsed % 60)

    # Milliseconds breakdown
    ms = int((elapsed * 1000) % 1000)

    print("\n TIME COMPLETE")
    print(f"Total Time: {mins} min, {secs} sec, {ms:03d} ms ")
    
#         ALARM CLOCK

def alarm ():
    print("\n Setting the Wake-Up Call")
    
    # putting hours minutes seconds line by line
    h = grab_valid_number("Hour   (0-23): ", 0, 23)
    m = grab_valid_number("Minute (0-59): ", 0, 59)
    s = grab_valid_number("Second (0-59): ", 0, 59)
    
    target_time = datetime.time(h, m, s)
    
    print(f"\nAlarm armed for {target_time.strftime('%H:%M:%S')}.")
    print(" Waiting... type Ctrl+C if you want to snooze.")
    
    try:
        while True:
            # Check the current time every half second.
            now = datetime.datetime.now().time()
            
            # This check is a little loose, but it gets the job done!
            if now.hour == target_time.hour and now.minute == target_time.minute and now.second == target_time.second:
                print("\n" + "" *20)
                print("WAKE UP!")
                print(""   *20)
                # Gives you a moment to see the message.
                time.sleep(4) 
                break
            
            time.sleep(0.5) # Don't burn up the CPU
    except KeyboardInterrupt:
        print("\n Alarm disabled.")

#  Main Loop
def run_the_program():
    while True:

        print("\n" + "" * 30)
        print("" * 30)
        print("1. Stopwatch (Measure time)")
        print("2. Alarm (wake up)")
        print("3. Quit ")
        print("-" * 30)

        #  input for the given choices
        choice = input("What's your choice? (1/2/3): ").strip().lower()
        
        if choice == "1":
            stopwatch ()
        elif choice == "2":
            alarm ()
        elif choice in ("3", "q", "exit"):
            print("Exit")
            sys.exit(0)
        else:
            print("Huh? That wasn't an option. Let's try that again...")
            time.sleep(1)

# Let's get this on the road!
if __name__ == "__main__":
    try:
        run_the_program()
    except KeyboardInterrupt:
        # A backup exit plan just in case you hammer Ctrl+C
        print("\n\nForcing an exit? Rough. See ya!")