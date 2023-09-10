# Mafia game

Repository contains HSE service-oriented architectures HW.
code. It implements mafia game. The following is implemented:

- [x] engine
- [x] text chat
- [ ] voice chat
- [ ] game stats

## Demonstation:
![](demonstration.gif)

## Virtual bot game

To start game session with only bots you can use command
```bash
 docker compose build && docker compose up --scale mafia-bot=5
```

## Real game

Game creates session with id `0` at start for making easy to start 
(you can create your own session if you want to by command `create_game`,
this will generate unique session_id for commands `connect`).
That standard session will start automatically when it will reach 5 player.
So if you want to play with bots you can specify 4 bots:
```bash
 docker compose build && docker compose up --scale mafia-bot=4
```
and then connect to that session
```bash
pip install -r client/requierements.txt
python client
connect 0 MY_USERNAME
```
Game supports following commands:
- `help` - print available commands
- `create_game` - crate game and return session_id for connection
- `connect [sesion_id] [username]` - connect to existing session
- `start_game [mafia_count] [detective_count]` - start a game
- `lynch [username]` - choose player to lynch
- `mafia_choose [username]` - choose player to kill
- `detective_choose [username]` - choose plyaer to check
- `chat [any_string...]` - chat with everyone if it day or chat with your roles if it your role's turn

Inside client you can type 'help' to see available commands. 

## Chat
You can chat with other people with command `chat`
```
chat Hello world!
```
This will be received by everyone, only mafia or only detectives 
depending on day time and your role in game.