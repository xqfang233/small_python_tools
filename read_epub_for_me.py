import ebooklib
from ebooklib import epub
import pyttsx3

def read_epub_aloud(epub_path, start_chapter=1, end_chapter=None):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

    # Load the EPUB file
    book = epub.read_epub(epub_path)
    chapters = [item for item in book.get_items() if item.get_type() == ebooklib.ITEM_DOCUMENT]
    end_chapter = end_chapter or len(chapters)

    # Read each item in the EPUB
    for chapter in chapters[start_chapter - 1:end_chapter]:
        text = chapter.get_body_content().decode('utf-8')
        engine.say(text)
        engine.runAndWait()
    #
    # for item in book.get_items():
    #     if item.get_type() == ebooklib.ITEM_DOCUMENT:
    #         text = item.get_body_content().decode('utf-8')
    #         engine.say(text)
    #         engine.runAndWait()

if __name__ == "__main__":
    epub_path = "C:/Users/xq/Downloads/the lazy genius way.epub"
    read_epub_aloud(epub_path,12,12)
