from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.errors import ChannelPrivateError, PeerIdInvalidError

api_id = 2040
api_hash = "b18441a1ff607e10a989891a5462e627"
session_name = 'session_name.session'

channels = [
    'https://t.me/Alpha_V2ray_Group',
    'https://t.me/vpnplusee_free',
    'https://t.me/V2All0',
    'https://t.me/v2rayNG_Streisand',
    'https://t.me/v2ray_proxyz',
    'https://t.me/proxyirgp0',
    'https://t.me/NETMelliAnti',
    'https://t.me/prrofile_purple',
    'https://t.me/vpnz4',
    'https://t.me/Computerwormss',
    'https://t.me/v2rayngvpn',
    'https://t.me/vpnmasi_gp',
    'https://t.me/xy_su',
    'https://t.me/ServerNett',
    'https://t.me/Outline_Vpn',
    'https://t.me/vpnplusee',
    'https://t.me/FAST_configs',
    'https://t.me/NIM_VPN_ir',
    'https://t.me/TechnoTrendZone',
    'https://t.me/YamYamProxy',
    "https://t.me/ZAVI3H",
    'https://t.me/V2rayfastt',



]

message_limit = 10

async def main():
    result_text = ""
    for channel_identifier in channels:
        try:
            print(f"Attempting to connect to channel: {channel_identifier} ...")
            channel = await client.get_entity(channel_identifier)

            history = await client(GetHistoryRequest(
                peer=channel,
                limit=message_limit,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))

            messages = history.messages
            
            result_text += f"\n\n--- Channel: {channel.title} ({channel_identifier}) ---\n"
            print(f"Reading messages from '{channel.title}'...")
            
            message_count = 0
            for msg in messages:
                if msg.message:
                    result_text += msg.message + '\n'
                    message_count += 1
            
            if message_count == 0:
                result_text += "No text messages were found in this channel.\n"

        except (ChannelPrivateError, PeerIdInvalidError):
            error_msg = f"Error: Channel '{channel_identifier}' is private or could not be found. Please ensure you are a member or the username is correct."
            print(error_msg)
            result_text += f"\n\n--- Channel: {channel_identifier} ---\n{error_msg}\n"
        except Exception as e:
            error_msg = f"An unexpected error occurred for '{channel_identifier}': {type(e).__name__} - {e}"
            print(error_msg)
            result_text += f"\n\n--- Channel: {channel_identifier} ---\n{error_msg}\n"

    with open("all_channel_messages.txt", "w", encoding="utf-8") as f:
        f.write(result_text)

    print("\nOperation finished. All messages have been saved to 'all_channel_messages.txt'.")

with TelegramClient(session_name, api_id, api_hash) as client:
    client.loop.run_until_complete(main())