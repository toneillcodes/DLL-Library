# Binary Specification: prnntfy.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\prnntfy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `14b7cb7aaf440b82efd7cef4e729df3239aee5066255006f449c9986b0a65d8f`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0xA490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xA4A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xA560` | 71,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xA560` | 71,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AsyncUILoaderEntryW` | `0x1BE60` | 1,286 | UnwindData |  |
| 6 | `PrintNotifyTray_Exit` | `0x1C460` | 116 | UnwindData |  |
| 7 | `PrintNotifyTray_Init` | `0x1C4E0` | 460 | UnwindData |  |
