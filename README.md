
# Mutebot Discord Bot

This Discord bot is designed to perform administrative tasks in voice channels.

## Features

- **Mute All Users**: Mutes all users in the current voice channel.
- **Unmute All Users**: Unmutes all users in the current voice channel.
- **List Commands**: Lists all available commands.
- **Developer Information**: Shows information about the bot developer.

## Commands

- `!muteall`: Mutes all users in the voice channel.
- `!unmuteall`: Unmutes all users in the voice channel.
- `!commands`: Lists all available commands.
- `!info`: Shows developer information.

## Getting Started

### Prerequisites

- Python 3.6+
- discord.py library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shishir1337/discord-bot.git
   cd discord-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the bot:
   - Replace `YOUR_BOT_TOKEN` in `bot.run('YOUR_BOT_TOKEN')` with your bot token obtained from the Discord Developer Portal.

4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

Once the bot is running, invite it to your Discord server and use the commands listed above in a voice channel where the bot has administrator permissions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the discord.py community for their helpful resources and documentation.

---

Replace placeholders like `YOUR_BOT_TOKEN` with actual values and adjust any additional details specific to your bot's functionalities or setup instructions. This README provides a clear overview of what the bot does, how to install it, and how to contribute to its development.
