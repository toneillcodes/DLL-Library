# Binary Specification: hnetcfg.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\hnetcfg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8b52c7e1d3db7a08b8249817837f432bcc1982f3a5309aaecb71b4092ada2aaf`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllGetClassObject` | `0xD820` | 139 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0xD940` | 77 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x169D0` | 18,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllUnregisterServer` | `0x169D0` | 18,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `HNetDeleteRasConnection` | `0x1B1D0` | 341 | UnwindData |  |
| 14 | `WinBomConfigureWindowsFirewall` | `0x1B570` | 499 | UnwindData |  |
| 11 | `RegisterClassObjects` | `0x23DF0` | 322 | UnwindData |  |
| 12 | `ReleaseSingletons` | `0x23F40` | 194 | UnwindData |  |
| 13 | `RevokeClassObjects` | `0x24010` | 391 | UnwindData |  |
| 8 | `HNetGetFirewallSettingsPage` | `0x2A620` | 631 | UnwindData |  |
| 2 | `HNetFreeSharingServicesPage` | `0x2B5D0` | 307 | UnwindData |  |
| 3 | `HNetGetSharingServicesPage` | `0x2B710` | 583 | UnwindData |  |
| 9 | `HNetSharedAccessSettingsDlg` | `0x2FBE0` | 417 | UnwindData |  |
| 10 | `HNetSharingAndFirewallSettingsDlg` | `0x2FD90` | 801 | UnwindData |  |
