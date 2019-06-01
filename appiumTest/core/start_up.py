from appium import webdriver


class StartApp:

    # 启动app
    def startUp_app(self, conf_data):
        startUp_action = {
            'platformName': conf_data['platformName'],                  # android还是ios的环境
            'deviceName': conf_data['deviceName'],                      # 手机设备名称，通过adb devices查看
            'platformVersion': conf_data['platformVersion'],            # android版本号
            'appPackage': conf_data['appPackage'],                      # apk的包名
            'appActivity': conf_data['appActivity'],                    # apk的launcherActivity
            'noReset': True,                                            # 不需要每次都安装apk
            'unicodeKeyboard': True,                                    # 使用unicode编码方式发送字符串
            'resetKeyboard': True,                                      # 隐藏手机软键盘
            'automationName': 'Uiautomator2'                            # 定位toast元素,弹框消息提示定位
                        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', startUp_action)

        return driver

    # login 启动app,会重新安装app，启动到登录页面
    def login_app(self, conf_data):
        startUp_action = {
            'platformName': conf_data['platformName'],
            'deviceName': conf_data['deviceName'],
            'platformVersion': conf_data['platformVersion'],
            'appPackage': conf_data['appPackage'],
            'appActivity': conf_data['appActivity'],
            # 'noReset': True,                                        # 不需要每次都安装apk
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'automationName': 'Uiautomator2'
                        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', startUp_action)
        return driver
