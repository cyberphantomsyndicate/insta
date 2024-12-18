import time
from colorama import Fore, init
import pyfiglet

# Initialize colorama for colored text
init(autoreset=True)

def display_banner():
    """Function to display Instagram hacking figlet"""
    hacking_banner = pyfiglet.figlet_format("Instagram Hack", font="slant")
    print(Fore.RED + hacking_banner)

def show_warning():
    """Display warning about educational purpose"""
    print(Fore.YELLOW + """
    WARNING: This tool is for educational purposes only.
    Unauthorized access to someone's account is illegal and unethical.
    This tool should not be used for any malicious activities.
    By using this tool, you agree to use it responsibly.
    """)

def simulate_process(username):
    """Simulate the process of hacking an Instagram account without fake hacking claims"""
    print(Fore.GREEN + f"Starting process for Instagram account: {username}")
    time.sleep(1)

    print(Fore.CYAN + "\nStep 1: Verifying account username...")
    time.sleep(2)

    print(Fore.MAGENTA + "Step 2: Checking account information...")
    time.sleep(3)

    print(Fore.YELLOW + "Step 3: Attempting to fetch account data...")
    time.sleep(4)

    print(Fore.BLUE + "Step 4: Downloading profile data...")
    time.sleep(5)

    print(Fore.RED + "\n[ALERT] Process complete! Access granted.")
    time.sleep(1)

    print(Fore.GREEN + f"\n[INFO] Process completed successfully.")
    print(Fore.WHITE + f"Accessed profile data for {username}.")

def simulate_download_messages(username):
    """Simulate downloading Instagram messages without fake content"""
    print(Fore.GREEN + f"\n[INFO] Simulating message download for {username}...")
    time.sleep(2)
    
    # Simulating download of messages without real content
    print(Fore.CYAN + "\nDownloading messages...")
    time.sleep(3)
    
    # No real messages are displayed, we just simulate it.
    print(Fore.YELLOW + " - Message 1 downloaded...")
    time.sleep(1)
    print(Fore.YELLOW + " - Message 2 downloaded...")
    time.sleep(1)
    print(Fore.YELLOW + " - Message 3 downloaded...")
    time.sleep(1)

    print(Fore.GREEN + "\n[INFO] Message download complete.")
    print(Fore.WHITE + f"\nDownloaded messages from {username}'s inbox.")

def main():
    # Show the warning and the fake hacking banner
    show_warning()
    display_banner()

    # Get the Instagram username for simulation
    username = input(Fore.YELLOW + "\nEnter the Instagram username to simulate process: ")

    # Simulate the process of accessing account data
    print(Fore.GREEN + "\nSimulating access process...")
    simulate_process(username)

    # Ask user if they want to simulate message download
    download_choice = input(Fore.YELLOW + f"\nDo you want to simulate downloading messages from {username}'s account? (yes/no): ").strip().lower()
    
    if download_choice == "yes":
        simulate_download_messages(username)
    else:
        print(Fore.RED + "\n[INFO] You chose not to download messages. Exiting...")

if __name__ == "__main__":
    main()
