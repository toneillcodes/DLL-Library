# Binary Specification: hnetcfg.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\hnetcfg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6283eebb0a70f968d1c21970d5afa8b5a7b5bb41435732c0799a804e76695c0f`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllGetClassObject` | `0xD9A0` | 139 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0xDAC0` | 77 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x16CA0` | 18,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllUnregisterServer` | `0x16CA0` | 18,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `HNetDeleteRasConnection` | `0x1B4A0` | 341 | UnwindData |  |
| 14 | `WinBomConfigureWindowsFirewall` | `0x1B840` | 499 | UnwindData |  |
| 11 | `RegisterClassObjects` | `0x240C0` | 322 | UnwindData |  |
| 12 | `ReleaseSingletons` | `0x24210` | 194 | UnwindData |  |
| 13 | `RevokeClassObjects` | `0x242E0` | 391 | UnwindData |  |
| 8 | `HNetGetFirewallSettingsPage` | `0x2A8F0` | 631 | UnwindData |  |
| 2 | `HNetFreeSharingServicesPage` | `0x2B8A0` | 307 | UnwindData |  |
| 3 | `HNetGetSharingServicesPage` | `0x2B9E0` | 583 | UnwindData |  |
| 9 | `HNetSharedAccessSettingsDlg` | `0x2FEB0` | 417 | UnwindData |  |
| 10 | `HNetSharingAndFirewallSettingsDlg` | `0x30060` | 801 | UnwindData |  |
