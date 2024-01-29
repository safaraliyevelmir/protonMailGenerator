from src import DropMailMe
from src import ProtonRegistration


def write_data(password, email):
    with open('accLog.txt', 'a') as f:
        f.write(f"{email}:{password}\n")

if __name__ == '__main__':

    proton = ProtonRegistration()
    username, password = proton.generateUserInformation()
    proton.registrationFirstStep(username, password)

    dropmailme = DropMailMe()
    email = dropmailme.getMailAddress()

    proton.emailVerify(email)
    verificationCode = dropmailme.getVerificationCode()

    proton.sendVerificationCode(verificationCode)

    write_data(password, email)

    # this methods is optional. in the above procces you create account allready
    proton.displayName()
    proton.recoveryMethodSkip()

