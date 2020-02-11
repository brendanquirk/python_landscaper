tools = [
    {
    "name": "teeth",
    "wage": 1,
    "cost": 0
    },
    {
    "name": "scissors",
    "wage": 5,
    "cost": 5
    },
    {
    "name": "old mower",
    "wage": 50,
    "cost": 35
    },
    {
    "name": "fancy mower",
    "wage": 100,
    "cost": 250
    },
    {
    "name": "students",
    "wage": 250,
    "cost": 500
    }
]

# print(tools)

player = {
    "current_tool": tools.pop(0),
    "bank_account": 0
}

def start_game():
    print("Lets make that bread")
    show_status()
    ask_for_action()


def show_status():
    print(f"Current tool: {player['current_tool']}// Bank Account: {player['bank_account']}")

def cut_grass():
    player['bank_account'] += player['current_tool']['wage']
    print(f"Let's cut some grass! You current have {player['current_tool']['name']}!")


def buy_tool():
    if player['bank_account'] >= tools[0]['cost']:
        player['bank_account'] -= tools[0]['cost']
        player['current_tool'] = tools.pop(0)
        print(f"You just bought {player['current_tool']['name']} for {player['current_tool']['cost']}")
        show_status()
        ask_for_action()
    else:
        print(f"You cant afford {tools[0]['name']} yet!")
        ask_for_action()

def ask_for_action():
    player_choice = ''

    if len(tools) > 0:
        player_choice = input(f"Next tool: {tools[0]['name']}, cost(s) {tools[0]['cost']}// (l)andscape or (b)uy new tool")
    else:
        player_choice = input(f"No more tools to buy! Keep (l)andscaping!\n")

    if player_choice == 'l':
        cut_grass()
    elif player_choice == 'b' and len(tools) > 0:
        buy_tool()
    else:
        print('Option unavailable please choose a valid entry!')
        ask_for_action()

def check_win():
    if player['bank_account'] >= 1000 and player['current_tool']['name'] == 'students':
        print('You win!')
    else:
        show_status()
        ask_for_action()

while player['bank_account'] < 1000:
    if player['current_tool']['name'] == 'students' and player['bank_account'] == 1000:
        print('You win!')
    else:
        start_game()
