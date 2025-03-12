import os
import subprocess


def convert_m4s_to_mp3(folder):
    # 遍历指定文件夹下的所有文件
    for filename in os.listdir(folder):
        if filename.lower().endswith(".m4s"):
            input_file = os.path.join(folder, filename)
            # 构造输出的 mp3 文件路径，保持文件名不变，仅扩展名改为 .mp3
            mp3_filename = os.path.splitext(filename)[0] + ".mp3"
            output_file = os.path.join(folder, mp3_filename)

            # 使用 ffmpeg 进行转换
            command = [
                "ffmpeg",
                "-i", input_file,  # 输入文件
                "-vn",  # 不处理视频，仅提取音频
                "-acodec", "libmp3lame",  # 指定 MP3 编码器
                "-q:a", "2",  # 设置音频质量参数
                output_file
            ]

            print(f"正在转换: {filename} -> {mp3_filename}")
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode != 0:
                print(f"转换 {filename} 时发生错误:")
                print(result.stderr.decode())
            else:
                print(f"成功转换: {mp3_filename}")


if __name__ == "__main__":
    folder = input("请输入包含 m4s 文件的文件夹路径: ").strip()
    if os.path.isdir(folder):
        convert_m4s_to_mp3(folder)
    else:
        print("输入的路径不是一个有效的文件夹。")