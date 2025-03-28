import PyPDF2
import pyttsx3

def read_pdf_aloud(pdf_path, start_page=29, end_page=None):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 350)
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")


    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        end_page = end_page or len(reader.pages)

        # Read each page aloud
        for i in range(start_page - 1, end_page):
            text = reader.pages[i].extract_text()
            engine.say(text)
            engine.runAndWait()

# Example usage

if __name__ == "__main__":
    read_pdf_aloud("Cracking the Data Engineering Interview.pdf")


    # This is only a speech test for voice and speed!
    # engine = pyttsx3.init()
    # rate = engine.getProperty('rate')
    # print(rate)
    # engine.setProperty('rate', rate - 50)
    # voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(voice.id)
    #     engine.setProperty('voice', voice.id)
    #     engine.say('The quick brown fox jumped over the lazy dog.')
    # engine.runAndWait()
