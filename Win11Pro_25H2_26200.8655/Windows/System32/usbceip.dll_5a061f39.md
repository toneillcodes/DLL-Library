# Binary Specification: usbceip.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\usbceip.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5a061f39494389129206ab5c5c8cb5f701c9c43ef00141b2b722520b49e27dca`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x38F0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x38F0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x3C70` | 9,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `UsbCeip_Execute` | `0x60A0` | 244 | UnwindData |  |
