# Binary Specification: rdpendp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rdpendp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f6e2c608964c4eaa3f16bcae08a8469b59b4a5c74524ae4b2015593acc8c9b68`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x29B0` | 157 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x2A60` | 394 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2EB0` | 131,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x2EB0` | 131,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetTSAudioEndpointEnumeratorForSession` | `0x23050` | 668 | UnwindData |  |
