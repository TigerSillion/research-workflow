"""Create a research workspace with the Python standard library."""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="从模板创建课题；重跑仅补齐缺少的文件")
    parser.add_argument("directory", type=Path)
    parser.add_argument("--question", help="本轮要回答的问题")
    args = parser.parse_args()
    destination = args.directory.expanduser().resolve()
    templates = Path(__file__).resolve().parents[1] / "templates"
    question = args.question or "写下一个可用证据检验的问题。"
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "artifacts").mkdir(exist_ok=True)
    for source in sorted(templates.glob("*.md")):
        target = destination / source.name
        content = source.read_text(encoding="utf-8").replace("{{QUESTION}}", question)
        try:
            with target.open("x", encoding="utf-8") as stream:
                stream.write(content)
        except FileExistsError:
            if not target.is_file():
                raise
            print("保留", target.name)
        else:
            print("创建", target.name)
    print("课题目录", destination)


if __name__ == "__main__":
    main()
