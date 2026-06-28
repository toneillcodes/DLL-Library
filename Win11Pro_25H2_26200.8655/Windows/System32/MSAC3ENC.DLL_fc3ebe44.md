# Binary Specification: MSAC3ENC.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MSAC3ENC.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fc3ebe444f4427dafc7b2c79a5612e6f779ac647f6619fd2fb680ae215d8740f`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x6120` | 66 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x6170` | 54 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0xDC30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xDC60` | 224 | UnwindData |  |
