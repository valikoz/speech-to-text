import os
import openai
from openai.error import AuthenticationError 
from pydub import AudioSegment
import config


if config.api_key == '':
    try:
        key = input('Please enter your api key: ')
        openai.api_key = key
    except KeyboardInterrupt:
        print('')
else:
    openai.api_key = config.api_key


# List of the input file types are supported 
# https://platform.openai.com/docs/guides/speech-to-text/introduction
list_of_format = ['mp3', 'mp4', 'mpeg', 'mpga', 'm4a', 'wav', 'webm']


def transcript_maker(path: str):
    '''
    By default, the Whisper API only supports files that are less than 25 MB. 
    If you have an audio file that is longer than that, `transcript_maker` breaks 
    it up into mini chunks which less than 25 MB's.

    Then, it uses the openai.Audio.transcribe() function to transcribe the audio file.
    The function takes in the `audio` variable as the `file` parameter, and
    sets the response format to 'text' using the `response_format` parameter.
    It also specifies the model to use for transcription as 'whisper-1' using the model parameter.

    The transcribed text is then stored in the transcript variable.
    Finally, the transcribed text is saved into text file.

    '''
    root, suffix = os.path.splitext(path)
    dir, stem = os.path.split(root)
    document = os.path.join(dir, stem + '.txt')
    if os.path.exists(document):
        print(f'File {document} already exists. It will be overwritten.', '...', sep='\n')
        os.remove(document)

    size = os.path.getsize(path)

    if size < 24 * 10**6:
        audio = open(path, 'rb')
        transcript = openai.Audio.transcribe(
                model='whisper-1',
                file=audio,
                response_format='text'
        )
        audio.close()

        with open(document, mode='w+', encoding='utf-8') as f:
            f.write(transcript)
            
    else:
        chunk = AudioSegment.from_file(path, suffix[1:])

        while chunk.duration_seconds > 0:
            # PyDub handles time in milliseconds.
            ten_minutes = 10 * 60 * 1000

            mini_chunk, chunk = chunk[:ten_minutes], chunk[ten_minutes:]

            tmp = os.path.join(dir, stem + '.mp3')
            mini_chunk.export(tmp, format='mp3')

            audio = open(tmp, 'rb')
            transcript = openai.Audio.transcribe('whisper-1', audio)
            audio.close()
            
            with open(document, mode='a+', encoding='utf-8') as f:
                f.write(transcript.text + '\n')

            os.unlink(tmp)


def main():
    while True:
        audio = input('File path: ')
        path = os.path.abspath(audio)
        _, suffix = os.path.splitext(path)

        if not os.path.exists(path):
            print(f'{path}, File does not exist.')
            continue
        elif suffix[1:] not in list_of_format:
            print(f'An unsupported file format {suffix[1:]}.')
            continue
        break

    print('...')
    transcript_maker(path)

    print('Process completed successfully.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('')
    except AuthenticationError:
        print('Openai key is wrong!')
