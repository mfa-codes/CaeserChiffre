from CaeserCheffire import ChaeserCheffire

class Main():
    def main():
        # save the key and msg from user
        userInputMSG = input("Please enter the message here\n>>> ")
        userInputKEY = input("Enter the number of movement\n>>> ")

        cc = ChaeserCheffire(userInputMSG, userInputKEY)

        encyptedText = cc.encryptMSG(cc.getMSG(), cc.getKey())
        print("+==============================The MSG after encrypt======================================+")
        print(encyptedText)

        dencyptedText = cc.dencryptMSG(encyptedText, cc.getKey())

        print("\n+==============================The MSG after dencrypt======================================+")
        print(dencyptedText)


if __name__ == "__main__":
    Main.main()