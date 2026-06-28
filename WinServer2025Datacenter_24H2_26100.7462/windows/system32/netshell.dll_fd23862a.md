# Binary Specification: netshell.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\netshell.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fd23862ab577f78c9bd5db77e3375cc55dd0dd2b3bf3178df0b01c0547ef8e9a`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0xA670` | 180 | UnwindData |  |
| 12 | `NcFreeNetconProperties` | `0xA820` | 67 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x21160` | 6,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x21160` | 6,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x22B50` | 51 | UnwindData |  |
| 5 | `HrCreateDesktopIcon` | `0x22B90` | 252 | UnwindData |  |
| 6 | `HrGetIconFromMediaType` | `0x22CA0` | 91 | UnwindData |  |
| 7 | `HrGetIconFromMediaTypeEx` | `0x22D10` | 80 | UnwindData |  |
| 8 | `HrLaunchConnection` | `0x22D70` | 234 | UnwindData |  |
| 9 | `HrLaunchConnectionEx` | `0x22E60` | 371 | UnwindData |  |
| 10 | `HrLaunchPropertiesSheet` | `0x22FE0` | 261 | UnwindData |  |
| 11 | `HrRenameConnection` | `0x230F0` | 243 | UnwindData |  |
| 13 | `NcIsValidConnectionName` | `0x231F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `StartNCW` | `0x23200` | 293,733 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
