class Host(object):
  def __init__(self):
# add attributes to ourself
    self = self.__dictify_xl_info()
    self.cpus = self.nr_cpus # for usability and reasonable attribute names
    self.mhz = self.cpu_mhz
    self.architecture = self.machine
    self.hostname = self.host

  def mem_use_percent(self):
    a = self.__dictify_xl_info()
    return str(round((float(int(a.total_memory) - int(a.free_memory)) /  float(a.total_memory) ) * 100, 2))

  def mem_free_percent(self):
# to return str or not to return str?
    return str(round(float(100 - self.mem_use_percent()), 2))

  def __dictify_xl_info(self):
    import subprocess
    l = list()
    k = list()

    a = subprocess.check_output(['xl', 'info'])
    for line in a.split('\n'):
      try:
        name, value = line.split(":", 1)[0], line.split(":", 1)[1]
        setattr(self, name.strip(), value.strip())
      except IndexError:
        continue

    return self

  def display(self):
    for a in dir(self):
      if not a.startswith('__'):
        print a, ": " + str(getattr(self, a))

if __name__ == "__main__":
  h = Host()
  h.display()
