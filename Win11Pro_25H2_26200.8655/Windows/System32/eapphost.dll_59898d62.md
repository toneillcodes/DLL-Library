# Binary Specification: eapphost.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\eapphost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `59898d629e136b9eecc9b3b40e8a8e5883b043dd85a378a3388b3abd151740bb`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `OnSessionChange` | `0x8BA0` | 84 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xDB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xDB40` | 96 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xDC00` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xDC50` | 64 | UnwindData |  |
| 6 | `InitializeEapHost` | `0xDCA0` | 31 | UnwindData |  |
| 7 | `StopServiceOnLowPower` | `0xDEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `UninitializeEapHost` | `0xDEC0` | 18 | UnwindData |  |
