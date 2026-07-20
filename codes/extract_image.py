import json
import base64
from pathlib import Path


ipynb_file = r"D:\GNN\notebooks\图神经网络和信息传递机制.ipynb"

output_dir = Path(__file__).parent.parent / "images"
output_dir.mkdir(exist_ok=True)


with open(ipynb_file, "r", encoding="utf-8") as f:
    notebook = json.load(f)


count = 0


for cell in notebook["cells"]:

    # 1. 提取输出图片
    if "outputs" in cell:

        for output in cell["outputs"]:

            if "data" in output:

                if "image/png" in output["data"]:

                    img = output["data"]["image/png"]

                    with open(
                        output_dir / f"output_{count}.png",
                        "wb"
                    ) as f:

                        f.write(base64.b64decode(img))

                    count += 1


    # 2. 提取 Markdown 附件图片
    if "attachments" in cell:

        for name, data in cell["attachments"].items():

            if "image/png" in data:

                img = data["image/png"]

                with open(
                    output_dir / f"attachment_{count}.png",
                    "wb"
                ) as f:

                    f.write(base64.b64decode(img))

                count += 1


print(f"共导出 {count} 张图片")