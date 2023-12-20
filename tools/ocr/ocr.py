from .PPOCR_api import GetOcrApi
from tools.environment import logger
from PIL import Image
import sys
import os
import io
# import cpufeature
# import time


# "D:\Kin-project\python-SGA\tools\ocr\PaddleOCR-json_v.1.3.1\PaddleOCR-json.exe"
class OCR:
    def __init__(self):
        # if cpufeature.CPUFeature["AVX2"]:
        #     self.exe_name = "PaddleOCR-json"
        #     self.exe_path = r"tools\ocr\PaddleOCR-json_v.1.3.1\PaddleOCR-json.exe"
        #     # logger.debug(_("CPU 支持 AVX2 指令集，使用 PaddleOCR-json"))
        # else:
        #     self.exe_name = "RapidOCR-json"
        #     self.exe_path = r"tools\ocr\RapidOCR-json_v0.2.0\RapidOCR-json.exe"
        # logger.debug(_("CPU 不支持 AVX2 指令集，使用 RapidOCR-json"))
        self.exe_name = "PaddleOCR-json"
        self.exe_path = r"3rd_package\PaddleOCR-json_v.1.3.1\PaddleOCR-json.exe"
        # self.exe_name = "RapidOCR-json"
        # self.exe_path = r"3rd_package\RapidOCR-json_v0.2.0\RapidOCR-json.exe"
        self.running = None
        self.enable()
        
    # def install_ocr(self):
    #     # from module.update.update_handler import UpdateHandler
    #     # from tasks.base.fastest_mirror import FastestMirror
    #     if self.exe_name == "PaddleOCR-json":
    #         ocr_name = "PaddleOCR-json_v.1.3.1"
    #         url = "https://github.com/hiroi-sora/PaddleOCR-json/releases/download/v1.3.1/PaddleOCR-json_v.1.3.1.7z"
    #     else:
    #         ocr_name = "RapidOCR-json_v0.2.0"
    #         url = "https://github.com/hiroi-sora/RapidOCR-json/releases/download/v0.2.0/RapidOCR-json_v0.2.0.7z"
    #     update_handler = UpdateHandler(FastestMirror.get_github_mirror(url), os.path.dirname(self.exe_path), ocr_name)
    #     update_handler.run()
    
    def enable(self):
        if self.running is not None:
            logger.debug("OCR早已启用")
        else:
            abs_path = os.path.join(os.getcwd(), self.exe_path)
            if not os.path.exists(abs_path):
                logger.warning("OCR 路径不存在: {path}").format(path=self.exe_path)
                # self.install_ocr()
            if self.running is None:
                try:
                    logger.debug("开始初始化OCR...")
                    self.running = GetOcrApi(self.exe_path)
                    logger.debug("初始化OCR完成")
                except Exception as e:
                    logger.error("初始化OCR失败：{e}".format(e=e))
                    self.running = None
                    # logger.info(_("请尝试重新下载或解压"))
                    # logger.info(_("若 Win7 报错计算机中丢失 VCOMP140.DLL，请安装 VC运行库"))
                    # logger.info("https://aka.ms/vs/17/release/vc_redist.x64.exe")
                    # input(_("按回车键关闭窗口. . ."))
                    sys.exit(1)
            
    def disable(self):
        if self.running is None:
            logger.debug("OCR早已关闭")
        else:
            self.running.exit()
            logger.debug("OCR关闭")

    @staticmethod
    def convert_format(result):
        if result['code'] != 100:
            logger.debug("222")
            logger.debug(result)
            return False
        converted_result = []

        for item in result['data']:
            box = item['box']
            text = item['text']
            score = item['score']

            converted_item = [
                [box[0], box[1], box[2], box[3]],
                (text, score)
            ]

            converted_result.append(converted_item)

        return converted_result

    def run(self, image):
        # self.instance_ocr()
        try:
            if isinstance(image, Image.Image):
                pass
            elif isinstance(image, str):
                return self.running.run(os.path.abspath(image))
            else:  # 默认为 np.ndarray，避免需要import numpy
                image = Image.fromarray(image)
            image_stream = io.BytesIO()
            image.save(image_stream, format="PNG")
            image_bytes = image_stream.getvalue()
            return self.running.runBytes(image_bytes)
        except Exception as e:
            logger.error(e)
            return r"{}"

    def recognize_single_line(self, image, blacklist=None):
        results = self.convert_format(self.run(image))
        if results:
            for i in range(len(results)):
                line_text = results[i][1][0] if results and len(results[i]) > 0 else ""
                if blacklist and any(char == line_text for char in blacklist):
                    continue
                else:
                    return line_text, results[i][1][1]
        return None

    def output(self, image):
        if isinstance(image, Image.Image):
            pass
        elif isinstance(image, str):
            return self.running.run(os.path.abspath(image))
        else:  # 默认为 np.ndarray，避免需要import numpy
            image = Image.fromarray(image)
        image_stream = io.BytesIO()
        image.save(image_stream, format="PNG")
        image_bytes = image_stream.getvalue()
        result = self.running.runBytes(image_bytes)
        if result['code'] == 101:
            return None
        elif result['code'] != 100:
            logger.debug(result)
            return False
        converted_result = []
        for item in result['data']:
            box = item['box']
            text = item['text']
            score = item['score']
            converted_item = [[box[0], box[1], box[2], box[3]], (text, score)]
            converted_result.append(converted_item)
        return converted_result
