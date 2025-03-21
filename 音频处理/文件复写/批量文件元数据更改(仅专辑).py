import subprocess
import os


def update_album_metadata(file_path, new_album):
    # 根据文件扩展名确定元数据键
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ('.flac', '.ogg'):
        metadata_key = 'ALBUM'
    elif ext in ('.mp3', '.m4a', '.wav', '.aac', '.alac'):
        metadata_key = 'album'
    else:
        metadata_key = 'album'  # 默认尝试使用album

    # 构造临时文件路径
    base, ext = os.path.splitext(file_path)
    temp_file = f"{base}.tmp{ext}"

    # 构建ffmpeg命令
    command = [
        "ffmpeg",
        "-y",  # 覆盖输出文件
        "-i", file_path,
        "-codec", "copy",  # 直接复制流，不重新编码
        "-metadata", f"{metadata_key}={new_album}",
        temp_file
    ]

    print(f"正在处理文件: {os.path.basename(file_path)}")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print(f"错误：无法更新文件 {file_path}")
        print("错误信息：", result.stderr.decode())
        # 清理临时文件
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return False
    else:
        # 替换原文件
        os.replace(temp_file, file_path)
        print(f"成功更新: {os.path.basename(file_path)}")
        return True


if __name__ == "__main__":
    # 支持的音频文件扩展名
    supported_extensions = ['.mp3', '.flac', '.ogg', '.m4a', '.wav', '.aac', '.alac']

    folder_path = input("请输入文件夹路径: ").strip()
    if not os.path.isdir(folder_path):
        print("错误：文件夹不存在")
    else:
        new_album = input("请输入新的专辑名称: ").strip()
        # 遍历所有子目录和文件
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_ext = os.path.splitext(file)[1].lower()
                if file_ext in supported_extensions:
                    file_path = os.path.join(root, file)
                    update_album_metadata(file_path, new_album)
        print("所有文件处理完成。")