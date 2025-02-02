import ffmpeg


def extract_audio_from_video(video_path, audio_path):
    """
    使用 ffmpeg 从视频文件中提取音频，并保存为 MP3 格式。
    
    参数:
    - video_path: 输入的视频文件路径 (MP4)。
    - audio_path: 输出的音频文件路径 (MP3)。
    """
    try:
        # 提取音频并保存为 MP3
        (
            ffmpeg
            .input(video_path)
            .output(audio_path, vn=None)
            .run(overwrite_output=True)
        )
        print(f"音频已从视频中提取并保存为: {audio_path}")
    except ffmpeg.Error as e:
        print(f"提取音频时出错: {e}")
        raise