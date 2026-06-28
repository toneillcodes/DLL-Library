# Binary Specification: icfupgd.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\icfupgd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `776cd3b03f5196466448300515ca13b0217bee3dac74944d4fc0e107f4eeae14`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE490` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xE4C0` | 103 | UnwindData |  |
| 3 | `DllMain` | `0xE610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xE630` | 335 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xE790` | 29,852 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
