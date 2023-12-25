import sys
import time
from src.text_color import error_message
print("")
error_message("Quick Animation Press CTRL + C")
print("")
def letter_animation(duration=10):
    start_time = time.time()

    try:
        while time.time() - start_time < duration:
            elapsed_time = time.time() - start_time
            progress = elapsed_time / duration
            letters = 'Made By Rajan Goswami'[:int(progress * 20) % len('Made By Rajan Goswami')]

            sys.stdout.write(f'\r[{letters}] {int(progress * 100)}%')
            sys.stdout.flush()
            time.sleep(0.5)

    except KeyboardInterrupt:
        sys.stdout.write('\rAnimation interrupted. Finishing quickly...\n')
        time.sleep(0.5)  # Finish the animation quickly
    finally:
        sys.stdout.write('\r[{}] 100%\n'.format('Made By Rajan Goswami'))

def progress_bar(duration=5, length=40):
    start_time = time.time()

    try:
        while time.time() - start_time < duration:
            elapsed_time = time.time() - start_time
            progress = elapsed_time / duration
            filled_length = int(length * progress)
            bar = '=' * filled_length + '>' * (length - filled_length)

            sys.stdout.write(f'\r[{bar}] {int(progress * 100)}%')
            sys.stdout.flush()
            time.sleep(0.1)

    except KeyboardInterrupt:
        sys.stdout.write('\rProgress interrupted. Finishing quickly...\n')
        time.sleep(0.5)  # Finish the progress quickly
    finally:
        sys.stdout.write('\r[{}] 100%\n'.format('=' * length))