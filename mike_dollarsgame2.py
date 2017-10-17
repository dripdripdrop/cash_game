import random
winnings = int(0)
fireworks = """
               \`\/\/\/`/
                )======(
              .'        '.
             /    _||__   \\
            /    (_||_     \\
           |     __||_)     |
           |       ||       |
           '.              .'
             '------------'

"""
sorry = """
            .( * .
         .*  .  ) .
        . . POOF .* .
         '* . (  .) '
          ` ( . *

Sorry, you lost all your money


"""

over = """
  _______      ___      .___  ___.  _______
 /  _____|    /   \     |   \/   | |   ____|
|  |  __     /  ^  \    |  \  /  | |  |__
|  | |_ |   /  /_\  \   |  |\/|  | |   __|
|  |__| |  /  _____  \  |  |  |  | |  |____
 \______| /__/     \__\ |__|  |__| |_______|

  ______   ____    ____  _______ .______
 /  __  \  \   \  /   / |   ____||   _  \\
|  |  |  |  \   \/   /  |  |__   |  |_)  |
|  |  |  |   \      /   |   __|  |      /
|  `--'  |    \    /    |  |____ |  |\  \----.
 \______/      \__/     |_______|| _| `._____|


"""

thanks = """
.___________. __    __       ___      .__   __.  __  ___      _______.
|           ||  |  |  |     /   \     |  \ |  | |  |/  /     /       |
`---|  |----`|  |__|  |    /  ^  \    |   \|  | |  '  /     |   (----`
    |  |     |   __   |   /  /_\  \   |  . `  | |    <       \   \\
    |  |     |  |  |  |  /  _____  \  |  |\   | |  .  \  .----)   |
    |__|     |__|  |__| /__/     \__\ |__| \__| |__|\__\ |_______/

 _______   ______   .______
|   ____| /  __  \  |   _  \\
|  |__   |  |  |  | |  |_)  |
|   __|  |  |  |  | |      /
|  |     |  `--'  | |  |\  \----.
|__|      \______/  | _| `._____|

.______    __          ___   ____    ____  __  .__   __.   _______
|   _  \  |  |        /   \  \   \  /   / |  | |  \ |  |  /  _____|
|  |_)  | |  |       /  ^  \  \   \/   /  |  | |   \|  | |  |  __
|   ___/  |  |      /  /_\  \  \_    _/   |  | |  . `  | |  | |_ |
|  |      |  `----./  _____  \   |  |     |  | |  |\   | |  |__| |
| _|      |_______/__/     \__\  |__|     |__| |__| \__|  \______|


"""


def rooms(cont,risk_level,purse):
    if cont < 1:
        door = int(risk_level / 10) + 1
        print(f"Are you ready to see what's behind door #{door}?")
        ready = input("(yes or no)> ")
        if ready == "yes":
            # find a random number to compare, add some good or bad luck to it
            risk = random.randint(1,100) + random.randint(-(int(risk_level / 10)),(int(risk_level / 10)))
            if risk > risk_level:
                winnings = random.randint(1,(1000 + (risk_level * 10)))
                print(fireworks)
                print(f"You won: ${winnings} this round")
                purse += winnings
                print(f"\n\nYour total winnings are: ${purse}\n\n")
                #increment risk_level for next round
                risk_level += 10
                rooms(0,risk_level, purse)
            elif risk <= risk_level:
                purse = 0
                print(sorry)
                rooms(2,0,0)
        elif ready == "no":
            print(thanks)
            print(f"You are walking away with ${purse}.\nCongratulations.\n\n")
        else:
            print("Please type \"yes\" or \"no\"")
            rooms(0,risk_level,purse)
    else:
        print(over)

print("""
  ______     ___           _______. __    __
 /      |   /   \         /       ||  |  |  |
|  ,----'  /  ^  \       |   (----`|  |__|  |
|  |      /  /_\  \       \   \    |   __   |
|  `----./  _____  \  .----)   |   |  |  |  |
 \______/__/     \__\ |_______/    |__|  |__|

  _______      ___      .___  ___.  _______
 /  _____|    /   \     |   \/   | |   ____|
|  |  __     /  ^  \    |  \  /  | |  |__
|  | |_ |   /  /_\  \   |  |\/|  | |   __|
|  |__| |  /  _____  \  |  |  |  | |  |____
 \______| /__/     \__\ |__|  |__| |_______|


""")
rooms(0,int(0),int(0))
