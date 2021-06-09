# Web Request Library
import requests

# Draft Team Class
class Team:

  def __init__(self, name, managers = [], players = [], budget = 100000):

    # Team Name
    self.name = name

    # Team Budget
    self.budget = budget

    # Team Players
    self.players = players

    # Team Managers
    self.managers = managers

# Draft Class
class Draft:

  def __init__(self):

    # Empty list of teams
    self.teams = {}
    
    # Empty list of players
    self.players = []

    # Finite State Machine
    # States:
    # 0: Waiting
    # 1: Nominating
    # 2: Bidding
    self.state = 0

  # Add a team to the draft
  def new_team(self, name):
    self.teams[name] = Team(name)

  # Remove a team from the draft
  def remove_team(self, name):
    self.teams.pop(name)

  # Add a new manager to a team
  def new_manager(self, team, manager):
    self.teams[team].managers.append(manager)

  # Remove a manger from a team
  def remove_manager(self, team, manager):
    self.teams[team].managers.remove(manager)

  # Add a new player to a team
  def new_player(self, team, player):
    self.teams[team].players.append(player)

  # Remove a player from a team
  def remove_player(self, team, player):
    self.teams[team].managers.remove(player)

  # Add (or remove) from the team budget
  def modify_budget(self, team, amount):
    self.teams[team].managers.budget += amount

  # Import the player list from a web url
  def import_players(self, httpurl):

    # Get a response from the given url
    response = requests.get(httpurl)

    # Iterate over the text lines
    for line in response.text:

      # Add the player's name to the list
      self.players.append(line)

  # Empty the player list
  def delete_players(self):
    self.players = []

class Export:

  def __init__(self):

    # Empty initial draft object
    self.draft = None

  # Start a new draft
  def new_draft(self):

    # If a draft is not running
    if not self.draft:

      # Create a new draft
      self.draft = Draft()

  # End the current draft
  def end_draft(self):

    # If a draft is running
    if self.draft:

      # Need more steps here, for now just do this

      # End the draft
      self.draft = None

  # Add a team to the draft
  def new_team(self, name):
    if self.draft: return self.draft.new_team(name)
    else: return "No draft is running!"

  # Remove a team from the draft
  def remove_team(self, name):
    if self.draft: return self.draft.remove_team(name)
    else: return "No draft is running!"

  # Add a new manager to a team
  def new_manager(self, team, manager):
    if self.draft: return self.draft.new_manager(team, manager)
    else: return "No draft is running!"

  # Remove a manger from a team
  def remove_manager(self, team, manager):
    if self.draft: return self.draft.remove_manager(team, manager)
    else: return "No draft is running!"

  # Add a new player to a team
  def new_player(self, team, player):
    if self.draft: return self.draft.new_player(team, player)
    else: return "No draft is running!"

  # Remove a player from a team
  def remove_player(self, team, player):
    if self.draft: return self.draft.remove_player(team, player)
    else: return "No draft is running!"

  # Add (or remove) from the team budget
  def modify_budget(self, team, amount):
    if self.draft: return self.draft.modify_budget(team, amount)
    else: return "No draft is running!"

  # Import the player list from a web url
  def import_players(self, httpurl):
    if self.draft: return self.draft.import_players(httpurl)
    else: return "No draft is running!"

  # Empty the player list
  def delete_players(self):
    if self.draft: return self.draft.delete_players()
    else: return "No draft is running!"

  def nominate_player(self, player):
    if self.draft: return self.draft.nominate_player(player)
    else: return "No draft is running!"

  # Accept a command
  def command(self, sender, message):

    # Sender Info:
    # [0: name, 1: access level]

    # Split the argument on the spaces
    args = message.split(" ")

    # New Draft (Args: newdraft)
    # User must have AT LEAST moderator privileges to use
    if args[0] in ["newdraft", "nd"]and sender[1] > 1: 
      self.new_draft()

    # End Draft (Args: enddraft)
    # User must have AT LEAST moderator privileges to use
    if args[0] in ["enddraft", "ed"] and sender[1] > 1: 
      self.end_draft()

    # New Team (Args: newteam [name])
    # User must have AT LEAST moderator privileges to use
    if args[0] in ["newteam", "nt"] and len(self.args) > 1 and sender[1] > 1:
      self.new_team(args[1])

    # Remove Team (Args: rmteam [name])
    # User must have AT LEAST moderator privileges to use
    if args[0] in ["rmteam", "rt"] and len(self.args) > 1 and sender[1] > 1: 
      self.remove_team(args[1])

    # Modify Budget (Args: modifybudget [team] [amount])
    # User must have AT LEAST moderator privileges to use
    if args[0] in ["modifybudget", "mb"] and len(self.args) > 2 and sender[1] > 1:
      self.modify_budget(args[1], args[2])

    # Import Players (Args: importplayers [url])
    # User must have AT LEAST moderator privileges to use
    if args[0] in ["importplayers", "ip"] and len(self.args) > 1 and sender[1] > 1:
      self.import_players(args[1])

    # Delete Players (Args: deleteplayers)
    # User must have AT LEAST moderator privileges to use
    if args[0] in ["deleteplayers", "dp"] and sender[1] > 1:
      self.delete_players()

    # New Player (Args: newplayer [team] [name])
    # User must have AT LEAST moderator privileges to use
    if args[0] in ["newplayer", "nt"] and len(self.args) > 2 and sender[1] > 1:
      self.new_player(args[1], args[2])

    # Remove Player (Args: rmplayer [team] [name])
    # User must have AT LEAST moderator privileges to use
    if args[0] in ["rmplayer", "rt"] and len(self.args) > 2 and sender[1] > 1: 
      self.rm_player(args[1], args[2])

    # New Manager (Args: newmanager [team] [name])
    # User must be a moderator or an team manager to use
    if args[0] in ["newmanager", "nt"] and len(self.args) > 2 and sender[1] > 1:
      self.new_manager(args[1], args[2])

    # Remove Manager (Args: rmmanager [team] [name])
    # User must be a moderator or an team manager to use
    if args[0] in ["rmmanager", "rt"] and len(self.args) > 2 and sender[1] > 1: 
      self.remove_manager(args[1], args[2])

    if args[0] in ["nominate", "nom"] and len(self.args) > 1 and sender[1] > 1: 
      self.nominate_player(args[1])