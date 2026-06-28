# Binary Specification: usercpl.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\usercpl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `713f28f1fdfdf4187bb55dfd5dea2867e6e1215cc8fa357a5d863f920e017c13`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE790` | 88 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xE7F0` | 353 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xEA20` | 460,370 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0xEA20` | 460,370 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
