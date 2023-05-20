# напиши здесь код основного приложения и первого экрана

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.connects()
    self.show()
  def set_appear(self):
    
