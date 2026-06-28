# Binary Specification: SxsMigPlugin.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\migration\SxsMigPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d5a3e8e0c3f749fd94e3cc3c1904cacb08eee20eb7d02224c3efef2669682932`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x9850` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x9880` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x99C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x99E0` | 321 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x9B30` | 179 | UnwindData |  |
