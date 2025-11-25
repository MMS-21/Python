import time

# -----------------------------
# Countdown Timer
# -----------------------------
def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"\r⏳ Time left: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print("\r⏰ Time's up!            ")

# -----------------------------
# Stopwatch
# -----------------------------
def stopwatch():
    print("▶ Stopwatch started... Press Ctrl + C to stop.")
    start = time.time()
    try:
        while True:
            elapsed = time.time() - start
            mins, secs = divmod(int(elapsed), 60)
            ms = int((elapsed - int(elapsed)) * 100)
            print(f"\r⏱ Time: {mins:02d}:{secs:02d}.{ms:02d}", end="")
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n⏹ Stopwatch stopped.")
        mins, secs = divmod(int(time.time() - start), 60)
        print(f"Final time: {mins:02d}:{secs:02d}")

# -----------------------------
# Pomodoro Mode
# -----------------------------
def pomodoro(work=25*60, short_break=5*60, long_break=15*60, cycles=4):
    print("🍅 Pomodoro Mode Started")
    for cycle in range(1, cycles + 1):
        print(f"\n▶ Work Session {cycle}/{cycles}")
        countdown(work)

        if cycle == cycles:
            print("\n🌴 Long break!")
            countdown(long_break)
        else:
            print("\n☕ Short break!")
            countdown(short_break)

    print("\n🎉 Pomodoro Completed! Great work!")

# -----------------------------
# Main Menu
# -----------------------------
def main():
    while True:
        print("\n==============================")
        print(" 🧰 Productivity Tool (3-in-1) ")
        print("==============================")
        print("1️⃣ Countdown Timer")
        print("2️⃣ Stopwatch")
        print("3️⃣ Pomodoro Mode")
        print("4️⃣ Exit")
        choice = input("> ")

        if choice == "1":
            try:
                seconds = int(input("Enter time in seconds: "))
                countdown(seconds)
            except ValueError:
                print("❌ Enter a valid number.")
        elif choice == "2":
            stopwatch()
        elif choice == "3":
            pomodoro()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
