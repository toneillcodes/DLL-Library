# Binary Specification: wmi2xml.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\xml\wmi2xml.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `75eddcbaf054cf1c0c781db9e9a80bae477dfd27697d0d2ed81e8808b2b83543`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CloseWbemTextSource` | `0xE650` | 23 | UnwindData |  |
| 2 | `OpenWbemTextSource` | `0xE7F0` | 23 | UnwindData |  |
| 3 | `TextToWbemObject` | `0xEE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WbemObjectToText` | `0xEE60` | 1,778 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0xF560` | 42 | UnwindData |  |
| 6 | `DllGetClassObject` | `0xF590` | 47 | UnwindData |  |
| 7 | `DllRegisterServer` | `0xF650` | 673 | UnwindData |  |
| 8 | `DllUnregisterServer` | `0xF900` | 458 | UnwindData |  |
