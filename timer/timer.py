import time
import argparse
import os
import sys

def beep():
    """Cross-platform beep."""
    try:
        # Windows beep
        if sys.platform == "win32":
            import winsound
            winsound.Beep(1000, 500)
        else:
            # Unix / macOS beep
            print("\a", end="")
    except:
        pass  # If beep fails, silently ignore

def countdown(seconds):
    paused = False
    original_seconds = seconds

    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        display = f"{mins:02d}:{secs:02d}"

        print(f"\r⏳ Countdown: {display}  (press 'p' to pause/resume)", end="")
        time.sleep(1)

        if seconds == 0:
            print("\n⏰ Time's up!")
            beep()
            break

        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.readline().strip().lower()
            if key == "p":
                paused = not paused
                if paused:
                    print("\n⏸ Paused. Press 'p' to resume.")
                while paused:
                    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                        key = sys.stdin.readline().strip().lower()
                        if key == "p":
                            print("▶️ Resumed.")
                            paused = False
                            break

        seconds -= 1

def stopwatch():
    print("⏱ Stopwatch started. Press Ctrl+C to stop.")
    start = time.time()
    try:
        while True:
            elapsed = int(time.time() - start)
            mins, secs = divmod(elapsed, 60)
            display = f"{mins:02d}:{secs:02d}"
            print(f"\r⏱ Elapsed: {display}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopwatch stopped.")

def main():
    parser = argparse.ArgumentParser(description="Python Timer Toolkit")

    parser.add_argument("time", nargs="?", type=int, help="Countdown time in seconds")
    parser.add_argument("-s", "--stopwatch", action="store_true", help="Run stopwatch mode")

    args = parser.parse_args()

    if args.stopwatch:
        stopwatch()
    elif args.time is not None:
        countdown(args.time)
    else:
        print("Usage examples:")
        print("  python timer.py 60         # 60 sec countdown")
        print("  python timer.py --stopwatch")

if __name__ == "__main__":
    import select
    main()
