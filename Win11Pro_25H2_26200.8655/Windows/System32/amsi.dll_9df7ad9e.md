# Binary Specification: amsi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\amsi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9df7ad9e6826ab76294a91bef274696ee13d18a8cebabcd5c4c352a3d1141df3`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `AmsiUacInitialize` | `0x1570` | 466 | UnwindData |  |
| 10 | `AmsiUninitialize` | `0x1840` | 80 | UnwindData |  |
| 8 | `AmsiUacScan` | `0x20A0` | 304 | UnwindData |  |
| 2 | `AmsiInitialize` | `0x6F20` | 1,174 | UnwindData |  |
| 12 | `DllGetClassObject` | `0x75B0` | 312 | UnwindData |  |
| 6 | `AmsiScanString` | `0x8100` | 84 | UnwindData |  |
| 5 | `AmsiScanBuffer` | `0x8160` | 235 | UnwindData |  |
| 4 | `AmsiOpenSession` | `0x8A50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AmsiCloseSession` | `0x8AB0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `AmsiNotifyOperation` | `0x8B20` | 201 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x8CF0` | 42 | UnwindData |  |
| 13 | `DllRegisterServer` | `0xA670` | 4,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DllUnregisterServer` | `0xA670` | 4,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `AmsiUacUninitialize` | `0xB620` | 78 | UnwindData |  |
