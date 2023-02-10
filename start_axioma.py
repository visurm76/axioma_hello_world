import axipy
from axipy.app import MainWindow

'''
Запуск аксиомы как приложения из среды питон. Например, PyCharm
'''

app = axipy.init_axioma()
MainWindow.show()
app.exec_()
