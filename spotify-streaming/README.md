# Spotify Streaming bot
This repository was created with the intent of applying different selnium concepts. Neither do I use spotify nor this streaming bot.

# How to Run
1. Create a `secret.json` file with following template

	```
	{
		"username":"your_user_name_here",
		"password":"your_password_here"
	}
	```

Replace `your_user_name_here` with the email or username registered on Spotify
Replace `your_password_here` with your Spotify registered password

2. Update the next playlist url `https://open.spotify.com/playlist/<play_list_number>` from file `bot.py` located on the line number 8 on the code
3. Install dependencies using `pip install -r requirements.txt`
4. Run with `python bot.py`