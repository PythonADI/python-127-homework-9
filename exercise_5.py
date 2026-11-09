def read_votes():
    """Keep asking for names until 'done' is entered and return vote counts."""
    votes = {}
    while True:
        print("Vote (or done):")
        name = input()
        if name == "done":
            break
        votes[name] = votes.get(name, 0) + 1
    return votes
def report(votes): 
    """Print the vote report and announce the winner based on early voting rules."""
    if not votes:
        print("No votes.")  
        return
    for name, count in votes.items():
        print(f"{name}: {count}")
    winner = None
    max_votes = -1
    for name,count in votes.items():
        if count > max_votes:
            max_votes = count
            winner = name
    print(f"Winner: {winner}")
votes = read_votes()
report(votes)
