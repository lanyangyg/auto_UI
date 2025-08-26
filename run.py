import os, shutil, pytest
ROOT_DIR = os.path.dirname(__file__)          # 项目根目录
os.chdir(ROOT_DIR)                            # 强制切到根目录

pytest.main(["--alluredir=allure-results"])
shutil.rmtree("allure_report", ignore_errors=True)
os.system("allure generate allure-results -o allure_report --clean")
#os.system("open allure_report/index.html")
