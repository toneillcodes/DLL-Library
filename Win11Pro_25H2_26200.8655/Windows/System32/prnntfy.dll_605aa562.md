# Binary Specification: prnntfy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\prnntfy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `605aa562d6fb112a6c586db053c50fc26a83cc56e345e6ac61ef6529117cfa59`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0xA860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xA870` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xA930` | 79,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xA930` | 79,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AsyncUILoaderEntryW` | `0x1DFB0` | 1,286 | UnwindData |  |
| 6 | `PrintNotifyTray_Exit` | `0x1E5B0` | 116 | UnwindData |  |
| 7 | `PrintNotifyTray_Init` | `0x1E630` | 460 | UnwindData |  |
