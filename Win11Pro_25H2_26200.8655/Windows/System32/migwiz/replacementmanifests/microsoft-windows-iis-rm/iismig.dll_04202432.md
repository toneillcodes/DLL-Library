# Binary Specification: iismig.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\migwiz\replacementmanifests\microsoft-windows-iis-rm\iismig.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `042024324cfc73bbf885fb0e5a2732091dd2524f794d71d934437c84f0945af5`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x2D70` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `TriggerApply` | `0x2F70` | 88 | UnwindData |  |
| 2 | `TriggerGather` | `0x2FD0` | 88 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x3050` | 170 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x31D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x31F0` | 188,532 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
