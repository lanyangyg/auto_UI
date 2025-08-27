# #SeleniumManager update chromedriverVersion (需要vpn)
#
# import os
# from selenium import webdriver
#
# # 设置代理（示例为本地 Clash/V2Ray，端口请改成自己的）
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:1087"
#
# driver = webdriver.Chrome()
# print(driver.capabilities['chrome']['chromedriverVersion'])
# driver.quit()