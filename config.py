#============================================
version = "1.20.1"
# расположение сервера mc
server_dir = "/root/pm-nodes/server/"

# эти значения по умолчанию не требуют изменений
log_file = server_dir + "/logs/latest.log"

# часто плагины сервера будут использовать "[PluginName] сообщение" для регистрации сообщений
# это приводит к ложным срабатываниям обнаружения /say,
# так как /say выводит [игрок] сообщение

# все, что находится в этом списке, не будет вызывать обнаружение /say
blacklisted_users = ["Dynmap"] #"[Dynmap] что-то" не вызовет обнаружение /say

#--------------------------------------------

# настройка webhook в Discord
webhook = False # если False, будет использоваться бот
webhook_url = "https://discord.com/api/webhooks/xxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
discord_nickname = "PM-Chat"

#--------------------------------------------

# настройка бота в Discord
bot_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
bot_channel_id = 0 # идентификатор канала, к которому вы хотите привязать чат mc
command_prefix = "!" # префикс команды для бота

# сообщения из Discord, отправляемые в чат mc
# допустимые заполнители: user, message, reply_user, reply_message
discord_to_mc_message = "§b[Discord]§r {user} » {message}" 
discord_reply_message = "§b[Discord]§r {user} (ответ на {reply_user}) » {message}"
discord_ignore_bots = True # игнорировать ботов в привязанном канале?

console_channel = True # включить/отключить канал консоли
console_channel_id = 0 # идентификатор канала для дополнительного канала консоли

# установить пользовательский статус
# допустимые заполнители: motd, gametype, map, numplayers, maxplayers, hostport, hostip
# допустимые типы статуса: playing, streaming, listening, watching и competing
custom_status = True
custom_status_type = "playing"
custom_status_message = "с {numplayers}/{maxplayers} игроками" # будет отображаться как "играет с x/y игроками"


# настройка rcon
# вы можете найти порт и пароль rcon-сервера в server.properties
rcon_address = "127.0.0.1:25575"
rcon_password = "password"

# настройка query
# вы можете найти адрес и порт в server.properties
use_query = True # использовать протокол query, совместимый с версией beta 1.9 и выше
# если это значение false, то оно будет работать только для версий 1.7 и выше
# рекомендуется установить в true
query_address = "127.0.0.1:25565"

# настройка ping
server_address = "127.0.0.1:25565"

# сообщения об ошибках
timeout_message = "Ошибка: время запроса истекло. Запущен ли сервер MC?."
connection_refused_message = "Ошибка: соединение отклонено. Запущен ли сервер MC?."

#--------------------------------------------

#commands config:
#these are the outputs of the commands that are run from discord

#help command:
#{pre} is a placeholder for the prefix
help_use_embed = True #use embeds?

#message to send if embeds are disabled
help_message = """Command List:
 - {pre}players - Lists the online players
 - {pre}stats - Gets various stats about the server
 - {pre}run [cmd] - Run a command in the server console
 - !motd (address) (port) - Displays a server MOTD as an image.
 - {pre}help - Shows this message

Source code: <1github.com/PM-Kirill/PM-Chat>
""".format(pre=command_prefix)

#will only be used for the embed
command_list = """
 - {pre}players - Lists the online players
 - {pre}stats - Gets various stats about the server
 - {pre}run [cmd] - Run a command in the server console
 - !motd (address) (port) - Displays a server MOTD as an image.
 - {pre}help - Shows this message
""".format(pre=command_prefix)

#the embed to send, if enabled
help_output_embed = {
    "title": "Command List:",
    "footer": "Source code: github.com/PM-Kirill/PM-Chat",
    "color": 0x3CB371,
    "description": command_list
}
thumbnail_in_help = True

#--------------------------------------------

#player list commands
#valid placeholders: hostname, gametype, game_id, version, plugins,
#map, numplayers, maxplayers, hostport, hostip
player_list_use_embed = True #use embeds?

#the message to send if embeds are disabled
player_list_message = """
{numplayers}/{maxplayers} players connected:
{items}
"""
#valid placeholders: player
player_list_item = " - {player}"

#the embed to send, if enabled
player_list_embed = {
    "title": "{numplayers}/{maxplayers} Players Connected:",
    "footer": None,
    "color": 0x3CB371,
    "fields": [
        {
            "name": "Players:",
            "value": "{items}",
            "inline": False
         },
    ]
}
thumbnail_in_player_list = True

#--------------------------------------------

#stats command
#valid placeholders: hostname, gametype, game_id, version, plugins,
#map, numplayers, maxplayers, hostport, hostip
stats_use_embed = True #use embeds?

#will only be used if the embed is disabled
stats_output_query = """
Server Stats:
Players: {numplayers}/{maxplayers}
Map name: {map}
Port: {hostport}
Version: {version}
MOTD:
{hostname}
"""
#the embed to send, if enabled
stats_output_embed = {
    "title": "Server Stats:",
    "footer": "Server IP: newsmp.mine.bz:{hostport}",
    "color": 0x3CB371,
    "fields": [
        {
            "name": "Players:",
            "value": "{numplayers}/{maxplayers}",
            "inline": True
         },
        {
            "name": "Map Name:",
            "value": "{map}",
            "inline": True
        },
        {
            "name": "Version",
            "value": "{version}",
            "inline": True
        }
    ]
}
motd_image_in_stats = True
thumbnail_in_stats = True #will only work if the embed is enabled

#--------------------------------------------

#run command
#valid placeholders: output
run_output = """
Command output:

{output}

"""

#--------------------------------------------

#motd command
#no placeholders
motd_use_embed = True #use embeds?
#the message to send if embeds are disabled
motd_message = """
Server MOTD:
"""
#the embed to send, if enabled
motd_embed = {
    "title": "Server MOTD:",
    "footer": None,
    "color": 0x3CB371
}
#the message to send while the desired server is being pinged
motd_pinging_message = "Pinging the server..."

#name of the server
motd_title = "Server"

bad_ip_output = "Invalid IP address!"

#--------------------------------------------

#messages config:
#these are the messages that are displayed in discord

#chat messages
#valid placeholders: player, chatmsg
player_message = "{player} » {chatmsg}"
slash_say_message = "[{player}] » {chatmsg}"

#player join/leave messages
#valid placeholders: player
player_join_message = "{player} joined the game"
player_leave_message = "{player} left the game"

#server start/stop messages
#valid placeholders: [none]
server_start_message = ":white_check_mark: Server has started"
server_stop_message = ":octagonal_sign: Server has stopped"

#advancement get messages
#valid placeholders: players
advancement_message = "{player} has made the advancement [{advancement}]"
goal_message = "{player} has reached the goal [{advancement}]"
challenge_message = "{player} has completed the challenge [{advancement}]"

#death messages
#valid placeholders: chatmsg
death_message = "{deathmsg}"

#===========================================
