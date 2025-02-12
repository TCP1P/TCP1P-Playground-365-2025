from lamda.client import Device, ApplicationOpStub, GrantType
from time import sleep
from type import Status, Queue

MAIN_PACKAGE_NAME = "com.dimas.kehilangankunci"
PROCESS_TIMEOUT = 5*60 # 5 minutes
CHALLENGE_NAME = "Intro To Intent"


def run_exploit(device: Device, pocPackageName: str):
    exploit: ApplicationOpStub = device.application(pocPackageName)
    permissions = exploit.permissions()
    for permission in permissions:
        if permission.startswith("android.permission"):
            exploit.grant(permission, mode=GrantType.GRANT_ALLOW)
        exploit.start()

    while not exploit.is_foreground():
        pass


def callback(device: Device, pocPackageName: str, q: Queue):
    q.status = Status.RUNNING_PROOF_OF_CONCEPT

    run_exploit(device, pocPackageName)

    sleep(5)
