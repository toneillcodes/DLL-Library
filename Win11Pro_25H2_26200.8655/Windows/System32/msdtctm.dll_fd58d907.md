# Binary Specification: msdtctm.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msdtctm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fd58d90771ed9517b8c507fc7c0a834acd14a2a8a35a79e1292a1114a0be13ff`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DtcMainExt` | `0x40D0` | 5,227 | UnwindData |  |
| 11 | `DllGetClassObject` | `0x108D0` | 459 | UnwindData |  |
| 9 | `CreateInstance` | `0x28740` | 203 | UnwindData |  |
| 7 | `ASCDefer` | `0x78130` | 126 | UnwindData |  |
| 6 | `ASCDeliverDeferred` | `0x781C0` | 126 | UnwindData |  |
| 8 | `ASCGetSafeReference` | `0x78250` | 145 | UnwindData |  |
| 5 | `ASCWrapObject` | `0x782F0` | 311 | UnwindData |  |
| 10 | `ASCWrapClassFactory` | `0x78430` | 275 | UnwindData |  |
| 12 | `GetTipFunctionalityWorking` | `0x7C3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `SetTipFunctionalityWorking` | `0x7C3C0` | 272,380 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
