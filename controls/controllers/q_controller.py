import readchar

class QController:
  def execute(self):
    print("Do you really want to quit? (Y\\n)")
    command = readchar.readchar()

    if command.upper() == 'Y':
      exit()