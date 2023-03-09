# Import libraries
import names, os, random, sqlite3, sys, time, password_generator, pandas
from ascii import *

class Utils():
    def skip(self):
        Game().database()

    def clear(self):
        # Clear terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

    def die(self, message="You failed to steal all the data from the database."):
        self.clear()
        print(message)
        sys.exit()

    def exitGame(self, type):
        # Exit the game with a message based on the type of exit
        self.clear()
        if type.strip().lower() == "health":
            print("38 minutes has passed and the boss noticed the missing SQL table, you failed.")
        elif type.strip().lower() == "xp":
            print("You stole the entire database, well done!")
        sys.exit()

    def timedPrint(self, text, wait=0):
        # Prints and then sleeps to save time
        print(text)
        if wait != 0:
            time.sleep(wait)

    def choice(self, question, options=[]):
        if len(options) == 0:
            options_display = "(yes/no)"
            print(question, options_display)
            while True:
                answer = input("> ").strip().lower()
                if answer in ["yes", "y"]:
                    return True
                elif answer in ["no", "n"]:
                    return False
        else:
            options_display = "(" + "/".join(options) + ")"
            print(question, options_display)
            while True:
                answer = input("> ").strip().lower()
                if answer in options:
                    return answer

class Setup():
    name = None

    def setup(self):
        self.makeDatabase()
        # Reference functions for ease of use
        tprint = Utils().timedPrint
        clear = Utils().clear
        # Show user text to explain the game
        clear()
        tprint(game_name, 2)
        clear()
        x = random.randint(1, 100)
        if x == 50:
            tprint("Welcome to THE GAME (haha you lost)", 1)
        else:
            tprint("Welcome to Sequel", 1)
        tprint("-------------------", 0)
        tprint("You are going to perform a SQL injection on a company's database.", 1.5)
        tprint("Try to steal as much information as possible without being detected.", 1.5)
        tprint("You have 38 minutes until the work day starts, and somebody notices.", 1.5)
        tprint("-------------------", 0)
        tprint("Good luck.", 3)
        clear()
        self.getName()
        tprint(f"Cause great destruction, {self.name}!", 2)
        clear()
        self.warning()
        clear()
        Game().website()

    def getName(self):
        # Get name of the virus and save it
        while True:
            name = input("Enter your virus name: ").strip()
            if len(name) > 0 and len(name) < 15:
                self.name = name
                break

    def warning(self):
        # Reference functions for ease of use
        tprint = Utils().timedPrint
        # Show the user a warning saying that SQL injections are illegal
        tprint(warning)
        tprint("Warning: Hacking is illegal and has real life consequences.", 1.5)
        tprint("Do not copy any of the actions performed thoughout the game.", 1.5)
        tprint("The creator of this game does not endorse or condone hacking.", 1.5)
        tprint("-------------------", 0)
        tprint("With that aside, enjoy the game!", 1.5)

    def makeDatabase(self):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM customer_info")
        for i in range(10):
            emails = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "email.com", "aol.com", "icloud.com"]
            email_punctuation = [".", "!", "_"]
            name = names.get_full_name()
            name_list = name.lower().split()
            email = random.choice(name_list) + random.choice(email_punctuation) + str(random.randint(1, 200)) + "@" + random.choice(emails)
            password = password_generator.PasswordGenerator().generate()
            purchases = random.randint(1, 100)
            loyalty = True if random.randint(0, 2) == 1 else False
            staff = True if random.randint(0, 5) == 1 else False

            cur.execute("INSERT INTO customer_info (customer_id, name, email, password, purchases, loyalty, staff) VALUES (?, ?, ?, ?, ?, ?, ?)", (i+1, name, email, password, purchases, loyalty, staff))

        conn.commit()


