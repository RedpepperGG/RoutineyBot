import random
import discord


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'oi':
        return 'terima bhalu sutna dey!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'help':
        return '`Help chaiye admin lai ping han eta kina halla muji`'

    if p_message == 'muji':
        return 'Eva muji sutna ja kati bolya'
    if p_message == 'gajedi':
        return 'Pratyush muji ko name na ley sidhai ping han'
