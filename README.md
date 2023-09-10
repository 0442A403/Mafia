# Mafia game

Repository contains HSE service-oriented architectures HW.
code. It implements mafia game. The following is implemented:

- [ ] engine
- [ ] text chat
- [ ] voice chat
- [ ] game stats

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

### Start client 
```
python client -b=0
```
Inside client you can type 'help' to see available commands