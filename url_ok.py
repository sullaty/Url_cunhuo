import argparse
import requests

def check_url_availability(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return "可访问"
        else:
            return "无法访问 (HTTP 状态码: {})".format(response.status_code)
    except requests.ConnectionError:
        return "无法访问"

def main():
    parser = argparse.ArgumentParser(description="检测指定URL的可访问性")
    parser.add_argument("-u", "--url", required=True, help="要检测的URL")
    parser.add_argument("-o", "--output", default=None, help="结果输出文件路径")
    args = parser.parse_args()
    
    url = args.url.strip()
    result = check_url_availability(url)
    output = "{}: {}\n".format(url, result)
    
    if args.output:
        with open(args.output, "a") as output_file:
            output_file.write(output)
    else:
        print(output)

if __name__ == "__main__":
    main()
