# Video2DTX

本项目旨在实现从视频或音频文件中自动生成 DTX 鼓谱、生成无声 MP4 背景视频以及生成消除鼓声的 MP3 背景音乐的功能。

## 项目结构

- **requirements.txt**：项目依赖包
- **main.py**：项目入口脚本
- **utils/**：功能模块代码
  - **audio_separation.py**：音频分离（例如使用 Demucs）
  - **midi_conversion.py**：鼓音轨转换为 MIDI，再转换为 DTX 格式（待实现）
  - **video_processing.py**：调用 ffmpeg 进行视频处理
- **input/**：存放输入文件
- **output/**：存放输出结果

## 使用方法

1. **创建并激活虚拟环境**：

   - **Windows**：

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **macOS 和 Linux**：

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **安装依赖**：

   ```bash
   pip install -r requirements.txt

3. **使用**：

  将待处理文件放入 input/ 文件夹。
  运行 python main.py 开始处理。

