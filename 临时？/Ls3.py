import subprocess
import os


def update_mp3_metadata(file_path, title, artist, comment):
    # 构造临时输出文件，防止直接覆盖原文件导致损坏
    temp_file = file_path + ".tmp.mp3"

    command = [
        "ffmpeg",
        "-y",  # 如果输出文件已存在，则覆盖
        "-i", file_path,  # 输入文件
        "-codec", "copy",  # 不重新编码，直接复制音频流
        "-metadata", f"title={title}",
        "-metadata", f"artist={artist}",
        "-metadata", f"comment={comment}",
        temp_file
    ]

    print("正在更新元数据...")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("更新元数据时发生错误：")
        print(result.stderr.decode())
    else:
        # 成功后将原文件替换为新文件
        os.replace(temp_file, file_path)
        print("元数据更新成功！")


if __name__ == "__main__":
    file_path = input("请输入 mp3 文件路径: ").strip()
    if not os.path.isfile(file_path):
        print("文件不存在，请检查路径。")
    else:
        title = input("请输入新标题: ").strip()
        artist = input("请输入新艺术家: ").strip()
        comment = input("请输入新注释（例如来源信息）: ").strip()
        update_mp3_metadata(file_path, title, artist, comment)
