import pretty_midi
# import mido MidiTrack, Message
from mido import MidiFile
# import os


def audio_to_midi(audio_file, midi_file):
    """
    将音频文件转换为 MIDI 文件。

    参数:
    - audio_file: 输入音频文件路径（例如鼓声 MP3）。
    - midi_file: 输出 MIDI 文件路径。
    """
    try:
        # 使用 pretty_midi 库将音频转换为 MIDI
        midi_data = pretty_midi.PrettyMIDI(audio_file)
        
        # 导出为 MIDI 文件
        midi_data.write(midi_file)
        print(f"MIDI 文件已保存: {midi_file}")
    except Exception as e:
        print(f"转换音频到 MIDI 时出错: {e}")
        raise


def midi_to_dtx(midi_file, dtx_file):
    """
    将 MIDI 文件转换为 DTX 格式。

    参数:
    - midi_file: 输入 MIDI 文件路径。
    - dtx_file: 输出 DTX 文件路径。
    """
    try:
        # 打开 MIDI 文件
        midi = MidiFile(midi_file)
        
        with open(dtx_file, 'w') as dtx:
            # 写入 DTX 文件的头部信息
            dtx.write("#TITLE: Converted MIDI to DTX\n")
            dtx.write("#ARTIST: MIDI to DTX Conversion\n")
            
            # 遍历每个 MIDI track
            for i, track in enumerate(midi.tracks):
                dtx.write(f"#TRACK{i+1}\n")
                
                for msg in track:
                    if msg.type == 'note_on':
                        # 将 MIDI note 信息写入 DTX 格式
                        # 此处假设 MIDI 的 note 是鼓音轨，适合转换为 DTX
                        # 在实际中，您需要根据鼓的音符转换为 DTX 对应的编码
                        note = msg.note
                        time = msg.time
                        dtx.write(f"{time} {note}\n")
            
            print(f"DTX 文件已保存: {dtx_file}")
    except Exception as e:
        print(f"转换 MIDI 到 DTX 时出错: {e}")
        raise


def convert_audio_to_dtx(audio_file, midi_file, dtx_file):
    """
    从音频文件转换到 DTX 文件。

    参数:
    - audio_file: 输入音频文件路径（鼓声 MP3）。
    - midi_file: 输出 MIDI 文件路径。
    - dtx_file: 输出 DTX 文件路径。
    """
    audio_to_midi(audio_file, midi_file)
    midi_to_dtx(midi_file, dtx_file)
