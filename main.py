import os
from video_processing import extract_audio_from_video
from audio_separation import separate_audio
from midi_conversion import convert_audio_to_dtx

input_video = 'path/to/your/video/file.mp4'
output_directory = 'path/to/output/directory'

# 确保输出目录存在
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

try:
    # 提取音频并保存为 MP3
    audio_file = os.path.join(output_directory, "extracted_audio.mp3")
    extract_audio_from_video(input_video, audio_file)

    # 使用 Demucs 分离音频
    separate_audio(audio_file, output_directory)
except Exception as e:
    print(f"处理过程中出现错误: {e}")

# 输入的鼓声音频文件路径
audio_file = 'path/to/drums_audio.mp3'
# 输出的 MIDI 文件路径
midi_file = 'path/to/drums_output.mid'
# 输出的 DTX 文件路径
dtx_file = 'path/to/drums_output.dtx'

# 从音频文件转换到 DTX 文件
convert_audio_to_dtx(audio_file, midi_file, dtx_file)