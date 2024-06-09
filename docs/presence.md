# *module* **presence**

> [Source: ../presence.py @ line 0](../presence.py#L0)

presence.py  
A Genshin Impact Discord RPC Presence script which gives your AR and additional information while playing.

## Imports

- [../assets/characters.py](../assets/characters.py): As `characters`

- [../assets/games.py](../assets/games.py): As `games`

- [../assets/regions.py](../assets/regions.py): As `regions`

- [../config.py](../config.py): As `config`

## *class* **GameData**

> [Source: ../presence.py @ line 24-32](../presence.py#L24-L32)

### *attr* GameData.**game**

> [Source: ../presence.py @ line 25](../presence.py#L25)

> Type: `games.Game`

The game

### *attr* GameData.**region**

> [Source: ../presence.py @ line 27](../presence.py#L27)

> Type: `str`

The region the player is playing in

### *attr* GameData.**name**

> [Source: ../presence.py @ line 29](../presence.py#L29)

> Type: `str`

The name of the player

### *attr* GameData.**level**

> [Source: ../presence.py @ line 31](../presence.py#L31)

> Type: `int`

The level of the player (ex: Adventure Rank on Genshin)

## *class* **GenshinPresence**

> [Source: ../presence.py @ line 35-317](../presence.py#L35-L317)

The Genshin Impact Discord RPC Presence  
It can connect to the Discord RPC and show the player's information while playing Genshin Impact

### Raises

- `ValueError`

### *func* GenshinPresence.**connect**

> [Source: ../presence.py @ line 65-82](../presence.py#L65-L82)

Connects to the Discord RPC

#### Parameters

- **application_id**: `int`
  - The Discord Application ID


#### Returns

- `Presence`
    - The Discord RPC Client

- `pypresence.Presence`

### *func* GenshinPresence.**reset_start**

> [Source: ../presence.py @ line 84-86](../presence.py#L84-L86)

Resets the start time

### *func* GenshinPresence.**reload_config**

> [Source: ../presence.py @ line 88-90](../presence.py#L88-L90)

Reloads the configuration file

### *func* GenshinPresence.**retrieve_cookie**

> [Source: ../presence.py @ line 92-117](../presence.py#L92-L117)

Retrieves the cookie from the configuration file

#### Returns

- `str`
    - The cookie

#### Raises

- `ValueError`

### *func* GenshinPresence.**get_game_data**

> [Source: ../presence.py @ line 119-168](../presence.py#L119-L168)

Gets the game data from the HoYoLAB API

#### Parameters

- **hoyolab_uid**: `int`


#### Returns

- `GameData`
    - The game data associated with the player

#### Raises

- `ValueError`
    - When no game data is found

### *func* GenshinPresence.**sleep**

> [Source: ../presence.py @ line 170-187](../presence.py#L170-L187)

Sleeps for a random amount of time between `time` and `time` + 1 second

#### Parameters

- **amount**: `NoneType`, `float`, `int`
  - This value is **optional**


- **time**: `NoneType`, `float`, `int`
  - This value is **optional**
  - The time to sleep for. If None, it will sleep for the refresh rate specified in the configuration


#### Returns

- `float`

### *func* GenshinPresence.**update_rpc**

> [Source: ../presence.py @ line 189-213](../presence.py#L189-L213)

Updates the Discord RPC Client with the game data

#### Parameters

- **game_data**: `GameData`
  - The game data to update the RPC with


### *func* GenshinPresence.**run**

> [Source: ../presence.py @ line 215-261](../presence.py#L215-L261)

Runs the presence in a loop

> [!WARNING]
> This method is blocking

### *func* GenshinPresence.**stop**

> [Source: ../presence.py @ line 263-281](../presence.py#L263-L281)

Stops the presence

#### Parameters

- **pid**: `NoneType`, `int`
  - This value is **optional**


- **tid**: `NoneType`, `int`
  - This value is **optional**


### *func* GenshinPresence.**flow**

> [Source: ../presence.py @ line 283-317](../presence.py#L283-L317)

The main flow of the presence

#### Returns

- `ForwardRef('GameData')`

- `GameData`

- `NoneType`
