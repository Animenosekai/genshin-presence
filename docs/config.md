# *module* **config**

> [Source: ../config.py @ line 0](../config.py#L0)

## Imports

- [../assets/characters.py](../assets/characters.py): As `characters`

- [../assets/games.py](../assets/games.py): As `games`

- [../assets/regions.py](../assets/regions.py): As `regions`

## *class* **Player**

> [Source: ../config.py @ line 8-18](../config.py#L8-L18)

### *attr* Player.**GAME**

> [Source: ../config.py @ line 9](../config.py#L9)

> Type: `games.Game`

The game you are playing

### *attr* Player.**CHARACTER**

> [Source: ../config.py @ line 11](../config.py#L11)

> Type: `characters.Character`

The character you are playing

### *attr* Player.**HOYOLAB_UID**

> [Source: ../config.py @ line 13](../config.py#L13)

> Type: `int`

The HoYoLAB UID of the player

### *attr* Player.**SERVER_REGION**

> [Source: ../config.py @ line 15](../config.py#L15)

> Type: `Optional`

The server region of the player

## *class* **Text**

> [Source: ../config.py @ line 22-40](../config.py#L22-L40)

Texts for the RPC Client  
Available variables for the texts:  
- {name}: The nickname of the player  
- {region}: The name of the region the player is playing on  
- {level}: The level (Adventure Rank) of the player  
- {character}: The character the player is playing  
- {game}: The game the player is playing

### *attr* Text.**STATE_TEXT**

> [Source: ../config.py @ line 33](../config.py#L33)

> Type: `str`

The state text that will be displayed. Available variables: {name}, {region}

### *attr* Text.**DETAILS_TEXT**

> [Source: ../config.py @ line 35](../config.py#L35)

> Type: `str`

The details text that will be displayed. Available variables: {level}

### *attr* Text.**HOVER_TEXT**

> [Source: ../config.py @ line 37](../config.py#L37)

> Type: `str`

The text that will be displayed when the game image is hovered

### *attr* Text.**HOVER_CHARACTER_TEXT**

> [Source: ../config.py @ line 39](../config.py#L39)

> Type: `str`

The text that will be displayed when the character image is hovered. Available variables: {character}

## *class* **Settings**

> [Source: ../config.py @ line 44-52](../config.py#L44-L52)

Settings for the RPC Client

### *attr* Settings.**REFRESH_RATE**

> [Source: ../config.py @ line 47](../config.py#L47)

> Type: `Union`

The rate at which the RPC Client will update the presence

### *attr* Settings.**DISCORD_APPLICATION_ID**

> [Source: ../config.py @ line 49](../config.py#L49)

> Type: `int`

The Discord Application ID

### *attr* Settings.**COOKIE**

> [Source: ../config.py @ line 51](../config.py#L51)

> Type: `Optional`

The cookie header sent by the browser (you can get it from the network tab in the developer tools of your browser). It None, it will try to find it in the environment variable `COOKIE` or the `COOKIE` file in the root directory of the project
