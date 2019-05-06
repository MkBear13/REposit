class Singleton:
  def __new__(self):
    if not hasattr(self, 'instance'):
      self.instance = super().__new__(self)
    return self.instance