# Binary Specification: qoswmi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\qoswmi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b5b94283fcd0b7f2fdafc33f3fd95c1d4aa58a801b7328f8b725946b0eaaf7ec`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1EB0` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1EF0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x1F70` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1FD0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x2020` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x2240` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x23C0` | 63,600 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
