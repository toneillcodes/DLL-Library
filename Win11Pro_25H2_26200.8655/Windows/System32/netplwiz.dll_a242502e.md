# Binary Specification: netplwiz.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netplwiz.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a242502ec268b2846d30ccb15ba6234c9a5e503cfd6f22c6853ce776f552516e`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `SHDisconnectNetDrives` | `0xBB70` | 154 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xC060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xC080` | 26 | UnwindData |  |
| 1 | `ClearAutoLogon` | `0xD790` | 130 | UnwindData |  |
| 5 | `NetPlacesWizardDoModal` | `0x10180` | 587 | UnwindData |  |
| 4 | `NetAccessWizard` | `0x15670` | 860 | UnwindData |  |
| 7 | `UsersRunDllW` | `0x18860` | 911 | UnwindData |  |