class Stats():
    xp = 0
    xpTotal = 25
    health = 10
    healthTotal = 10

    def editXP(self, amount = 1, print = False, more = False):
        # Print stats
        if print:
            self.statsBar(end="\r")
            self.xp += amount
            time.sleep(1)
            if more:
                self.statsBar("\r")
            else:
                self.statsBar()
        # Add XP
        else:
            self.xp += amount
        # Check the XP does not exceed the total XP
        if self.xp >= self.xpTotal:
            Utils().exitGame("xp")

    def editHealth(self, amount = 1, print = False, more = False):
        # Print stats
        if print:
            self.statsBar(end="\r")
            self.health -= amount
            time.sleep(1)
            if more:
                self.statsBar("\r")
            else:
                self.statsBar()
        # Add healths
        else:
            self.xp += amount
        # Check the health is not lower than 0
        if self.health <= 0:
            Utils().exitGame("health")

    def statsBar(self, end="\n"):
        # Print two status bars
        xpFilledLength = int(self.xpTotal * self.xp // self.xpTotal)
        xpBar = '▓' * xpFilledLength + '░' * (self.xpTotal - xpFilledLength)
        healthFilledLength = int(self.healthTotal * self.health // self.healthTotal)
        healthBar = '▓' * healthFilledLength + '░' * (self.healthTotal - healthFilledLength)
        print(f'\rProgress: {xpBar}   Time Remaining: {healthBar}', end=end)

class Game():
    # ANSI colour codes
    RED = "\u001b[31;1m"
    GREEN = "\u001b[32;1m"
    AQUA = "\u001b[36;1m"
    RESET = "\u001b[0m"

    def website(self):
        # Reference functions for ease of use
        tprint = Utils().timedPrint
        clear = Utils().clear
        choice = Utils().choice
        editXP = stats.editXP
        editHealth = stats.editHealth
        statsBar = stats.statsBar
        sleep = time.sleep

        tprint("""       +-----------------------------+
       |      LOCATION: Website      |
       +-----------------------------+""", 2)
        tprint("You approach the website and see a login page.", 1.5)
        tprint("It looks like a standard input, however you are not a normal user, and know better.", 2)
        tprint("You notice the URL has a parameter for the database name.", 1.5)
        exploit = choice("Can you exploit this?", [])
        if exploit:
            clear()

            # Text entering into box animation
            spaces = 28 - 1
            text = ["n", "na", "nam", "name", "name@", "name@e", "name@em", "name@ema", "name@emai", "name@email", "name@email.c", "name@email.", "name@email", "name@emai", "name@ema", "name@em", "name@e", "name@", "name", "nam", "na", "n", "", "p", "pa", "pas", "pass", "passw", "passwo", "passwor", "password", "password'", "password' ", "password' O", "password' OR", "password' OR 1", "password' OR 1=", "password' OR 1=1"]
            for i in text:
                print(f"""      +-----------------------------+
      |{" " + i + "_" + " " * (spaces - len(i))}|
      +-----------------------------+""", end="\n")
                sleep(0.15)
                clear()
            sleep(1)

            tprint("You enter a query into the username field and hit submit.", 1.5)
            tprint(f"The page refreshes and lets you in - {self.GREEN}jackpot!{self.RESET}", 1.5)
            tprint(f"You've found a vulnerability, however you need to be quick - {self.RED}time is running out!{self.RESET}", 2)
            editHealth(1, True, False)
            self.database()
        elif not exploit:
            Utils().die("Wrong decision. Looks like you won't be getting any information from this database.")


    def database(self):
        # Reference functions for ease of use
        tprint = Utils().timedPrint
        clear = Utils().clear
        choice = Utils().choice
        editXP = stats.editXP
        editHealth = stats.editHealth
        statsBar = stats.statsBar
        sleep = time.sleep

        tprint("""       +-----------------------------+
       |      LOCATION: Database     |
       +-----------------------------+""", 2)
        tprint("You successfully infiltrate the database and start sifting through the data.", 1.5)
        tprint("You can see sensitive data that could cause serious data in the wrong hands.\n", 1.5)

        # Print each row of a database with an interval
        conn = sqlite3.connect("database.db")
        db = str(pandas.read_sql_query("SELECT * FROM customer_info", conn))
        for line in db.splitlines():
            print(line)
            sleep(0.1)
        sleep(1)
        clear()

        # User choose which route they take
        playstyle = choice(f"Do you want to {self.AQUA}play it safe{self.RESET} and only steal a small amount of data or {self.AQUA}be reckless{self.RESET} and take everything?", ["safe", "reckless"])
        if playstyle == "safe":
            print("safe")
        elif playstyle == "reckless":
            print("reckless")

    def firewall(self):
        pass

    def security_professionals(self):
        pass

    def decryption(self):
        pass

def main():
    # Classes
    global stats
    stats = Stats()
    setup = Setup()

    # Run game setup
    # setup.setup()
    Utils().skip()


 #   i = 1
  #  while i < 50:
   #     stats.editHealth(1, True)
    #    time.sleep(1)
     #   stats.editXP(3, True)
      #  time.sleep(1)

if __name__ == "__main__":
    main()

# Print database
# conn = sqlite3.connect("database.db")
# print(pandas.read_sql_query("SELECT * FROM customer_info", conn))
