# Binary Specification: netshell.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netshell.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6c49be01554d453dff2af1f286de518d6a2043e1c2bf3b176a6fcb20d5c45baa`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0xA580` | 180 | UnwindData |  |
| 12 | `NcFreeNetconProperties` | `0xA730` | 67 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x20FA0` | 6,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x20FA0` | 6,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x22990` | 51 | UnwindData |  |
| 5 | `HrCreateDesktopIcon` | `0x229D0` | 252 | UnwindData |  |
| 6 | `HrGetIconFromMediaType` | `0x22AE0` | 91 | UnwindData |  |
| 7 | `HrGetIconFromMediaTypeEx` | `0x22B50` | 80 | UnwindData |  |
| 8 | `HrLaunchConnection` | `0x22BB0` | 234 | UnwindData |  |
| 9 | `HrLaunchConnectionEx` | `0x22CA0` | 371 | UnwindData |  |
| 10 | `HrLaunchPropertiesSheet` | `0x22E20` | 261 | UnwindData |  |
| 11 | `HrRenameConnection` | `0x22F30` | 243 | UnwindData |  |
| 13 | `NcIsValidConnectionName` | `0x23030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `StartNCW` | `0x23040` | 269,856 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
