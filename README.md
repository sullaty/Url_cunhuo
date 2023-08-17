## 脚本使用方式

`url_ok.py` 是一个用于检测URL可访问性的Python脚本。你可以使用命令行运行该脚本，并根据需要指定URL以及输出结果的文件。

### 用法示例

1. **检测单个URL并打印结果：**

   如果你只想要在命令行中检测一个单独的URL，并直接在命令行中查看结果，可以使用以下命令：

   ```sh
   python url_ok.py -u [URL]
   ```

   其中 `[URL]` 是你要检测的URL。

   例如：

   ```sh
   python url_ok.py -u https://www.example.com
   ```

2. **检测单个URL并将结果写入文件：**

   如果你想要将检测结果写入到文件中，可以使用 `-o` 参数来指定输出文件路径。使用以下命令：

   ```sh
   python url_ok.py -u [URL] -o [output_file_path]
   ```

   其中 `[URL]` 是你要检测的URL，`[output_file_path]` 是你想要将结果写入的文件路径。

   例如：

   ```sh
   python url_ok.py -u https://www.example.com -o results.txt
   ```

   结果将被追加写入到 `results.txt` 文件中。

### 参数说明

- `-u, --url [URL]`：要检测的URL。必填参数。
- `-o, --output [output_file_path]`：结果输出文件路径。可选参数。如果不提供此参数，结果将直接打印到命令行。

### 示例

- 检测单个URL并打印结果：

  ```sh
  python url_ok.py -u https://www.example.com
  ```

- 检测单个URL并将结果写入文件：

  ```sh
  python url_ok.py -u https://www.example.com -o results.txt
  ```
