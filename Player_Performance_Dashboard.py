players = []
n = int(input("Enter number of players: "))

# 1. Collect Player Data
for i in range(n):
    print(f"\nEnter details for player {i+1}:")
    name = input("Player Name: ")
    missions = int(input("Missions Completed: "))
    health = int(input("Health Level (0–100): "))
    powerups = int(input("Power-ups Collected: "))
    score = int(input("Score (0–1000): "))
    players.append((name, missions, health, powerups, score))

# 2. Display Player Stats Table
print("\n🎮 Player Stats Table")
print("| {:<12} | {:<8} | {:<6} | {:<9} | {:<5} |".format("Player Name", "Missions", "Health", "Power-ups", "Score"))
print("|" + "-"*14 + "|" + "-"*10 + "|" + "-"*8 + "|" + "-"*11 + "|" + "-"*7 + "|")
for p in players:
    print("| {:<12} | {:<8} | {:<6} | {:<9} | {:<5} |".format(p[0], p[1], p[2], p[3], p[4]))

# 3. Identify Star Player (Highest score, then highest health)
star = players[0]
for p in players[1:]:
    if p[4] > star[4]:
        star = p
    elif p[4] == star[4] and p[2] > star[2]:
        star = p
print(f"\n🏆 Star Player: {star[0]} (Score: {star[4]}, Health: {star[2]})")

# 4. Assign Rank to Players
print("\n🎖️ Player Ranks:")
for p in players:
    score = p[4]
    health = p[2]
    if score >= 900 and health >= 80:
        rank = "🥇 Elite"
    elif score >= 700:
        rank = "🥈 Pro"
    elif score >= 500:
        rank = "🥉 Amateur"
    else:
        rank = "🚫 Noob"
    print(f"{p[0]}: {rank}")

# 5. Flag Critical Health Players
print("\n🚑 Players Needing Recovery:")
critical = [p for p in players if p[2] < 30]
if critical:
    for p in critical:
        print(f"- {p[0]} (Health: {p[2]})")
else:
    print("All players are healthy.")

# 🔄 6. Update Player Stats by Name
choice = input("\nDo you want to update a player's data? (yes/no): ").lower()
if choice == 'yes':
    update_name = input("Enter the name of the player to update: ").lower()
    found = False
    for i in range(len(players)):
        if players[i][0].lower() == update_name:
            print(f"\nCurrent data for {players[i][0]}:")
            print(f"Missions: {players[i][1]}, Health: {players[i][2]}, Power-ups: {players[i][3]}, Score: {players[i][4]}")
            
            # Ask for updated data
            missions = int(input("Enter updated missions: "))
            health = int(input("Enter updated health (0–100): "))
            powerups = int(input("Enter updated power-ups: "))
            score = int(input("Enter updated score (0–1000): "))

            # Update the tuple
            players[i] = (players[i][0], missions, health, powerups, score)
            print(f"✅ Data for {players[i][0]} updated successfully.")
            found = True
            break
    if not found:
        print("❌ Player not found.")
else:
    print("No updates made.")

# 7. Final Performance Report
print("\n📊 Final Performance Report")
print("| {:<12} | {:<5} | {:<6} | {:<9} | {:<8} | {:<17} |".format(
    "Player", "Score", "Health", "Power-ups", "Rank", "Status"))
print("|" + "-"*14 + "|" + "-"*7 + "|" + "-"*8 + "|" + "-"*11 + "|" + "-"*10 + "|" + "-"*19 + "|")

for p in players:
    name, missions, health, powerups, score = p
    # Rank
    if score >= 900 and health >= 80:
        rank = "Elite"
    elif score >= 700:
        rank = "Pro"
    elif score >= 500:
        rank = "Amateur"
    else:
        rank = "Noob"
    # Status
    status = "Needs Recovery" if health < 30 else "Healthy"
    
    print("| {:<12} | {:<5} | {:<6} | {:<9} | {:<8} | {:<17} |".format(
        name, score, health, powerups, rank, status))