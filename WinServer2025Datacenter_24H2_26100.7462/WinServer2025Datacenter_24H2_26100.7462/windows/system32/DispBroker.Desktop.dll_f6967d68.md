# Binary Specification: DispBroker.Desktop.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\DispBroker.Desktop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f6967d68434874df5b1766af5a5357f1099d5cb572d3828e13d2fe71257a750c`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x21220` | 434 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x37010` | 138 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x370A0` | 242 | UnwindData |  |
| 5 | `ServiceMain` | `0x37B90` | 30 | UnwindData |  |
| 6 | `SvchostPushServiceGlobals` | `0x37BC0` | 325,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetProxyDllInfo` | `0x87210` | 124,160 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
