# Binary Specification: usbceip.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\usbceip.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `68c20e1954147f09df5976f2448243664639a37ce3ab3e0ca4d71f2bc2885423`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x36C0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x36C0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x3A40` | 9,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `UsbCeip_Execute` | `0x5E70` | 244 | UnwindData |  |
