# Speech to text

A simple python code to turn audio into text. Works on _Windows, macOS / OS X_ or _Linux_. From this [tutorial](https://platform.openai.com/docs/guides/speech-to-text/speech-to-text-beta).

## Installation

You need [Python](https://www.python.org/downloads/), as well as a [pip](https://github.com/git-guides/install-git#install-git), and [Git](https://github.com/git-guides/install-git#install-git) to clone this repo.

- Clone the repository

```
git clone https://github.com/Valikoz/speech-to-text.git
```

- Install python modules

```
pip install openai
```

```
pip install pydub
```

## Authentication

The OpenAI API uses API keys for authentication. Visit your [API Keys](https://platform.openai.com/account/api-keys) page to retrieve the API key you'll use in your requests.

## Usage

First, go into the directory with project in a terminal. _Like this:_
```
cd path/to/the/project/speech-to-text
```
and run `python3 main.py`. Now, you can see the following dialog

> Please enter your api key: 

Type your [key]((https://platform.openai.com/account/api-keys)) there. You can also add your api key into [`/speech-to-text/config.py`](./config.py).

The next message you can see is

> File path:

You don't have to write full path.  For example for _Windows_ the following strings will be the same

```
File path: c:/users/user/sound-recordings/audio.m4a
File path: ./sound-recordings/audio.m4a
```
**Please use only the forward slash (/).**

[Here](https://platform.openai.com/docs/guides/speech-to-text/introduction) is the file types are supported.

Finally, you can find the transcribed text in the folder with audio.