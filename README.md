# Discord Webhook Tool

This tool provides several functionalities for interacting with Discord webhooks, including:
- Sending spam messages to a webhook
- Sending single messages to a webhook
- Generating and sending fake Nitro codes to a webhook

## Features

1. **Webhook Spammer**: Continuously sends a custom message to a specified webhook.
2. **Webhook Message Sender**: Sends a single message to a specified webhook.
3. **Nitro Code Generator**: Generates random fake Nitro codes and sends them to a specified webhook.

## Prerequisites

- Python 3.x
- Required Python libraries: `colorama`, `requests`

## Installation

1. Clone the repository or download the script.
   ```bash
   git clone https://github.com/your-repo/discord-webhook-tool.git
   cd discord-webhook-tool
   ```

2. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```bash
python webhook_tool.py
```

### Options

When prompted, choose one of the following options:

1. **Webhook Spammer**: Enter the webhook URL and the message you want to spam. The tool will continuously send messages until manually stopped.
2. **Webhook Message Sender**: Enter the webhook URL and a single message to send.
3. **Nitro Code Generator**: Enter the webhook URL. The tool will generate random fake Nitro codes and send them to the webhook.
4. **Exit**: Exits the program.

## Code Example

The tool features a custom ASCII logo and colorized output for better user experience. Here's an example of its usage:

```python
print("\nWhat do you want to do? ")
print("1. Webhook Spammer")
print("2. Webhook Message Sender")
print("3. Nitro Code Generator")
print("4. EXIT")

choose = int(input("Choose: "))

if choose == 1:
    spam()
elif choose == 2:
    send_single_message()
elif choose == 3:
    nitro()
elif choose == 4:
    exit_program()
```

## Notes

- Ensure the webhook URL is correct and active before using the tool.
- **Disclaimer**: Use this tool responsibly. Abusing Discord webhooks may violate Discord's terms of service.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Credits

- Developed by [@idok](https://github.com/idok)
- ASCII art inspired design included.

## Disclaimer

This tool is for educational purposes only. The author is not responsible for any misuse or damage caused by this script.
