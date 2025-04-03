import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

class BucketshotRouletteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bucketshot Roulette")
        self.root.geometry("800x600")
        
        # Game state variables
        self.players = {}
        self.bag = []
        self.current_player = None
        self.player_order = []
        self.player_index = 0
        self.round_number = 1
        self.bot_difficulty = 0 
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create welcome screen
        self.create_welcome_screen()
        
    def create_welcome_screen(self):
        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        # Welcome message
        ttk.Label(self.main_frame, text="Welcome to Bucketshot Roulette!", 
                 font=('Helvetica', 16, 'bold')).grid(row=0, column=0, pady=20)
        
        # Rules text
        rules = """Rules:
1. A bag contains 'Safe' and 'Buckshot' boxes.
2. Players take turns choosing to give the box to themselves or another player.
3. If 'Buckshot' is drawn, the recipient loses 1 life. (Each player starts with 3 lives)
4. If a player gives a 'Safe' box to themselves, they get another turn.
5. The game ends when only one player remains standing."""
        
        ttk.Label(self.main_frame, text=rules, justify=tk.LEFT).grid(row=1, column=0, pady=20)
        
        # Mode selection buttons
        ttk.Button(self.main_frame, text="Solo vs Bot", 
                  command=self.show_bot_difficulty_screen).grid(row=2, column=0, pady=10)
        ttk.Button(self.main_frame, text="Multiplayer", 
                  command=self.setup_multiplayer).grid(row=3, column=0, pady=10)
    
    def setup_multiplayer(self):
        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        ttk.Label(self.main_frame, text="Enter number of players:").grid(row=0, column=0, pady=10)
        self.num_players_var = tk.StringVar()
        num_players_entry = ttk.Entry(self.main_frame, textvariable=self.num_players_var)
        num_players_entry.grid(row=0, column=1, pady=10)
        
        ttk.Button(self.main_frame, text="Continue", 
                  command=self.create_player_entry_screen).grid(row=1, column=0, columnspan=2, pady=10)
    
    def create_player_entry_screen(self):
        try:
            num_players = int(self.num_players_var.get())
            if num_players < 2:
                messagebox.showerror("Error", "Please enter at least 2 players")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            return
            
        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        self.player_entries = []
        ttk.Label(self.main_frame, text="Enter player names:").grid(row=0, column=0, columnspan=2, pady=10)
        
        for i in range(num_players):
            ttk.Label(self.main_frame, text=f"Player {i+1}:").grid(row=i+1, column=0, pady=5)
            entry = ttk.Entry(self.main_frame)
            entry.grid(row=i+1, column=1, pady=5)
            self.player_entries.append(entry)
            
        ttk.Button(self.main_frame, text="Start Game", 
                  command=self.start_multiplayer_game).grid(row=num_players+1, column=0, columnspan=2, pady=10)
    
    def show_bot_difficulty_screen(self):
        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        ttk.Label(self.main_frame, text="Select Bot Difficulty", 
                 font=('Helvetica', 14, 'bold')).grid(row=0, column=0, pady=20)
        
        difficulties = [
            "Level 0 - Always Self",
            "Level 1 - 33% Self, 67% Opponent",
            "Level 2 - Always Opponent",
            "Level 3 - Box Count Strategy",
            "Level 4 - Random Preview",
            "Level 5 - Perfect Knowledge"
        ]
        
        for i, diff in enumerate(difficulties):
            ttk.Button(self.main_frame, text=diff, 
                      command=lambda d=i: self.start_solo_mode(d)).grid(row=i+1, column=0, pady=5)
            
        # Add back button
        ttk.Button(self.main_frame, text="Back", 
                  command=self.create_welcome_screen).grid(row=len(difficulties)+1, column=0, pady=20)

    def start_solo_mode(self, difficulty):
        self.players = {"You": 3, "Bot": 3}
        self.player_order = ["You", "Bot"]
        self.bot_difficulty = difficulty
        self.setup_game_screen()
        self.start_new_round()

    def make_bot_move(self):
        target = self.get_bot_decision()
        self.message_label.config(text=f"Bot gives box to {target}")
        self.root.after(1000, lambda: self.resolve_move(target))

    def get_bot_decision(self):
        # Level 0: Always give box to self
        if self.bot_difficulty == 0:
            return "self"
        
        # Level 1: Always give box to opponent
        elif self.bot_difficulty == 2:
            return "You"
        
        # Level 2: 1/3 chance self, 2/3 chance opponent
        elif self.bot_difficulty == 1:
            return "self" if random.random() < 1/3 else "You"
        
        # Level 3: Based on remaining box counts
        elif self.bot_difficulty == 3:
            safe_count = self.bag.count("Safe")
            buckshot_count = self.bag.count("Buckshot")
            
            if safe_count > buckshot_count:
                return "self"
            else:
                return "You"
        
        # Level 4: Random preview
        elif self.bot_difficulty == 4:
            # Peek at a random box without removing it
            preview_box = random.choice(self.bag)
            if preview_box == "Safe":
                return "self"
            else:
                return "You"
        
        # Level 5: Perfect knowledge
        elif self.bot_difficulty == 5:
            # Bot knows the next box
            next_box = self.bag[-1]  # Since we pop from the end
            if next_box == "Safe":
                return "self"
            else:
                return "You"
        
        return "You"  # Default fallback
    
    def start_multiplayer_game(self):
        self.players = {}
        for entry in self.player_entries:
            name = entry.get().strip()
            if name:
                self.players[name] = 3
        
        if len(self.players) < 2:
            messagebox.showerror("Error", "Please enter at least 2 player names")
            return
            
        self.player_order = list(self.players.keys())
        self.setup_game_screen()
        self.start_new_round()
    
    def setup_game_screen(self):
        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        # Create game info frame with two sections
        self.info_frame = ttk.LabelFrame(self.main_frame, text="Game Info", padding="10")
        self.info_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Add labels for round info and box count
        self.round_info_label = ttk.Label(self.info_frame, text="")
        self.round_info_label.grid(row=0, column=0, padx=5)
        
        self.box_count_label = ttk.Label(self.info_frame, text="")
        self.box_count_label.grid(row=0, column=1, padx=5)
        
        # Create player status frame
        self.status_frame = ttk.LabelFrame(self.main_frame, text="Player Status", padding="10")
        self.status_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)
        
        # Create action frame
        self.action_frame = ttk.LabelFrame(self.main_frame, text="Actions", padding="10")
        self.action_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=10)
        
        # Create message frame
        self.message_frame = ttk.LabelFrame(self.main_frame, text="Messages", padding="10")
        self.message_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.message_label = ttk.Label(self.message_frame, text="")
        self.message_label.grid(row=0, column=0)
    
    def start_new_round(self):
        self.round_number += 1
        num_boxes = random.randint(5, 10)
        num_safe = random.randint(1, num_boxes - 1)
        num_buckshot = num_boxes - num_safe
        self.bag = ["Safe"] * num_safe + ["Buckshot"] * num_buckshot
        random.shuffle(self.bag)
        
        # Update round info with box type counts
        self.round_info_label.config(
            text=f"Round {self.round_number}\n"
                 f"Starting boxes: {num_boxes}\n"
                 f"Safe boxes: {num_safe}\n"
                 f"Buckshot boxes: {num_buckshot}"
        )
        
        # Initialize box count display
        self.update_box_count()
        
        self.update_player_status()
        self.next_turn()
    
    def update_box_count(self):
        # Update only the remaining box count
        self.box_count_label.config(text=f"\nRemaining boxes: {len(self.bag)}")
    
    def update_player_status(self):
        # Clear existing status
        for widget in self.status_frame.winfo_children():
            widget.destroy()
            
        # Show each player's lives
        for i, (player, lives) in enumerate(self.players.items()):
            ttk.Label(self.status_frame, 
                     text=f"{player}: {'❤️' * lives}").grid(row=i, column=0, sticky=tk.W)
    

    def next_turn(self):
        if not self.bag:
            # Show message about empty bag
            self.message_label.config(text="📦 Bag is empty! Adding new boxes...")
            # Wait for 2 seconds before starting new round
            self.root.after(2000, self.start_new_round)
            return
            
        self.current_player = self.player_order[self.player_index]
        
        # Clear action frame
        for widget in self.action_frame.winfo_children():
            widget.destroy()
            
        # Update message
        self.message_label.config(text=f"{self.current_player}'s turn")
        
        # Update only the box count, preserve round info
        self.update_box_count()
        
        if self.current_player == "Bot":
            self.root.after(1000, self.make_bot_move)
        else:
            # Create target selection buttons
            ttk.Label(self.action_frame, text="Give box to:").grid(row=0, column=0, columnspan=2, pady=5)
            
            # Add "Self" button
            ttk.Button(self.action_frame, text="Self", 
                      command=lambda: self.make_move("self")).grid(row=1, column=0, columnspan=2, pady=2)
            
            # Add buttons for other players
            row = 2
            for player in self.players:
                if player != self.current_player:
                    ttk.Button(self.action_frame, text=player,
                             command=lambda p=player: self.make_move(p)).grid(row=row, column=0, columnspan=2, pady=2)
                    row += 1
    
    def make_move(self, target):
        self.resolve_move(target)
    
    def resolve_move(self, target):
        drawn_box = self.bag.pop()
        
        # Show the result
        if drawn_box == "Buckshot":
            if target == "self":
                self.players[self.current_player] -= 1
                self.message_label.config(text=f"❌ {self.current_player} drew Buckshot and loses a life!")
            else:
                self.players[target] -= 1
                self.message_label.config(text=f"❌ {target} receives Buckshot and loses a life!")
        else:
            self.message_label.config(text=f"✅ {target} is safe!")
            # Modified condition: Allow both human and bot to get another turn
            if target == "self":
                self.root.after(1500, self.next_turn)
                return
        
        # Check for eliminated players
        eliminated = [p for p, lives in self.players.items() if lives <= 0]
        for p in eliminated:
            del self.players[p]
            self.player_order.remove(p)
        
        # Check for game over
        if len(self.players) == 1:
            winner = list(self.players.keys())[0]
            messagebox.showinfo("Game Over", 
                              f"🎉 {winner} wins with {self.players[winner]} lives remaining!")
            self.create_welcome_screen()
            return
        
        # Move to next player
        self.player_index = (self.player_index + 1) % len(self.player_order)
        
        # Update display and continue
        self.update_player_status()
        self.update_box_count()
        self.root.after(1500, self.next_turn)


def main():
    root = tk.Tk()
    app = BucketshotRouletteGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
