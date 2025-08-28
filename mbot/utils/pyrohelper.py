from pyrogram.errors import MessageNotModified


async def safe_edit(message, *args, **kwargs):
    """Edit a message while gracefully handling MessageNotModified."""
    try:
        return await message.edit_text(*args, **kwargs)
    except MessageNotModified:
        # Ignore attempts to edit with the same content
        return message
