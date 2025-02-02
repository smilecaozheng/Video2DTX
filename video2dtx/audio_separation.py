import demucs
import os


def separate_audio(input_audio, output_path):
    """
    使用 Demucs 分离音频文件中的各个声源。
    
    参数:
    - input_audio: 输入的音频文件路径 (MP3)。
    - output_path: 输出分离结果的目录路径。
    """
    # 加载预训练模型
    model = demucs.load_pretrained('mdx_extra')

    # 分离音频
    sources = model.separate(input_audio)

    # 创建输出目录
    os.makedirs(output_path, exist_ok=True)

    # 将分离出的音轨保存到输出目录
    for source_name, source_data in sources.items():
        output_file = os.path.join(output_path, f"{source_name}.mp3")
        source_data.write(output_file)
        print(f"已保存 {source_name} 到 {output_file}")