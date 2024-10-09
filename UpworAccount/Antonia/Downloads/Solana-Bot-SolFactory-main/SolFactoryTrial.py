# To test or purchase the source code, contact @SolFactory_bot on Telegram
# To test or purchase the source code, contact @SolFactory_bot on Telegram
# To test or purchase the source code, contact @SolFactory_bot on Telegram

import curses

def main_menu(stdscr):
    curses.curs_set(0)  # Hide the cursor

    menu = {
        "main": [
            ("🔊 Volume Bot", "volume"),
            ("💣 Army Snipe Bot", "army"),
            ("🤖 Bump Bot", "bump"),
            ("🔧 Create Token Bundler", "token"),
            ("💼 Wallet Set", "wallet"),
            ("⚙️ Settings", "settings"),
            ("💰 Pump Strategies", "pump_strategies"),
            ("❌ Exit", "exit")
        ]
    }

    title = [
"   ______           __ ________                     __                                ",                               
"  /      \         |  \        \                   |  \                               ",                                
" |  ▓▓▓▓▓▓\\ ______ | ▓▓ ▓▓▓▓▓▓▓▓ ______   _______ _| ▓▓_    ______   ______  __    __ ",                                
" | ▓▓___\\▓▓/      \\| ▓▓ ▓▓__    |      \\ /       \\   ▓▓ \\  /      \\ /      \\|  \\  |  \\",                                
"  \\▓▓    \\|  ▓▓▓▓▓▓\\ ▓▓ ▓▓  \\    \\▓▓▓▓▓▓\\  ▓▓▓▓▓▓▓\\▓▓▓▓▓▓ |  ▓▓▓▓▓▓\\  ▓▓▓▓▓▓\\ ▓▓  | ▓▓",                                
"  _\\▓▓▓▓▓▓\\ ▓▓  | ▓▓ ▓▓ ▓▓▓▓▓   /      ▓▓ ▓▓       | ▓▓ __| ▓▓  | ▓▓ ▓▓   \\▓▓ ▓▓  | ▓▓",                                
" |  \\__| ▓▓ ▓▓__/ ▓▓ ▓▓ ▓▓     |  ▓▓▓▓▓▓▓ ▓▓_____  | ▓▓|  \\ ▓▓__/ ▓▓ ▓▓     | ▓▓__/ ▓▓",                                
"  \\▓▓    ▓▓\\▓▓    ▓▓ ▓▓ ▓▓      \\▓▓    ▓▓\\▓▓     \\  \\▓▓  ▓▓\\▓▓    ▓▓ ▓▓      \\▓▓    ▓▓",                                
"   \\▓▓▓▓▓▓  \\▓▓▓▓▓▓ \\▓▓\\▓▓       \\▓▓▓▓▓▓▓ \\▓▓▓▓▓▓▓   \\▓▓▓▓  \\▓▓▓▓▓▓ \\▓▓      _\\▓▓▓▓▓▓▓",                                
"                                                                            |  \\__| ▓▓",                                
"                                                                             \\▓▓    ▓▓",                                
"                                                                              \\▓▓▓▓▓▓ "
    ]

    def print_menu(stdscr):
        stdscr.clear()
        # Print the title
        for i, line in enumerate(title):
            stdscr.addstr(i, 0, line, curses.color_pair(4))
        stdscr.addstr(len(title) + 1, 0, "Original Dev: @SolFactory_bot on Telegram", curses.color_pair(3))
        stdscr.addstr(len(title) + 2, 0, "Main Menu - ", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(len(title) + 3, 0, "To test or purchase the source code, contact @SolFactory_bot on Telegram.", curses.color_pair(3))

        # Print the menu
        current_menu_items = menu["main"]
        for idx, item in enumerate(current_menu_items):
            x = 0
            y = idx + len(title) + 5
            stdscr.addstr(y, x, item[0])
        stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Highlighted menu item
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Title color
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Subtitle color
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Bright green title color

    print_menu(stdscr)

    # Wait for user to exit
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main_menu)

# To test or purchase the source code, contact @SolFactory_bot on Telegram
