import os
import subprocess


def adjust_audio_volume(input_file, volume_gain):
    """
    调整输入音频文件的音量，生成新的输出文件。

    参数：
      input_file：原始音频文件路径
      volume_gain：音量增益值，例如 "1.5" 表示音量增大 50%，"0.8" 表示降低 20%
    """
    # 构造输出文件名，例如 "audio.mp3" -> "audio_vol_adjusted.mp3"
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_vol_adjusted{ext}"

    # 构造 ffmpeg 命令，使用 volume 滤镜调整音量
    command = [
        "ffmpeg",
        "-i", input_file,
        "-filter:a", f"volume={volume_gain}",
        "-y",  # 覆盖输出文件（如果存在）
        output_file
    ]

    print(f"正在调整音量，增益设为 {volume_gain} ...")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("调整音量时发生错误：")
        print(result.stderr.decode())
    else:
        print("音量调整成功！输出文件为：", output_file)


if __name__ == "__main__":
    input_file = input("请输入音频文件路径: ").strip()
    if not os.path.isfile(input_file):
        print("文件不存在，请检查路径。")
    else:
        volume_gain = input("请输入音量增益（例如 1.5 表示增大50%，0.8 表示降低20%）: ").strip()
        adjust_audio_volume(input_file, volume_gain)
