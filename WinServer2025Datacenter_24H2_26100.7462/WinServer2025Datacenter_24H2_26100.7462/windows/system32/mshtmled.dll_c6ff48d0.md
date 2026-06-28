# Binary Specification: mshtmled.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mshtmled.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c6ff48d0cfad413fa59670f15b0a91980a942865888051051f3ac7540862cdf4`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xA980` | 135 | UnwindData |  |
| 2 | `DllEnumClassObjects` | `0xAA10` | 112 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xAA90` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xAE70` | 171 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xAF30` | 17 | UnwindData |  |
