# Mafia game

Repository contains HSE service-oriented architectures HW.
code. It implements mafia game. The following is implemented:

- [x] engine
- [ ] text chat
- [ ] voice chat
- [ ] game stats

## Demonstation:
![](demonstration.gif)

## Virtual bot game

To start game session with only bots you can use command
```bash
 docker compose build && docker compose up --scale mafia-bot=5
```

## Manual boot

### Start server:

```bash
python engine -s=True -m=5
```
or with 4/5 bots:
```bash
 docker compose build && docker compose up --scale mafia-bot=4
```

### Start client 
```bash
python client
connect 0 my_username
```
Inside client you can type 'help' to see available commands