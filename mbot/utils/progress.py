from asyncio import AbstractEventLoop


def upload_progress_hook_factory(client, message, index, total, title):
    bar_length = 20
    loop: AbstractEventLoop = client.loop

    def progress(current, total_size):
        percent = (current * 100 / total_size) if total_size else 0
        percent_str = f"{percent:.1f}%"
        filled = int(bar_length * percent // 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        text = (
            f"Uploading {index}/{total}\n"
            f"{title}\n"
            f"`[{bar}] {percent_str}`"
        )
        if current < total_size:
            loop.call_soon_threadsafe(
                loop.create_task, message.edit_text(text)
            )
        else:
            loop.call_soon_threadsafe(
                loop.create_task, message.edit_text("Upload complete.")
            )

    return progress
