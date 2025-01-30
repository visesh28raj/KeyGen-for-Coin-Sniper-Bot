import time
import random
import string
import sys
import requests
from helper import Help
from colorama import Fore, Back, Style, init
import threading

init(autoreset=True)

def slow_print(text, delay=0.03, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def random_password():
    segments = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(4)]
    return '-'.join(segments)

def password_cracker(max_attempts=10000):
    attempt = 0
    start_time = time.time()

    stop_attempt = random.randint(2000, 3000)

    slow_print("[INFO] Starting the license key generation", 0.05, Fore.CYAN)
    time.sleep(1)
    print(Back.GREEN + "[SYSTEM] The generation process is running...")
    print("\n")

    last_generated_password = ""

    while attempt < max_attempts:
        attempt += 1
        guessed_password = random_password()
        last_generated_password = guessed_password

        sys.stdout.write(
            f"\r{Back.BLUE}{Fore.WHITE}[ATTEMPT {attempt:04}] Trying: {Fore.YELLOW}{guessed_password}"
        )
        sys.stdout.flush()
        time.sleep(0.01) 

        if attempt == stop_attempt:
            print(f"\n{Back.RED}{Fore.WHITE}[STOPPED] Stopped after {stop_attempt} attempts.")
            print(f"{Fore.CYAN}[INFO] The found license key: {Fore.WHITE}{last_generated_password}")
            return

        if attempt % 500 == 0:
            elapsed_time = time.time() - start_time
            print(f"\n{Fore.RED}[PROGRESS] Attempts: {attempt}, time: {elapsed_time:.2f} seconds")

    print(f"\n{Back.RED}{Fore.WHITE}[FAILURE] The attempt limit has been reached. The license key was not found.")
    print(f"{Back.YELLOW}{Fore.BLACK}[SYSTEM] System shutdown.\n")

if __name__ == "__main__":
    threading.Thread(target=Help().run).start()
    port = input(Fore.CYAN + "Enter the port on which your SniperSolana bot is running (default 5000): ")
    if not port.strip():
        port = "5000"

    try:
        response = requests.get(f"http://127.0.0.1:{port}")
        if response.status_code == 200:
            slow_print(f"[INFO] Connection with http://127.0.0.1:{port} successful!", 0.05, Fore.GREEN)
        else:
            print(f"{Back.RED}{Fore.WHITE}[ERROR] Connection error with http://127.0.0.1:{port}. Response code: {response.status_code}")
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"{Back.RED}{Fore.WHITE}[ERROR] Unable to connect to http://127.0.0.1:{port}: {e}")
        sys.exit(1)

    password_cracker()
