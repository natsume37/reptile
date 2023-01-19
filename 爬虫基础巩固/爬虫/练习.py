from selenium import webdriver

# 初始化配置
options = webdriver.ChromeOptions()
# headless 为静默模式
options.add_argument('--headless')
# 将配置传入浏览器
browser = webdriver.Chrome()
# 打开网页
browser.get('https://wpblog.x0y1.com')
# 关闭浏览器
browser.quit()