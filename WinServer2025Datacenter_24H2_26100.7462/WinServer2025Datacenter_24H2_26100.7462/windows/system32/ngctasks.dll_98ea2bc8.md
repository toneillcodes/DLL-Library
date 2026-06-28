# Binary Specification: ngctasks.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ngctasks.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `98ea2bc8954bab3dc67a2cb2055a0c5fbb0acb930f55050ca2c19e66abc0807f`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllRegisterServer` | `0x15400` | 12,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x15400` | 12,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllCanUnloadNow` | `0x18520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x18540` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `NgcTriggerTaskForOobe` | `0x18580` | 281 | UnwindData |  |
| 1 | `GetRetryTimeStamp` | `0x19720` | 119 | UnwindData |  |
| 2 | `SetAikTimeTrigger` | `0x1A1F0` | 73 | UnwindData |  |
