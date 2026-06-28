# Binary Specification: wbemcntl.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\wbemcntl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2dd076ea03a0a5ceca645028a98b81e068a54035120ed7cc1b280b80f18c8b6a`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x15820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x15840` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x15900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x15920` | 35,564 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
