import random
import time
import os

class NumberGuessingGame:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.games_played = 0
        self.load_high_score()
    
    def load_high_score(self):
        """Load high score from file if exists"""
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read().strip())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
    
    def save_high_score(self):
        """Save high score to file"""
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_banner(self):
        """Display game banner"""
        print("🎯" * 40)
        print("🎯           NUMBER GUESSING GAME           🎯")
        print("🎯" * 40)
        print(f"🏆 High Score: {self.high_score} | 📊 Games Played: {self.games_played}")
        print()
    
    def choose_difficulty(self):
        """Let player choose difficulty level"""
        print("Choose Difficulty Level:")
        print("1. Easy (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 5 attempts)")
        print("4. Expert (1-500, 4 attempts)")
        
        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    difficulties = {
                        1: (1, 50, 10),
                        2: (1, 100, 7),
                        3: (1, 200, 5),
                        4: (1, 500, 4)
                    }
                    return difficulties[choice]
                else:
                    print("Please enter a number between 1 and 4")
            except ValueError:
                print("Please enter a valid number!")
    
    def get_hint(self, guess, target, attempts_left):
        """Provide hints based on the guess"""
        difference = abs(target - guess)
        
        if guess < target:
            direction = "HIGHER"
        else:
            direction = "LOWER"
        
        if difference > 50:
            hint_level = "very far"
        elif difference > 20:
            hint_level = "far"
        elif difference > 10:
            hint_level = "close"
        else:
            hint_level = "very close"
        
        print(f"💡 Hint: You're {hint_level}! Try going {direction}")
        
        # Special hint when few attempts remain
        if attempts_left <= 2:
            if target % 2 == 0:
                print("💡 Extra Hint: The number is EVEN")
            else:
                print("💡 Extra Hint: The number is ODD")
    
    def calculate_score(self, attempts_used, max_attempts, range_size, difficulty_multiplier):
        """Calculate score based on performance"""
        base_score = 100
        attempts_bonus = (max_attempts - attempts_used) * 20
        range_bonus = range_size // 10
        difficulty_bonus = difficulty_multiplier * 50
        
        return base_score + attempts_bonus + range_bonus + difficulty_bonus
    
    def play_game(self):
        """Main game logic"""
        self.clear_screen()
        self.display_banner()
        
        # Setup game parameters
        min_num, max_num, max_attempts = self.choose_difficulty()
        target_number = random.randint(min_num, max_num)
        attempts = 0
        difficulty_multiplier = (max_num // 50)  # Higher range = more points
        
        print(f"\n🎮 I'm thinking of a number between {min_num} and {max_num}")
        print(f"📈 You have {max_attempts} attempts to guess it!")
        print("─" * 50)
        
        while attempts < max_attempts:
            attempts_left = max_attempts - attempts
            print(f"\n🔄 Attempts left: {attempts_left}")
            
            try:
                guess = int(input(f"🎯 Enter your guess ({min_num}-{max_num}): "))
                
                # Validate input range
                if guess < min_num or guess > max_num:
                    print(f"❌ Please enter a number between {min_num} and {max_num}!")
                    continue
                
                attempts += 1
                
                # Check if guess is correct
                if guess == target_number:
                    # Calculate and display score
                    game_score = self.calculate_score(attempts, max_attempts, max_num, difficulty_multiplier)
                    self.score += game_score
                    
                    print("\n🎉" * 20)
                    print(f"🎉 CONGRATULATIONS! You guessed it! 🎉")
                    print(f"🎉 The number was {target_number}!")
                    print(f"🎉 You found it in {attempts} attempts!")
                    print(f"💰 Score earned: {game_score} points!")
                    print(f"🏆 Total score: {self.score} points!")
                    print("🎉" * 20)
                    
                    # Update high score
                    if self.score > self.high_score:
                        self.high_score = self.score
                        print("🏅 NEW HIGH SCORE! 🏅")
                        self.save_high_score()
                    
                    self.games_played += 1
                    break
                
                # Provide feedback for wrong guess
                else:
                    print("❌ Wrong guess!")
                    self.get_hint(guess, target_number, attempts_left)
                    
                    # Show temperature-based feedback
                    difference = abs(target_number - guess)
                    if difference <= 5:
                        print("🔥 Burning hot!")
                    elif difference <= 15:
                        print("♨️  Hot!")
                    elif difference <= 30:
                        print("💨 Warm")
                    elif difference <= 50:
                        print("❄️  Cold")
                    else:
                        print("🧊 Freezing!")
                        
            except ValueError:
                print("❌ Please enter a valid number!")
        
        else:
            # This runs if while loop completes (all attempts used)
            print("\n💀" * 20)
            print(f"💀 GAME OVER! You've used all {max_attempts} attempts!")
            print(f"💀 The number was {target_number}")
            print("💀" * 20)
            self.games_played += 1
    
    def show_stats(self):
        """Display game statistics"""
        self.clear_screen()
        self.display_banner()
        print("📊 GAME STATISTICS")
        print("─" * 30)
        print(f"🏆 High Score: {self.high_score}")
        print(f"💰 Current Score: {self.score}")
        print(f"📈 Games Played: {self.games_played}")
        
        if self.games_played > 0:
            accuracy = (self.games_played - len([g for g in range(self.games_played) if g == 0])) / self.games_played * 100
            print(f"🎯 Accuracy: {accuracy:.1f}%")
        
        input("\nPress Enter to continue...")
    
    def show_instructions(self):
        """Display game instructions"""
        self.clear_screen()
        self.display_banner()
        print("📖 HOW TO PLAY")
        print("─" * 40)
        print("1. Choose a difficulty level")
        print("2. Try to guess the secret number")
        print("3. You'll get hints after each wrong guess")
        print("4. Points are awarded based on:")
        print("   - Fewer attempts used = more points")
        print("   - Higher difficulty = more points")
        print("   - Larger number range = more points")
        print("5. Try to beat your high score!")
        print("\n🎯 HINT SYSTEM:")
        print("   - Distance hints (very far, far, close, very close)")
        print("   - Direction hints (higher/lower)")
        print("   - Temperature hints (burning hot to freezing)")
        print("   - Special hints when few attempts remain")
        input("\nPress Enter to continue...")
    
    def reset_game(self):
        """Reset current game progress"""
        self.score = 0
        self.games_played = 0
        print("🔄 Game progress reset!")
        time.sleep(1)
    
    def main_menu(self):
        """Display main menu and handle user input"""
        while True:
            self.clear_screen()
            self.display_banner()
            
            print("📋 MAIN MENU")
            print("─" * 30)
            print("1. 🎮 Play Game")
            print("2. 📊 View Statistics")
            print("3. 📖 How to Play")
            print("4. 🔄 Reset Progress")
            print("5. 🚪 Exit")
            print()
            print(f"💰 Current Score: {self.score}")
            
            try:
                choice = input("Enter your choice (1-5): ").strip()
                
                if choice == '1':
                    self.play_game()
                    input("\nPress Enter to continue...")
                elif choice == '2':
                    self.show_stats()
                elif choice == '3':
                    self.show_instructions()
                elif choice == '4':
                    self.reset_game()
                elif choice == '5':
                    print("\nThanks for playing! 👋")
                    break
                else:
                    print("❌ Invalid choice! Please enter 1-5")
                    time.sleep(1)
                    
            except (ValueError, KeyboardInterrupt):
                print("\n\nThanks for playing! 👋")
                break

def main():
    """Initialize and start the game"""
    game = NumberGuessingGame()
    game.main_menu()

# Quick play version for simple gameplay
def quick_play():
    """Simple version for quick gameplay"""
    print("🎯 QUICK PLAY - Number Guessing Game")
    print("─" * 40)
    
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"I'm thinking of a number between 1 and 100!")
    print(f"You have {max_attempts} attempts to guess it!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            attempts += 1
            
            if guess == number:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
            elif guess < number:
                print("📈 Try higher!")
            else:
                print("📉 Try lower!")
                
            # Show how close they are
            difference = abs(number - guess)
            if difference <= 5:
                print("🔥 Very close!")
            elif difference <= 15:
                print("♨️ Getting warm!")
                
        except ValueError:
            print("❌ Please enter a valid number!")
    else:
        print(f"\n💀 Game Over! The number was {number}")

if __name__ == "__main__":
    # Check if user wants quick play or full game
    print("Choose game mode:")
    print("1. Full Game (with scores, levels, and features)")
    print("2. Quick Play (simple version)")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '2':
        quick_play()
    else:
        main()