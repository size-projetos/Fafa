"""Le (e opcionalmente ajusta) o volume dos microfones no Windows via pycaw."""

import sys

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL, CoInitialize

CoInitialize()
ajustar = "--max" in sys.argv

for dev in AudioUtilities.GetAllDevices():
    nome = dev.FriendlyName or ""
    if "Microfone" not in nome and "Headset" not in nome and "Mic" not in nome:
        continue
    try:
        iface = dev._dev.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        vol = iface.QueryInterface(IAudioEndpointVolume)
        atual = vol.GetMasterVolumeLevelScalar()
        mudo = vol.GetMute()
        print(f"{nome:<45} volume={atual*100:5.1f}%  mudo={bool(mudo)}  estado={dev.state}")
        if ajustar and atual < 0.99:
            vol.SetMasterVolumeLevelScalar(1.0, None)
            vol.SetMute(0, None)
            print(f"   -> ajustado para 100% e sem mudo")
    except Exception as exc:  # noqa: BLE001
        print(f"{nome:<45} (sem acesso: {exc})")
