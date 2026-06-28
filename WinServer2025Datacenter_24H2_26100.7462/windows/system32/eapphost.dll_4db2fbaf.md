# Binary Specification: eapphost.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\eapphost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4db2fbaffc5b4f6f8d913a46706156eb22dfbc2c6f75f31ce7ed0463dfdecd22`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `OnSessionChange` | `0x8BD0` | 84 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xE030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xE050` | 96 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xE110` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xE160` | 64 | UnwindData |  |
| 6 | `InitializeEapHost` | `0xE1B0` | 31 | UnwindData |  |
| 7 | `StopServiceOnLowPower` | `0xE3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `UninitializeEapHost` | `0xE3D0` | 18 | UnwindData |  |
