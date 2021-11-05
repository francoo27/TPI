from ..Data import audioRepository

def audio_create(audio):
    audioRepository.audio_create(audio)

def audio_update(audio):
    audioRepository.audio_update(audio)

def query_audio():
    return audioRepository.query_audio()

def audio_delete(id):
    audioRepository.audio_delete(id)


def get_audio(id):    
    return audioRepository.get_audio(id)

