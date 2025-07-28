# Hopper Bot  
*A simple Telegram bot.*

---

## How to Run  
Follow these steps to get the bot running.

---

### 1. Get the Code  
This command downloads the bot's source code from GitHub to your computer.  

```bash
git clone https://github.com/biscuit1800/Hopper.git
```

### 2. Enter the Project Directory
This command moves you into the newly downloaded folder.
```bash
cd Hopper
```

### 3. Set Up a Virtual Environment
These commands create an isolated environment for the bot's dependencies, so they don't interfere with other Python projects.

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
This command reads the requirements.txt file and installs all the necessary Python libraries for the bot to work.
```bash
pip install -r requirements.txt
```

### 5. Configure the Bot
You need to provide your bot's token and your admin ID(s).

* Create a new file in the Hopper folder and name it env.py.
* Open this file and paste the following code, replacing the placeholders with your actual data:

Get this from @BotFather on Telegram
```bash
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```


Get your Telegram user ID(s) from @userinfobot on Telegram
You can add one or multiple IDs in a list, like this:
```bash
ADMIN_ID = [123456789]           # for one admin
```
or
```bash
ADMIN_ID = [123456789, 987654321]  # for multiple admins
```
### 6. Start the Bot
This command runs the main script and brings your bot online.
```bash
python main.py
```
