# Binary Specification: ngctasks.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ngctasks.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6449d02f3964f5f3b756bb60ab884da1d4d8aa81013f1314ca407790908518ed`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllRegisterServer` | `0x13850` | 5,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x13850` | 5,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllCanUnloadNow` | `0x14CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x14CE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `NgcTriggerTaskForOobe` | `0x14D20` | 281 | UnwindData |  |
| 1 | `GetRetryTimeStamp` | `0x15570` | 119 | UnwindData |  |
| 2 | `SetAikTimeTrigger` | `0x16040` | 73 | UnwindData |  |
